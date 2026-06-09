import streamlit as st
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelInfo

api_key = st.secrets["GROQ_API_KEY"]

st.title("Oracle Fusion AI Chatbot")
st.subheader("Ask me anything about Oracle Fusion!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask your Oracle Fusion question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    model_client = OpenAIChatCompletionClient(
        model="llama-3.3-70b-versatile",
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
        model_info=ModelInfo(
            vision=False,
            function_calling=True,
            json_output=True,
            family="unknown",
            structured_output=False
        )
    )
    agent = AssistantAgent(
        name="OracleFusionBot",
        model_client=model_client,
        system_message="You are an Oracle Fusion expert. Help with Procurement, AP, AR, GL, SCM modules."
    )
    async def get_response(question):
        response = await agent.run(task=question)
        return response.messages[-1].content
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = asyncio.run(get_response(prompt))
            st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})