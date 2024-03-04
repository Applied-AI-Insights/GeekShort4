import os
from groq import Groq

# Set Groq api_key
client = Groq(
    api_key=""
)

chat_completion = client.chat.completions.create(
    messages=[
        # Set an optional system message. This sets the behavior of the
        # assistant and can be used to provide specific instructions for
        # how it should behave throughout the conversation.
        {
            "role": "system",
            "content": "you are a helpful assistant."
        },
        # Set a user message for the assistant to respond to.
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs",
        }
    ],
    # The language model which will generate the completion.
    model="mixtral-8x7b-32768",
)

response =chat_completion.choices[0].message.content

print(response)
print("===== State =====")
print("prompt_tokens:",chat_completion.usage.prompt_tokens)
print("completion_tokens:",chat_completion.usage.completion_tokens)
print("total_tokens:",chat_completion.usage.total_tokens)
print("prompt_time:",chat_completion.usage.prompt_time)
print("completion_time:",chat_completion.usage.completion_time)
print("total_time:",chat_completion.usage.total_time)
print("total_token per second:", chat_completion.usage.total_tokens / chat_completion.usage.total_time , "s")






