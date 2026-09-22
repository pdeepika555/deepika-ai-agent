import streamlit as st
from openai import OpenAI

st.title("🤖 Deepika's AI Agent")
st.write("Hello! Ask me anything.")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
question = st.text_input("Enter your question:")

answer = client.responses.create(model="gpt-5.6-luna", instructions="You are a friendly and helpful AI assistant created by Deepika Pandey.", input=question).output_text if st.button("Ask AI") and question else ""

st.success(answer) if answer else None
