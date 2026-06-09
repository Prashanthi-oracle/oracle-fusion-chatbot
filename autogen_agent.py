import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelInfo
import os
from dotenv import load_dotenv

load_dotenv(r'C:\Users\HP\AIAgent\.env')
api_key = os.getenv('GROQ_API_KEY')

model_client = OpenAIChatCompletionClient(
    model='llama-3.3-70b-versatile',
    api_key=api_key,
    base_url='https://api.groq.com/openai/v1',
    model_info=ModelInfo(
        vision=False,
        function_calling=True,
        json_output=True,
        family='unknown',
        structured_output=False
    )
)

agent = AssistantAgent(
    name='OracleFusionBot',
    model_client=model_client,
    system_message='You are an Oracle Fusion expert. Help with Procurement, AP, AR, GL, SCM modules.'
)

async def main():
    print('=== Oracle Fusion Chatbot ===')
    print('Type your question and press Enter')
    print('Type exit to quit')
    print('============================')
    
    while True:
        question = input('\nYou: ')
        if question.lower() == 'exit':
            print('Goodbye!')
            break
        await Console(agent.run_stream(task=question))

asyncio.run(main())
