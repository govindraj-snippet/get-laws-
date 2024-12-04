import streamlit as st
import json

# Load the JSON file
with open('laws.json', 'r') as file:
    laws_data = json.load(file)

# Streamlit Chat-like App
st.title("Law Viewer Chat")
st.write("Chat with the Law Viewer: Enter a law number to get its details.")

# Chat messages stored in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# User input
if user_input := st.chat_input("Enter a law number (e.g., '123')"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Check if the input is a valid law number
    if user_input in laws_data:
        response = f"Law #{user_input}: {laws_data[user_input]}"
        st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        response = "Law not found. Please enter a valid number."
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Display assistant message
    st.chat_message("assistant").write(response)