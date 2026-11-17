import streamlit as st
from openrouter import OpenRouter

st.title("OPENROUTER CLOUD CHATBOT")

with st.sidebar:
    API_KEY = st.text_input("Enter the API KEY ")

user_input = st.text_input("Hello, What can I do for you!")

if st.button("Submit"):
    with OpenRouter(api_key=API_KEY) as client:
        response = client.responses.send(
            model = "nvidia/nemotron-3-ultra-550b-a55b:free",
            input = user_input
        )
        if response.status != "completed":
            message = response.error.message if response.error else f"Response ended as {response.status}"
            raise RuntimeError(message)

        message = next(item for item in reversed(response.output) if item.type == "message")
        st.markdown(next(part.text for part in message.content if part.type == "output_text"))


