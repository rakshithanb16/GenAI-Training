import os
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    messages=[{'role': "user", "content": "HELLO CLAUDE"}]
)
for block in response.content:
    if block.type == "text":
        print(block.text)