# graph/agent_graph.py
'''
Docstring for 04_AgenticRAG.graph.agent_graph
This module builds the agent graph for the Agentic RAG system.
It defines the graph structure, nodes, and routing logic based on query classification.
'''
from typing import Literal, List
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, END

from langchain_core.messages import BaseMessage
from services.llm import classify_query, RouterDecision

# Nodes imports
from tools.chitchat import chitchat_node
from tools.oos import oos_node
from tools.rag import rag_node
from tools.metadata import metadata_node
from LoggerSetUp import setup_logger


from config import(
    LOGS_BASE_PATH,
    LOG_LEVEL,
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


class GraphState(TypedDict, total=False):
    '''
    State dictionary for the agent graph.

    It contains:
    - question: str
    - category: Literal["BN", "MD", "CC", "OOC"]
    - answer: str
    - router_raw: dict (optional, to see the full object)
    - relevant_tables: list[str] (for MD queries)

    '''
    question: str
    chat_history: List[BaseMessage]

    # Router outputs
    category: Literal["BN", "MD", "CC", "OOC"]
    needs_context: bool
    contextualized_query: str
    router_raw: dict  # Optional, to see the full object
    keywords : list[str]
    CorrectedQuery : str
    relevant_tables: list[str]  # Tables needed for metadata queries
    user_language: str
    answer: str


async def router_node(state: GraphState) -> GraphState:
    """
    Router node that classifies the user's question into categories.

    Expects in state:
      - question: str

    Returns in state:
      - category (Literal["BN", "MD", "CC", "OOC"])
      - router_raw (dict): full decision object
      - relevant_tables (list[str]): for MD queries
      - answer (str): for debugging, shows selected category

    Args:
        state(GraphState):  containing the current state, expects "question" key.
    Returns:
        GraphState: with updated keys "category", "router_raw", "relevant_tables", and "answer".
    """
    question = state["question"]
    history = state.get("chat_history", [])

    decision: RouterDecision = await classify_query(question, history)

    new_state = state.copy() 

    new_state["needs_context"] = decision.needs_context
    new_state["contextualized_query"] = decision.contextualized_query
    new_state["category"] = decision.category
    new_state["router_raw"] = decision.model_dump()
    new_state["keywords"] = decision.keywords
    new_state["relevant_tables"] = decision.relevant_tables
    new_state["user_language"] = decision.user_language
    
    # Logic for selecting the best query version
    if decision.needs_context:
        new_state["CorrectedQuery"] = decision.contextualized_query
    else:
        new_state["CorrectedQuery"] = decision.CorrectedQuery

    # Debugging Output
    logger.debug(f"Router Decision: {decision.category}")
    
    # Construct a debug answer
    debug_msg = (
        f"Selected Category: **{decision.category}**\n"
        f"Needs Context: {decision.needs_context}\n"
    )
    if decision.contextualized_query:
        debug_msg += f"Contextualized: {decision.contextualized_query}"

    logger.debug(f"Router Debug Message: {debug_msg}") 
    new_state["answer"] = debug_msg

    return new_state


def route_from_state(state: GraphState) -> str:
    """
    Routing function to determine the next node based on the category.

    Args:
        state (GraphState): containing the current state with "category" key.
    Returns:
        str: the name of the next node to route to.
    """
    category = state["category"]

    return category
    

def build_agent_graph()-> StateGraph:
    """
    Builds the agent graph with a router node.
    Returns:
        StateGraph: compiled agent graph.
    """
    graph = StateGraph(GraphState)

    # Nodes declarations
    graph.add_node("router", router_node)
    graph.add_node("cc_node", chitchat_node)
    graph.add_node("oos_node", oos_node)
    graph.add_node("rag_node", rag_node)
    graph.add_node("md_node", metadata_node)


    # Edges and routing
    graph.set_entry_point("router")
    graph.add_conditional_edges(
        "router", route_from_state,
        {
            "CC": "cc_node",
            "BN": "rag_node",
            "MD": "md_node",
            "OOC": "oos_node",
        })

    # Final edges to END
    graph.add_edge("cc_node", END)
    graph.add_edge("oos_node", END)
    graph.add_edge("rag_node", END)
    graph.add_edge("md_node", END)


    return graph.compile()
