import streamlit as st
import requests

st.title("AI Chatbot")

# store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for role,msg in st.session_state.messages:
    with st.chat_message(role):
        st.write(msg)

# input box
prompt = st.chat_input("Ask something...")

if prompt:
    # save user message
    st.session_state.messages.append(("user", prompt))

    with st.chat_message("user"):
        st.write(prompt)

    # call Ollama
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    ai_msg = response.json()["response"]

    # save AI message
    st.session_state.messages.append(("assistant", ai_msg))


    with st.chat_message("assistant"):
        st.write(ai_msg)