import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.messages import AIMessage, HumanMessage

# Import the weather tool we just created
from weather_tool import get_current_weather

# --- LLM Imports (Groq chosen) ---
from langchain_groq import ChatGroq
# ---------------------------------------------------

# 1. Load environment variables
load_dotenv()

# 2. Initialize the LLM (Using Groq)
# You need to have GROQ_API_KEY set in your .env file
llm = ChatGroq(model_name="llama3-8b-8192", groq_api_key=os.environ.get("GROQ_API_KEY"))

# 3. Define the tools the agent can use
tools = [get_current_weather] # Our tool remains the same

# 4. Define the Agent Prompt for create_tool_calling_agent
# This prompt is simpler as tool-calling models handle tool structure internally
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant specialized in providing current weather information."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

# 5. Create the Tool-Calling Agent
# This should be more robust
agent = create_tool_calling_agent(llm, tools, prompt)

# 6. Create the Agent Executor
# Set verbose=True to see the internal steps (tool calls, observations)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 7. Main loop for interaction
if __name__ == "__main__":
    print("Simple Weather Bot: Ask me about the current weather in any city!")
    print("Type 'exit' to quit.")

    chat_history = []

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Re-adding the try...except block for robust error handling during normal operation
        try:
            # Invoke the agent executor with the user's input and current chat history
            response = agent_executor.invoke(
                {"input": user_input, "chat_history": chat_history}
            )
            agent_response = response["output"]
            print(f"Bot: {agent_response}")

            # Update chat history for context in future turns
            chat_history.extend([HumanMessage(content=user_input), AIMessage(content=agent_response)])

        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again or check the logs if you are encountering repeated issues.")