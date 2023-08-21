import json

from wrappers.BitAPAI import LangChainBitAPAIWrapper


# Initialize the BitAPAI wrapper
bitapai = LangChainBitAPAIWrapper()

# Define the messages
messages = [
    {
      "role": "system",
      "content": "You are an AI assistant"
    },
    {
      "role": "user",
      "content": "What is the meaning of life?"
    },
    {
      "role": "assistant",
      "content": "42"
    },
    {
      "role": "user",
      "content": "What is the question?"
    }
]

# Call the BitAPAI endpoint
response = bitapai._call(messages)

# Print the response
print(bitapai)
print(response)
