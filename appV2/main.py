# Imports
import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
from apikey import apikey

def main():
    # Define OpenAI API KEY
    os.environ['OPENAI_API_KEY'] = apikey

    # Title and description
    st.title("OpenAI CSV Query App")
    st.write("Upload a CSV file and query answers from your data.")

    # Upload File
    file =  st.file_uploader("Upload CSV file",type=["csv"])
    if not file: st.stop()

    # Read Data as Pandas
    data = pd.read_csv(file)

    # Display Data Head
    st.write("Data Preview:")
    st.dataframe(data.head()) 

    # Define pandas df agent - 0 ~ no creativity vs 1 ~ very creative
    agent = create_pandas_dataframe_agent(OpenAI(temperature=0.1),data,verbose=True) 
    
    # Define Generated and Past Chat Arrays
    if 'generated' not in st.session_state: 
        st.session_state['generated'] = []

    if 'past' not in st.session_state: 
        st.session_state['past'] = []

    # CSS for chat bubbles
    chat_bubble_style = \
    """
        .user-bubble {
            background-color: dodgerblue;
            color: white;
            padding: 8px 12px;
            border-radius: 15px;
            display: inline-block;
            max-width: 70%;
        }
        
        .gpt-bubble {
            background-color: #F3F3F3;
            color: #404040;
            padding: 8px 12px;
            border-radius: 15px;
            display: inline-block;
            max-width: 70%;
            text-align: right;
        }
    """

    # Apply CSS style
    st.write(f'<style>{chat_bubble_style}</style>', unsafe_allow_html=True)

    # Accept input from user
    query = st.text_input("Enter a query:") 

    # Execute Button Logic
    if st.button("Execute") and query:
        with st.spinner('Generating response...'):
            try:
                answer = agent.run(query)

                # Store conversation
                st.session_state.past.append(query)
                st.session_state.generated.append(answer)

                # Display conversation in reverse order
                for i in range(len(st.session_state.past)-1, -1, -1):
                    st.write(f'<div class="gpt-bubble">{st.session_state.generated[i]}</div>', unsafe_allow_html=True)
                    st.write(f'<div class="user-bubble">{st.session_state.past[i]}</div>', unsafe_allow_html=True)
                    st.write("")

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

  
if __name__ == "__main__":
    main()   
