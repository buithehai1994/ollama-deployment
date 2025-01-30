import streamlit as st
import requests

# FastAPI URL
fastapi_url = "http://127.0.0.1:8000/generate"

# Set up the Streamlit app layout
st.title("Ollama Text Generator")
st.write("Enter a prompt to generate text using the Ollama model.")

# Input field for the user to provide a prompt
prompt = st.text_area("Prompt:", height=150)

# Button to generate text when clicked
if st.button("Generate Text"):
    if prompt.strip():
        # Send a GET request to the FastAPI server with the prompt as a query parameter
        try:
            response = requests.get(f"{fastapi_url}?prompt={prompt}")
            response.raise_for_status()  # Check if request was successful
            generated_text = response.json().get("generated_text", "No response")
            st.subheader("Generated Text:")
            st.write(generated_text)
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt to generate text.")
