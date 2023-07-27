# Imports
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from langchain.agents import create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.agents.agent_types import AgentType
from html_templates import css, user_template, bot_template


def main():
    st.set_page_config(page_title="Pandas Agent")
    st.subheader("OpenAI LangChain Pandas Agent Chatbot")
    st.write("Upload a CSV or XLSX file and query answers from your data.")

    # Apply CSS
    st.write(css, unsafe_allow_html=True)

    # Define chat history session state variable
    st.session_state.setdefault('chat_history', [])

    # Temperature slider
    with st.sidebar:
        with st.expander("Settings",  expanded=True):
            TEMP = st.slider(label="LLM Temperature", min_value=0.0, max_value=1.0, value=0.5)

    # Upload File
    file =  st.file_uploader("Upload CSV file",type=["csv","xlsx"])
    if not file: st.stop()

    # Read Data as Pandas
    data = pd.read_csv(file)

    # Display Data Head
    st.write("Data Preview:")
    st.dataframe(data.head()) 


    # Define large language model (LLM)
    llm = OpenAI(temperature=TEMP)

    # Define pandas df agent
    agent = create_pandas_dataframe_agent(llm, 
                                          data, 
                                          verbose=True
    ) 

    # Accept input from user
    query = st.text_input("Enter a query:") 

    # Execute Button Logic
    if st.button("Execute") and query:
        with st.spinner('Generating response...'):
            try:
                # Define prompt for agent
                prompt = f'''
                    Consider the uploaded pandas data, respond intelligently to user input
                    \nCHAT HISTORY: {st.session_state.chat_history}
                    \nUSER INPUT: {query}
                    \nAI RESPONSE HERE:
                '''

                # Get answer from agent
                answer = agent.run(prompt)

                # Store conversation
                st.session_state.chat_history.append(f"USER: {query}")
                st.session_state.chat_history.append(f"AI: {answer}")

                # Display conversation in reverse order
                for i, message in enumerate(reversed(st.session_state.chat_history)):
                    if i % 2 == 0: st.markdown(bot_template.replace("{{MSG}}", message), unsafe_allow_html=True)
                    else: st.markdown(user_template.replace("{{MSG}}", message), unsafe_allow_html=True)

            # Error Handling
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

  
if __name__ == "__main__":
    load_dotenv() # Import enviornmental variables
    main()   

