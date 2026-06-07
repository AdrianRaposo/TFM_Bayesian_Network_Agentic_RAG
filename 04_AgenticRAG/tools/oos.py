# tools/oos.py
'''
Docstring for 04_AgenticRAG.tools.oos
This module contains the out-of-scope tool for handling queries that are beyond the system's capabilities.
It defines a node that provides a standard response for out-of-scope queries.
'''

from typing import Dict, Any
from pathlib import Path
from LoggerSetUp import setup_logger

from config import(
    PROMPTS_DIR,
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
    general_mode='w',
    error_mode='w'
)


def _load_prompt() -> str:
    '''
    Loads the out-of-scope prompt from the prompts directory.
    Returns:
        str: The content of the out-of-scope prompt.
    '''
    path = PROMPTS_DIR / "oos.md"
    if not path.exists():
        logger.error(f"Prompt file not found: {path}")
        raise FileNotFoundError(f"Prompt file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()
    
_OOS_PROMPT = _load_prompt()   


def oos_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Node to handle out-of-scope queries.
    Expects in state:
      - question: str
    Returns in state:
      - answer: str
    Args:
        state (Dict[str, Any]): containing the current state, expects "question" key. 
    Returns:
        Dict[str, Any]: with updated key "answer".
    """
    new_state = dict(state)
    new_state["answer"] = _OOS_PROMPT
    return new_state