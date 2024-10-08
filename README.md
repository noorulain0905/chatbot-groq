# Langchain Demo with Groq API

## Overview

This project demonstrates the integration of the Groq API with the Langchain framework using a chatbot interface. The chatbot allows users to interact with Groq's language models and get responses to their queries in real-time. The app is built using Streamlit, providing an interactive web interface.

### Key Features

- **Groq API Integration**: Utilizes Groq's powerful models for generating responses.
- **Langchain Support**: Incorporates Langchain's prompt templates for natural language understanding.
- **Interactive Interface**: Built with Streamlit for real-time interaction and ease of use.
- **Customizable Models**: Allows users to select different models based on their needs.
- **API Key Security**: Secure API key input and validation via Streamlit's sidebar.

## Installation

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.8+
- `pip` (Python package installer)

### Step-by-Step Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/noorulain0905/chatbot-groq.git
    cd chatbot-groq
    ```

2. **Create a virtual environment (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add your Groq API key:
     ```bash
     GROQ_API_KEY=gsk_your_api_key_here
     ```

5. **Run the application**:
    ```bash
    streamlit run app.py
    ```

6. **Access the app**:
    - Open the provided URL (usually `http://localhost:8501`) in your web browser.

## Usage

1. **Enter your Groq API key** in the sidebar.
2. **Select a language model** from the dropdown menu.
3. **Type your query** into the input box and press enter.
4. The chatbot will respond to your query using the selected model.

## Error Handling

- If you enter an invalid API key or experience connection issues, the app will notify you with an error message.
- Ensure your API key is valid and that you have an active internet connection to communicate with the Groq API.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
