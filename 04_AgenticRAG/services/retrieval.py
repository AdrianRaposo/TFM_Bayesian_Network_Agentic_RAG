# services/retrieval.py
'''
Docstring for 04_AgenticRAG.services.retrieval
This module provides functions for connecting to a PostgreSQL database,
generating text embeddings, and retrieving relevant document chunks using
various retrieval strategies including BM25 and dense vector similarity.
It also includes a hybrid retrieval pipeline that combines these methods and
prepares context for LLMs.
It contains:
- Database connection utilities
- Embedding generation functions
- Retrieval functions (BM25, dense vector)
- Re-ranking and context preparation for LLMs
- Hybrid retrieval pipeline
'''

from __future__ import annotations
import re
import psycopg
import torch

from psycopg.rows import dict_row
from sentence_transformers import SentenceTransformer
from typing import List, Dict
from functools import lru_cache
from LoggerSetUp import setup_logger


from config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
    DB_SCHEMA,
    EMBEDDING_MODEL_NAME,
    DB_CHUNKS_TABLE as CHUNK_TABLE,
    DB_ABSTRACTS_TABLE as ABSTRACT_TABLE,
    DB_DOC_METADATA_TABLE as DOC_METADATA_TABLE,
    DB_DOC_AUTHORS_TABLE as DOC_AUTHORS_TABLE,
    N_MAX_DOC_REPETITION,
    PONDERTATION_ALPHA,
    PONDERTATION_BETA,
    PONDERTATION_GAMMA,
    GET_DOC_METADATA_QUERY_RAG,
    SEARCH_CHUNKS_QUERY_BM25_RAG,
    SEARCH_ABSTRACTS_QUERY_RAG,
    GET_TOP_CHUNKS_PER_DOC_QUERY_RAG,
    GET_TOP_DENSE_CHUNKS_QUERY_RAG,
    LOGS_BASE_PATH,
    LOG_LEVEL
)

logger = setup_logger(
    name=__name__,
    logs_base_path=LOGS_BASE_PATH,
    general_log_filename='AgenticRAG.log',
    error_log_filename='AgenticRAG_error.log',
    general_level=LOG_LEVEL,
    error_level='ERROR',
    general_mode='a',
    error_mode='a'
)



# EMBEDDING MODEL LOADING WITH CACHING
@lru_cache
def get_embedding_model(modelName=EMBEDDING_MODEL_NAME) -> SentenceTransformer:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    return SentenceTransformer(modelName, device=device)

# DATABASE CONNECTION AND EMBEDDING UTILITIES

def connect_db() -> psycopg.Connection:
    """Establish a connection to the PostgreSQL database."""
    return psycopg.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        row_factory=dict_row
    )

def get_embbedding(text: str, model_name: str = EMBEDDING_MODEL_NAME) -> list[float]:
    """
    Generates a vector embedding for the given text using the specified model.
    Args:
        text (str): The input text to be embedded.
        model_name (str): The name of the sentence transformer model to use for embedding.
    Returns:
        list[float]: The vector embedding of the input text.
    """
    model = get_embedding_model(modelName=model_name)
    arr =  model.encode(text, normalize_embeddings=True).tolist()
    return "[" + ",".join(f"{float(x):.6f}" for x in arr) + "]"

def get_doc_list( abstracts: List[Dict])-> list[str]:
    '''
    Converts a list of abstract dictionaries to a comma-separated string of document IDs.
    Args:
        abstracts (List[Dict]): List of dictionaries containing 'doc_id' keys.
    Returns:
        list[str]: List of document IDs.
    '''
    doc_ids = [str(abstract['doc_id']) for abstract in abstracts]
    return doc_ids


# RETRIEVAL FUNCTIONS

def fetch_bm25_chunks(conn, keywords: List[str], query_emb: list[float] , limit: int = 10) -> List[Dict]:
    '''
    Fetches document chunks from the database using BM25 ranking based on the provided keywords.

    Args:
        conn (psycopg.Connection): Database connection object.
        keywords (List[str]): List of keywords for the search query.
        query_emb (np.ndarray): Embedding of the original query for dense similarity calculation.
        limit (int, optional): Number of chunks to retrieve. Defaults to 10.
    Returns:
        List[Dict]: List of document chunks with their metadata and similarity scores.
    '''
    
    query_terms = ' & '.join(re.sub(r'\\W+', '', kw.lower()).replace(' ', ' & ') for kw in keywords)

    sql = SEARCH_CHUNKS_QUERY_BM25_RAG.format(
        schema=DB_SCHEMA,
        table=CHUNK_TABLE
    )

    with conn.cursor() as cur:
        cur.execute(sql, ((query_terms), query_emb, str(query_terms), int(limit)))
        rows = cur.fetchall()
        chunks = []
        for r in rows:
            chunks.append({
            "chunk_pk": r['chunk_pk'],
            "doc_id": r['doc_id'],
            "page_content": r['page_content'],
            "bm25_rank": r['rank'],
            "dense_dist": r['dist'],
            "source": "bm25"
            })
    return chunks

