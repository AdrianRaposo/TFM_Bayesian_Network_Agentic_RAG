# services/llm.py
'''
Docstring for 04_AgenticRAG.services.llm
This module contains LLM chains and functions for various tools used in the Agentic RAG system.
It includes:
- Router tool for classifying queries.
- Chit-chat tool for casual conversations.
- RAG tool for retrieval-augmented generation.
- Metadata tool for converting natural language to SQL and interpreting results.
'''
from functools import lru_cache
from typing import Literal, List


from langchain.chat_models import BaseChatModel
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable, chain
from langchain_core.messages import BaseMessage 

from services.retrieval import connect_db
from LoggerSetUp import setup_logger

from config import (
    LLM_PROVIDER_RAG,
    LLM_PROVIDER,
    OPENAI_API_KEY,
    OPENAI_API_MODEL,
    OPENAI_API_MODEL_ROUTER,
    GOOGLE_API_KEY,
    GEMINI_API_MODEL,
    GEMINI_API_MODEL_ROUTER,
    OLLAMA_BASE_URL,
    OLLAMA_MODEL,
    OLLAMA_MODEL_ROUTER,
    PROMPTS_DIR,
    MAX_TOKENS_RAG_RESPONSE,
    MAX_TOKEN_LLM,
    OPENAI_API_MODEL_ROUTER,
    LOGS_BASE_PATH,
    LOG_LEVEL,
    NOT_FOUND_PHRASE
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

# CLASS DEFINITIONS
class RouterDecision(BaseModel):
    """
    Defines the structure for router decision output.
    Attributes:
        category (Literal["BN", "MD", "CC", "OOC"]): The category of the query.
        needs_context (bool): Whether previous context is needed for the query.
        contextualized_query (str): The contextualized version of the query if needed.
        keywords (List[str]): List of keywords extracted from the query.
        CorrectedQuery (str): Corrected version of the query if applicable.
        relevant_tables (List[str]): List of relevant database tables for metadata queries.
    """
    category: Literal["BN", "MD", "CC", "OOC"]
    needs_context: bool = False
    contextualized_query: str = ""
    keywords: List[str] = []
    CorrectedQuery: str = ""
    relevant_tables: List[str] = []
    user_language: str = "English"


# GENERAL FUNCTIONS
def _load_prompt(name: str) -> str:
    """
    Loads a prompt template from the prompts directory.
    Args:
        name (str): Filename of the prompt template.
    Returns:
        str: Content of the prompt template.
    """ 
    path = PROMPTS_DIR / name
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# LLM INSTANCES
@lru_cache
def get_llm_rag(temperature: float = 0.5) -> BaseChatModel:
    """
    LLM specific for RAG tool.
    Args:
        temperature (float): Sampling temperature for the LLM.
    Returns:
        BaseChatModel: A configured instance of a LangChain chat model. Depending on the 
                       configuration, this will be one of:
                       - ChatOpenAI (OpenAI)
                       - ChatGoogleGenerativeAI (Google Gemini)
                       - ChatOllama (Local/Ollama)
    """

    logger.info(f"Initializing LLM for RAG with provider: {LLM_PROVIDER_RAG} and temperature: {temperature}")
    if LLM_PROVIDER_RAG == "gemini":
        return ChatGoogleGenerativeAI(
            model=GEMINI_API_MODEL,
            temperature=temperature,
            max_output_tokens=MAX_TOKENS_RAG_RESPONSE,
            google_api_key=GOOGLE_API_KEY,
        )
    elif LLM_PROVIDER_RAG == "ollama":
        return ChatOllama(
            model=OLLAMA_MODEL,
            base_url=OLLAMA_BASE_URL,
            temperature=temperature,
        )
    else: # Default a OpenAI
        return ChatOpenAI(
            model=OPENAI_API_MODEL,
            temperature=temperature,
            max_tokens=MAX_TOKENS_RAG_RESPONSE,
            api_key=OPENAI_API_KEY,
            streaming=True
        )

@lru_cache
def get_llm(temperature: float = 0.0) -> BaseChatModel:
    """
    LLm speecific for routing decisions.
    Args:
        temperature (float): Sampling temperature for the LLM. Default is 0.0 for deterministic routing.
    Returns:
        BaseChatModel: A configured instance of a LangChain chat model. Depending on the 
               configuration, this will be one of:
               - ChatOpenAI (OpenAI)
               - ChatGoogleGenerativeAI (Google Gemini)
               - ChatOllama (Local/Ollama)
    """


    logger.info(f"Initializing LLM for routing with provider: {LLM_PROVIDER} and temperature: {temperature}")

    if LLM_PROVIDER == "gemini":
        return ChatGoogleGenerativeAI(
            model=GEMINI_API_MODEL_ROUTER,
            temperature=temperature,
            max_output_tokens=MAX_TOKENS_RAG_RESPONSE,
            google_api_key=GOOGLE_API_KEY,
            # streaming=True # Gemini sometimes has quirks with streaming in complex chains, but you can enable it
        )
    elif LLM_PROVIDER == "ollama":
        return ChatOllama(
            model=OLLAMA_MODEL_ROUTER,
            base_url=OLLAMA_BASE_URL,
            temperature=temperature,
        )
    else: # Default a OpenAI
        return ChatOpenAI(
            model=OPENAI_API_MODEL_ROUTER,
            temperature=temperature,
            max_tokens=MAX_TOKENS_RAG_RESPONSE,
            api_key=OPENAI_API_KEY,
            streaming=True
        )


# ROTER TOOL FUNCTION
@lru_cache
def get_router_chain() -> BaseChatModel:
    '''
    LLM chain for routing decisions.
    Returns:
        ChatOpenAI: chain for routing.
    '''
    llm = get_llm()
    return llm.with_structured_output(RouterDecision)

async def classify_query(question: str, chat_history: List[BaseMessage]) -> RouterDecision:
    '''
    Classifies a query into one of the predefined categories.
    Args:
        question (str): The user's question.
        chat_history (List[BaseMessage]): The chat history.
    Returns:
        RouterDecision: The classification result.
    '''
    system_prompt = _load_prompt("router_prompt.md")

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="chat_history"), 
        ("human", "{question}")
    ])
    chain = prompt | get_router_chain()
    return await chain.ainvoke({
        "question": question, 
        "chat_history": chat_history
    })



