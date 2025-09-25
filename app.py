import os
import streamlit as st
from google import genai

# Initialize client with API key
client = genai.Client(api_key="AIzaSyCyl-nq1mrG_C8T85N58bKyrpXURNYuipw")

# Model to use
MODEL_NAME = "gemini-2.5-flash"

# Streamlit page config
st.set_page_config(page_title="Gemini Chat", page_icon="🤖")
st.title("💬 Chat with Gemini (Google API)")

# Store conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input box
if prompt := st.chat_input("Type your message..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gemini response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
            )
            reply = response.text
            st.markdown(reply)

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": reply})
