# Imports
import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI

def main():
    # Load the OpenAI API key from the environment variable
    load_dotenv()
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else: print("OPENAI_API_KEY is set")

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

    # Accept input from user
    query = st.text_input("Enter a query:") 

    # Execute Button Logic
    if st.button("Execute"):
        answer = agent.run(query)
        st.write("Answer:")
        st.write(answer)

  
if __name__ == "__main__":
    main()   
