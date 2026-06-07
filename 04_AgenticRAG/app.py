# app.py
'''
Docstring for 04_AgenticRAG.app
This is the main application file for the Agentic RAG system using Chainlit.
It sets up the chat interface, initializes the agent graph,
and handles user messages.
'''
import chainlit as cl

from graph.agent_graph import build_agent_graph
from langchain_core.messages import HumanMessage, AIMessage


@cl.on_chat_start
async def on_chat_start():
    """
    When the chat starts, we build the agent graph and store it in the user session.
    This way, we can reuse the same graph for each message from the user.
    1. The graph is built using the `build_agent_graph` function.
    2. The graph is stored in the user session using `cl.user_session.set`.
    3. This allows us to maintain state and context across multiple messages.
    4. The graph can be retrieved later in the `on_message` handler.
    """
    # Build the agent graph
    graph = build_agent_graph()
    # Store the graph in the user session
    cl.user_session.set("graph", graph)
    # Initialize chat history
    cl.user_session.set("chat_history", [])


@cl.on_message
async def on_message(message: cl.Message):
    graph = cl.user_session.get("graph")
    history = cl.user_session.get("chat_history") or []
    user_input = message.content

    input_state = {
          "question": user_input, 
          "chat_history": history
    }

    # 1. STATUS Message (Replaces the Steps that caused errors)
    # This message will update its text to tell you what the system is doing
    status_msg = cl.Message(content="⏳ Starting...", author="System")
    await status_msg.send()

    # 2. Message for the FINAL ANSWER (will be populated gradually via streaming)
    final_msg = cl.Message(content="")
    await final_msg.send()

    # Text configuration for each state
    status_texts = {
        "router": "Analyzing your intent...",
        "rag_node": "Searching for documents and context...",
        "md_node": "Preparing database query...",
        "cc_node": "Thinking of a response...",
        "oos_node": "Validating request..."
    }
    
    # Nodes that generate the visible final response
    final_nodes = {"rag_node", "cc_node", "md_node", "oos_node"}

    try:
        async for event in graph.astream_events(input_state, version="v2"):
            kind = event["event"]
            node_name = event.get("metadata", {}).get("langgraph_node", "")
            tags = event.get("tags", [])

            # --- A) UPDATE STATUS MESSAGE (Visual Feedback) ---
            
            # 1. Upon entering a new node
            if kind == "on_chain_start" and node_name in status_texts:
                status_msg.content = status_texts[node_name]
                await status_msg.update()

            # 2. Specific details within nodes
            if kind == "on_chat_model_start":
                # If we are in RAG and the model starts, it means documents were already searched
                if node_name == "rag_node":
                    status_msg.content = "Drafting response with found information..."
                    await status_msg.update()
                
                # If we are in Metadata (SQL)
                if node_name == "md_node":
                    if "final_answer" in tags:
                        status_msg.content = "Interpreting database results..."
                    else:
                        status_msg.content = "Generating and executing SQL code..."
                    await status_msg.update()

            # --- B) RESPONSE STREAMING (Final Text) ---
            
            if kind == "on_chat_model_stream" and node_name in final_nodes:
                should_stream = True
                
                # Hide SQL (Security Filter)
                if node_name == "md_node" and "final_answer" not in tags:
                    should_stream = False
                
                if should_stream:
                    content = event["data"]["chunk"].content
                    if content:
                        await final_msg.stream_token(content)

    except Exception as e:
        print(f"Error in process: {e}")
        final_msg.content += f"\n(An error occurred: {e})"
        await final_msg.update()
    
    finally:
        # On completion, remove the status message to keep the chat clean
        await status_msg.remove()
        
        # Save history and close response
        history.append(HumanMessage(content=user_input))
        history.append(AIMessage(content=final_msg.content))
        history = history[-2:]
        cl.user_session.set("chat_history", history)
        await final_msg.update()

@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="Example Question",
            message="What are Bayesian Networks?",
            icon="/public/Question.svg",
        )
    ]
