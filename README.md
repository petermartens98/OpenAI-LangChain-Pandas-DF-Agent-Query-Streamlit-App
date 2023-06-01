# OpenAI LangChain Pandas DF Agent Query Streamlit App

### App V2 Improvemnts
Added conversational memory and the abiliy for a continuous chat istead of a single Q&A

### Description
Python Streamlit web application designed to provide a user-friendly interface for querying and communicated with data from a CSV file using the OpenAI language model. 

The script begins by importing the necessary libraries, including os for operating system interactions, streamlit for building web applications, pandas for data manipulation, dotenv for loading environment variables, and langchain to for interacting with the openAI API and creating a Pandas DF agent. 

The main functionality of the script is contained within the main() function. It starts by loading the OpenAI API key from the environment variable and checking its existence. Then, it sets up the Streamlit application by displaying a title and description. The user is prompted to upload a CSV file, which is read using pandas and displayed as a preview. 

A pandas dataframe agent is created using the OpenAI language model, and the user is prompted to enter a query. Upon clicking the "Execute" button, the query is sent to the agent, and the answer as well as conversation is displayed on the application interface. Overall, this script provides a convenient way for users to interact with their CSV data and obtain answers based on their queries using the OpenAI language model.
### Example Screenshots App V2
![image](https://github.com/petermartens98/OpenAI-LangChain-Pandas-DF-Agent-Query-Streamlit-App/assets/87671757/2ca0d05b-3eff-48fc-8426-237634bc9661)

### Example Screenshots App V1
![image](https://github.com/petermartens98/OpenAI-LangChain-Pandas-DF-Agent-Query-Streamlit-App/assets/87671757/d80e6c6c-7afa-4c13-9b7c-57f8817b6515)
![image](https://github.com/petermartens98/OpenAI-LangChain-Pandas-DF-Agent-Query-Streamlit-App/assets/87671757/732abffc-7e37-4223-b60b-306daee62631)
