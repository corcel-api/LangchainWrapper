from wrappers.BitAPAI import BitAPAI_Wrapper


# Initialize the BitAPAI wrapper
bitapai = BitAPAI_Wrapper()
bitapai.api_key = '<YOUR-BITAPAI-API-KEY>'


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
response = bitapai(messages, return_all=True, exclude_unavailable=True, count=50)

# Print the response
print('\n'.join(response))