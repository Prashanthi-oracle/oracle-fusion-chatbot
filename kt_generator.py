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
    name='KTGenerator',
    model_client=model_client,
    system_message='You are an expert Oracle Functional Consultant who creates professional Knowledge Transfer documents. Generate detailed, structured KT documents with sections like Overview, Business Process, Configuration, Key Points, and Risks.'
)

async def main():
    print('=== KT Document Generator ===')
    print()
    
    module = input('Enter Module Name (e.g. Supplier 360): ')
    from_system = input('From System (e.g. Oracle EBS): ')
    to_system = input('To System (e.g. Oracle Fusion): ')
    audience = input('Audience (e.g. Business Team): ')
    details = input('Any specific details to include: ')
    
    task = f'''Generate a professional KT document with the following details:
    Module: {module}
    From System: {from_system}
    To System: {to_system}
    Audience: {audience}
    Additional Details: {details}
    
    Include these sections:
    1. Overview
    2. Business Process
    3. Key Changes
    4. Configuration Details
    5. Risks and Mitigation
    6. Next Steps
    '''
    
    print('\nGenerating KT Document...\n')
    await Console(agent.run_stream(task=task))

asyncio.run(main())
