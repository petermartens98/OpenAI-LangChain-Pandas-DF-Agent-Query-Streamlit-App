# OpenAI LangChain Pandas DF Agent Query Streamlit App



### Description
Python Streamlit web application designed to provide a user-friendly interface for querying and communicated with data from a CSV file using the OpenAI language model. 

The script begins by importing the necessary libraries, including os for operating system interactions, streamlit for building web applications, pandas for data manipulation, dotenv for loading environment variables, and langchain to for interacting with the openAI API and creating a Pandas DF agent. 

The main functionality of the script is contained within the main() function. It starts by loading the OpenAI API key from the environment variable and checking its existence. Then, it sets up the Streamlit application by displaying a title and description. The user is prompted to upload a CSV file, which is read using pandas and displayed as a preview. 

A pandas dataframe agent is created using the OpenAI language model, and the user is prompted to enter a query. Upon clicking the "Execute" button, the query is sent to the agent, and the answer as well as conversation is displayed on the application interface. Overall, this script provides a convenient way for users to interact with their CSV data and obtain answers based on their queries using the OpenAI language model.

### App V3 Improvements
1. Implemented .env variable for OpenAI API key.
2. Improved prompt for pandas df agent, taking into account prvious chats.
3. Improved CSS
4. .XLSX File Support
5. LLM Temperature Slider

### App V3 Screenshot
![image](https://github.com/petermartens98/OpenAI-LangChain-Pandas-DF-Agent-Query-Streamlit-App/assets/87671757/51e20a6f-bc16-4cdb-bd9e-75c6b9f0bd42)

### App V2 Improvemnts
Added conversational memory and the abiliy for a continuous chat istead of a single Q&A

### Example Screenshots App V2
![image](https://github.com/petermartens98/OpenAI-LangChain-Pandas-DF-Agent-Query-Streamlit-App/assets/87671757/2ca0d05b-3eff-48fc-8426-237634bc9661)

### Example Screenshots App V1
![image](https://github.com/petermartens98/OpenAI-LangChain-Pandas-DF-Agent-Query-Streamlit-App/assets/87671757/d80e6c6c-7afa-4c13-9b7c-57f8817b6515)
