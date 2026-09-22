import streamlit as st
from openai import OpenAI

st.title("🤖 Deepika's AI Agent")
st.write("Hello! Ask me anything.")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

question = st.text_input("Enter your question:")

if st.button("Ask AI"):
if question:
with st.spinner("Thinking..."):
response = client.responses.create(
model="gpt-5.6-luna",
instructions="You are a friendly and helpful AI assistant created by Deepika Pandey.",
input=question
)

st.success(response.output_text)
else:
st.warning("Please enter a question.")
