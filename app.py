import groq
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
import requests  # For making API requests
from dotenv import load_dotenv
from typing import List, Optional

# Load environment variables
load_dotenv()

st.set_page_config("Chatbot")
st.title('Langchain Demo with Groq API')

def get_models(api_key: str) -> List[str]:
    """
    Fetches available models from the Groq API.

    Args:
        api_key (str): The user's Groq API key.

    Returns:
        List[str]: A list of model IDs, excluding certain models.
    """
    try:
        client = groq.Client(api_key=api_key)
        models = client.models.list().data
        return [
            model.id for model in models
            if model.id not in ['whisper-large-v3', 'distil-whisper-large-v3-en']
        ]
    except (groq.AuthenticationError, groq.APIConnectionError, 
            groq.APIStatusError, groq.APIError) as e:
        st.error(f"Error: {e.body.get('error', {}).get('message')}")
        return []  # Return an empty list in case of error
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return []

def chatbot(api_key: str, model: str, input_text: str) -> Optional[str]:
    """
    Handles the chatbot response using the Groq API and Langchain.

    Args:
        api_key (str): The user's Groq API key.
        model (str): The selected model for the chatbot.
        input_text (str): The user's input question.

    Returns:
        Optional[str]: The chatbot's response or None in case of an error.
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Please respond to the user's queries."),
        ("user", "Question: {question}")
    ])

    try:
        llm = ChatGroq(model=model, api_key=api_key)
        output_parser = StrOutputParser()
        chain = prompt | llm | output_parser
        response = chain.invoke({'question': input_text})
        return response

    except groq.APIConnectionError as e:
        st.error(f"API Connection Error: {e}")
    except groq.AuthenticationError as e:
        st.error(f"Authentication Error: {e.body['error']['message']}")
    except groq.APIStatusError as e:
        st.error(f"API Status Error: {e}")
    except Exception as e:
        st.error(f"Unknown Error: {e}")
    
    return None

# Sidebar for API key input
st.sidebar.title("Settings")
user_api_key: str = st.sidebar.text_input("Enter your Groq API key:", type="password")

# Step 1: Check if the API key has been provided
if not user_api_key:
    st.warning("Please provide your API key in the sidebar to proceed.")
    st.stop()

# Step 2: Validate the API key format
if user_api_key.startswith("gsk_"):
    st.success("Thanks for providing a valid API key!")
    models: List[str] = get_models(user_api_key)
    
    if models:
        model_choice: str = st.selectbox("Select your model", sorted(models), index=0)
        user_input: str = st.text_input("Enter your question here:")

        if user_input:
            response: Optional[str] = chatbot(user_api_key, model_choice, user_input)
            if response:
                st.write(response)
else:
    st.warning("Please provide a valid API key.")
    st.stop()