# CHITCHAT TOOL FUNCTION
@lru_cache
def get_chitchat_chain()  -> Runnable[dict, str]:
    '''
    LLM chain for chit-chat conversations.
    Returns:
        Runnable[dict, str]: chain for chit-chat.
    '''
    system_prompt = _load_prompt("chitchat.md")
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("user", "IMPORTANT: You must write your final response exactly in this language: {user_language}.\n\nQuestion: {question}"),
        ]
    )
    llm = get_llm(temperature=0.8)
    return prompt | llm | StrOutputParser()

def generate_chitchat_reply(question: str,user_language: str = "English", callbacks: list | None = None) -> str:
    '''
    Generates a chit-chat reply using the LLM chain.
    Args:
        question (str): The user's question.
        user_language (str): The language in which to respond.
    Returns:
        str: The generated reply.
    '''
    chain = get_chitchat_chain()
    if callbacks:
        return chain.invoke({"question": question, "user_language": user_language}, config={"callbacks": callbacks})
    return chain.invoke({"question": question, "user_language": user_language})


# RAG TOOL FUNCTION
@lru_cache
def get_rag_chain()  -> Runnable[dict, str]:
    '''
    LLM chain for RAG (Retrieval-Augmented Generation).
    Returns:
        Runnable[dict, str]: chain for RAG.
    '''
    system_prompt = _load_prompt("rag_system.md")
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("user", "IMPORTANT: You must write your final response exactly in this language: {user_language}.\n\nQuestion: {question} \n\nContext: {context}"),
        ]
    )
    llm = get_llm_rag(temperature=0.2)
    return prompt | llm | StrOutputParser()