def fetch_top_abstracts(conn: psycopg.Connection, query_emb: list[float], limit=5) -> List[Dict]:
    '''
    Fetches top abstracts from the database based on dense vector similarity.
    Args:
        conn (psycopg.Connection): Database connection object.
        query_emb (list[float]): Embedding of the original query for similarity calculation.
        limit (int, optional): Number of abstracts to retrieve. Defaults to 5.
    Returns:
        List[Dict]: List of abstracts with their document IDs and similarity scores.
    '''     
    sql = SEARCH_ABSTRACTS_QUERY_RAG.format(
        schema=DB_SCHEMA,
        table=ABSTRACT_TABLE
    )

    with conn.cursor() as cur:
        cur.execute(sql, (query_emb, query_emb, limit))
        return cur.fetchall()

def fetch_chunks_by_doc(conn: psycopg.Connection, doc_ids: List[int], query_emb: list[float], limit=2) -> List[Dict]:
    '''
    Fetches document chunks from the database for specific document IDs based on dense vector similarity.
    Args:
        conn (psycopg.Connection): Database connection object.
        doc_ids (List[int]): List of document IDs to filter chunks.
        query_emb (list[float]): Embedding of the original query for similarity calculation.
        limit (int, optional): Number of chunks to retrieve per document. Defaults to 2.
    Returns:
        List[Dict]: List of document chunks with their metadata and similarity scores.
    '''
    sql = GET_TOP_CHUNKS_PER_DOC_QUERY_RAG.format(
        schema=DB_SCHEMA,
        table=CHUNK_TABLE
    )
    
    with conn.cursor() as cur:
        cur.execute(sql, (query_emb, query_emb, doc_ids, limit))
        rows = cur.fetchall()
        return [{"chunk_pk": r['chunk_pk'], 
                 "doc_id": r['doc_id'], 
                 "page_content": r['page_content'], 
                 "dense_dist": r['dist'], 
                 "source": "dense_abstract"} for r in rows]

def fetch_top_dense_chunks(conn : psycopg.Connection, query_emb: list[float], limit: int =10) -> List[Dict]:
    '''
    Fetches top document chunks from the database based on dense vector similarity. 
    Args:
        conn (psycopg.Connection): Database connection object.
        query_emb (list[float]): Embedding of the original query for similarity calculation.
        limit (int, optional): Number of chunks to retrieve. Defaults to 10.
    Returns:
        List[Dict]: List of document chunks with their metadata and similarity scores.
        
    '''

    sql = GET_TOP_DENSE_CHUNKS_QUERY_RAG.format(
        schema=DB_SCHEMA,
        table=CHUNK_TABLE
    )

    with conn.cursor() as cur:
        cur.execute(sql, (query_emb, query_emb, limit))
        rows = cur.fetchall()
        return [{"chunk_pk": r['chunk_pk'],
                  "doc_id": r['doc_id'],
                  "page_content": r['page_content'],
                  "dense_dist": r['dist'],
                  "source": "dense_global"} for r in rows]


#RE-RANKING, HYBRID RETRIEVAL PIPELINE AND CONTEXT PREPARATION

def rerank(
    chunks: List[Dict], 
    keywords: List[str], 
    alpha: float = PONDERTATION_ALPHA, 
    beta: float = PONDERTATION_BETA, 
    gamma: float = PONDERTATION_GAMMA, 
    top_k: int = 10
) -> List[Dict]:
    """
    Re-ranks retrieved chunks using a weighted combination of semantic similarity, keyword coverage, and diversity.

    Args:
        chunks (List[Dict]): List of retrieved chunks.
        keywords (List[str]): Keywords extracted from the query.
        alpha (float): Weight for semantic similarity (dense retrieval).
        beta (float): Weight for keyword match (BM25-like).
        gamma (float): Penalty for redundant chunks from the same document.
        top_k (int): Number of chunks to return.

    Returns:
        List[Dict]: Top-k re-ranked chunks.
    """
    seen_docs = {}
    reranked = []

    n_max_doc_repetition = N_MAX_DOC_REPETITION

    for chunk in chunks:
        text = chunk["page_content"].lower()

        # Keyword match score: ratio of matched keywords
        found_keywords = sum(1 for kw in keywords if kw in text)
        keyword_score = found_keywords / max(len(keywords), 1)

        # Semantic similarity: flip negative dot product from <#> to similarity (range 0–1+)
        raw_dense_dist = chunk.get("dense_dist", 0.0)
        sim = max(min(-raw_dense_dist, 1.0), 0.0)
        semantic_score = sim  # because <#> is negative dot product

        # Diversity penalty: reduce score if multiple chunks from same document
        doc_penalty = (1 - (  seen_docs.get(chunk["doc_id"], 0) / n_max_doc_repetition )  ) * gamma

        # Final score: weighted sum minus penalty
        final_score = alpha * semantic_score + beta * keyword_score - doc_penalty
        chunk["final_score"] = final_score
        reranked.append(chunk)

        # Track how many chunks we’ve used from this doc
        seen_docs[chunk["doc_id"]] = seen_docs.get(chunk["doc_id"], 0) + 1

    # Sort by final score
    reranked.sort(key=lambda x: x["final_score"], reverse=True)
    return reranked[:top_k]

