import os
import streamlit as st
import openai

# Set the OpenAI API key directly
OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

# Streamlit page configuration
st.set_page_config(page_title="GPT-4o Chat", page_icon="💬", layout="centered")

# Initialize chat session in Streamlit if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Streamlit page title
st.title("🤖 GPT-4o - ChatBot")

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field for user's message
user_prompt = st.chat_input("Ask GPT-4o...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Use OpenAI's ChatCompletion.create for GPT-3.5 or GPT-4
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Change this to "gpt-4" if using GPT-4
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            *st.session_state.chat_history,
        ],
    )

    # Extract assistant's response
    assistant_response = response["choices"][0]["message"]["content"]
    st.session_state.chat_history.append(
        {"role": "assistant", "content": assistant_response}
    )

    # Display assistant's response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