# METADTATA TOOL FUNCTION

def get_metadata_chain(table_schemas: dict) -> Runnable[dict, str]:
    '''
    LLM chain for converting natural language to SQL queries.
    Args:
        table_schemas (dict): Dictionary of table names and their DDL definitions.
    Returns:
        Runnable[dict, str]: chain for metadata SQL generation.
    '''
    base_system = _load_prompt("metadata_system.md")
    # Build a plain text schema section to avoid curly-brace variables
    ddl_sections: list[str] = []
    for tbl, ddl in table_schemas.items():
        section = f"-- {tbl}\n{ddl}".strip()
        ddl_sections.append(section)
    schema_text = "\n\n".join(ddl_sections)

    # Replace the placeholder with concrete text (no braces remain)
    system_prompt = base_system.replace("{table_schemas}", schema_text)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("user", "{question}"),
        ]
    )
    llm = get_llm(temperature=0.0)
    return prompt | llm | StrOutputParser()

def get_results_chain() -> Runnable[dict, str]:
    '''
    LLM chain for generating natural language response from SQL results.
    Returns:
        Runnable[dict, str]: chain for results interpretation.
    '''
    system_prompt = _load_prompt("metadata_results.md")
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("user", "IMPORTANT: You must write your final response exactly in this language: {user_language}.\n\nQuestion: {question}\n\nQuery Results:\n{results}"),
        ]
    )
    llm = get_llm(temperature=0.5)
    return prompt | llm | StrOutputParser()

def generate_sql_from_nl(question: str, table_schemas: dict, max_retries: int = 1, callbacks: list | None = None) -> str | None:
    '''
    Generates SQL from natural language with error recovery (1 retry).
    Args:
        question (str): Natural language question.
        table_schemas (dict): Dictionary of table schemas.
        max_retries (int): Number of retry attempts on SQL error.
    Returns:
        str | None: Generated SQL query string, or None if generation fails twice.
    '''
    
    
    chain = get_metadata_chain(table_schemas)
    
    current_prompt = question
    
    for attempt in range(max_retries + 1):
        try:
            # Generate SQL usando el prompt actual (que puede incluir el error previo)
            if callbacks:
                sql_query = chain.invoke({"question": current_prompt}, config={"callbacks": callbacks})
            else:
                sql_query = chain.invoke({"question": current_prompt})
                
            sql_query = sql_query.strip()
            
            if sql_query.startswith(NOT_FOUND_PHRASE) or sql_query.startswith("I cannot"):
                return sql_query
            
            # Try to execute EXPLAIN to validate
            conn = connect_db()
            with conn.cursor() as cur:
                cur.execute("EXPLAIN " + sql_query)  # Just explain, don't execute
            conn.close()
            
            return sql_query
            
        except Exception as e:
            error_msg = str(e)
            if attempt < max_retries:
                current_prompt = f"""{question}\n\nPrevious SQL attempt failed with error: {error_msg}\n\nPlease generate a corrected SQL query."""
                logger.warning(f"SQL generation failed on attempt {attempt + 1}. Retrying...")
            else:
                # Final attempt failed
                logger.error(f"Failed to generate SQL after {max_retries} retries. Last error: {error_msg}")
                return None

def generate_response_from_results(question: str, results: list[dict], user_language: str = "English", callbacks: list | None = None) -> str:
    '''
    Generates a natural language response from query results.
    Args:
        question (str): The original question.
        results (list[dict]): Query results (max 10 rows).
        user_language (str): The language in which to respond.
        callbacks (list | None): List of callbacks for the LLM chain.
    Returns:
        str: Natural language response.
    '''
    chain = get_results_chain()
    results_str = "\n".join([str(row) for row in results])

    config_args = {
        "tags": ["final_answer"] 
    }

    if callbacks:
        config_args["callbacks"] = callbacks

    return chain.invoke(
        {"question": question, "results": results_str, "user_language": user_language}, 
        config=config_args
    )