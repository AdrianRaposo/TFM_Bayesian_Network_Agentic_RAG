# tools/chitchat.py
'''
Docstring for 04_AgenticRAG.tools.chitchat
This module contains the chit-chat tool for casual conversations in the Agentic RAG system.
It defines a node that processes user questions and generates appropriate chit-chat responses.
'''
from json import tool
from typing import Dict, Any

from services.llm import generate_chitchat_reply

def chitchat_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Node to handle chit-chat conversations.
    Expects in state:
      - question: str
    Returns in state:
      - answer: str
    Args:
        state (Dict[str, Any]): containing the current state, expects "question" key. 
    Returns:
        Dict[str, Any]: with updated key "answer".
    """
    question: str = state["question"]
    user_language = state.get("user_language", "English")
    reply = generate_chitchat_reply(question, user_language)

    new_state = dict(state)
    new_state["answer"] = reply
    return new_state