def prepare_chunks_for_llm(conn: psycopg.Connection, chunks: List[Dict]) -> str:
    '''
    Prepares the retrieved chunks for input to the LLM by concatenating their content.

    Args:
        conn (psycopg.Connection): Database connection objec for obtaining additional metadata.
        chunks (List[Dict]): List of document chunks.   
    Returns:
        str: Concatenated string of chunk contents.
    '''
    context_string = ""

    sql = GET_DOC_METADATA_QUERY_RAG.format(
        schema=DB_SCHEMA,
        meta_table=DOC_METADATA_TABLE,
        auth_table=DOC_AUTHORS_TABLE
    )

    for chunk in chunks:
        with conn.cursor() as cur:
            cur.execute(sql,(chunk['doc_id'],))
            r = cur.fetchone()
            context_string += (f"---\n"
                f"{r['title']}, {r['year']}, {r['journal_name']}, {r['doi_url']}, {r['authors']}\n\n"
                f"{chunk['page_content']}\n")
            
    return context_string   
            
def hybrid_retrieval_pipeline(query: str, conn: psycopg.Connection, keywords: List[str], top_k=10,model_name=EMBEDDING_MODEL_NAME) -> List[Dict]:

    '''
    Hybrid retrieval pipeline combining BM25 and dense vector methods to fetch relevant document chunks.

    Args:
        query (str): The user's query.
        conn (psycopg.Connection): Database connection object.
        keywords (List[str]): Keywords extracted from the query.
        top_k (int, optional): Number of chunks to retrieve. Defaults to 10.
    Returns:
        List[Dict]: List of top-k relevant document chunks.
    '''
    limit_abstracts = top_k // 2
                                                                             
    query_emb = get_embbedding(query, model_name=model_name) 
    # Retrieve chunks using BM25 and dense methods
    bm25_chunks = fetch_bm25_chunks(conn, keywords, query_emb, limit=top_k)
    # Retrieve top abstracts and their chunks
    top_abstracts = fetch_top_abstracts(conn, query_emb, limit=limit_abstracts)
    doc_ids = get_doc_list(top_abstracts)
    dense_chunks_abstract = fetch_chunks_by_doc(conn, doc_ids, query_emb, limit=2)
    # Retrieve top dense chunks globally
    dense_chunks_global = fetch_top_dense_chunks(conn, query_emb, limit=4)
    
    # Combine all retrieved chunks
    all_chunks = bm25_chunks + dense_chunks_abstract + dense_chunks_global
    top_chunks = rerank(chunks=all_chunks, keywords=keywords, top_k=top_k)

    # FOR DEBUGGING PURPOSES ONLY
    if LOG_LEVEL == "DEBUG":
        with open("results_retrieval.txt", "w", encoding="utf-8") as f:
            for chunk in top_chunks:
                f.write(
                    f"DocID: {chunk['doc_id']} | "
                    f"SemanticScore: {chunk.get('dense_dist', 0):.4f} | "
                    f"Score: {chunk['final_score']:.4f} | "
                    f"Source: {chunk['source']}\n"
                    f"------------\n{chunk['page_content']}\n------------\n"
                )

    return top_chunks

def retrieval_llm_context(query: str, keywords: List[str], top_k=10) -> str:
    '''
    Retrieves relevant document chunks and prepares them as context for the LLM.

    Args:
        query (str): The user's query.
        keywords (List[str]): Keywords extracted from the query.
        top_k (int, optional): Number of chunks to retrieve. Defaults to 10.
    Returns:
        str: Concatenated string of chunk contents for LLM context.
    '''
    conn = connect_db()
    with conn:
        top_chunks = hybrid_retrieval_pipeline(query, conn, keywords, top_k, model_name=EMBEDDING_MODEL_NAME)
        context_string = prepare_chunks_for_llm(conn, top_chunks)
        conn.close()

        if LOG_LEVEL == "DEBUG":
            #FOR DEBUGGING PURPOSES ONLY
            with open("results_context.txt", "w", encoding="utf-8") as f:
                f.write("---- KEYWORDS ----\n")
                f.write(", ".join(keywords) + "\n\n")
                f.write("----CONTEXT FOR LLM----\n")
                f.write(context_string)
        
        conn.close()

    return context_string
    

