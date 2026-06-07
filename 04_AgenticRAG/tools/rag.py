# tools/rag.py
'''
Docstring for 04_AgenticRAG.tools.rag
This module contains the RAG (Retrieval-Augmented Generation) tool for domain-specific questions in the Agentic RAG system.
It defines a node that processes questions by retrieving relevant context and generating answers using a RAG chain.
'''
import asyncio
from services.retrieval import retrieval_llm_context
from services.llm import get_rag_chain
from LoggerSetUp import setup_logger

from config import (
    MAX_RESULTS_RETRIEVED,
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

async def rag_node(state: dict) -> dict:
    """
    Node to handle RAG (Retrieval-Augmented Generation) for domain-specific questions.
    Expects in state:
      - CorrectedQuery: str
    Returns in state:
      - answer: str
    Args:
        state (dict): containing the current state, expects "CorrectedQuery" key.
        keywords (list): list of keywords for retrieval context.
    Returns:
        dict: with updated key "answer".
    """
    question: str = state["CorrectedQuery"]
    history: list[dict] = state.get("chat_history", [])
    keywords = state.get("keywords")
    question: str = state.get("CorrectedQuery", question)
    user_language = state.get("user_language", "English")
    logger.debug(f"RAG Node - Question: {question}, Keywords: {keywords}")

    logger.info(f"RAG Node - Processing question: {question}")
    context: str = retrieval_llm_context(question, keywords, top_k=MAX_RESULTS_RETRIEVED)
    logger.info( f"Processed context retrieved for question.")
    rag_chain = get_rag_chain()
    answer: str = await rag_chain.ainvoke(
        {
            "question": question,
            "context": context,
            "previous_chat_history": history,
            "user_language": user_language
        }
    )

    new_state = dict(state)
    new_state["answer"] = answer
    return new_state