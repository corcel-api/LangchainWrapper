# Bittensor LangChain Wrapper

This project contains a language model wrapper for the various APIs (including, BitAPAI) on the Bittensor network. The `BitAPAI_Wrapper` class allows for easy interaction with the BitAPAI endpoint, enabling the sending and receiving of messages. The wrapper uses an API key for authentication and supports secure HTTPS connections.

## Supported parameters for BitAPAI interaction
- `uids`: List[int]
    A list of unique identifiers (UIDs) to query. If left empty (default is []), BitAPAI will query the top-incentivized miners on the network.
- `count`: int
    The number of UIDs to query. Default value is 20.
- `return_all`: bool
    A boolean flag indicating whether to return all responses from the BitAPAI endpoint. If set to False (default), choose one randomly among the top `count` responses.
- `exclude_unavailable`: bool
    A boolean flag indicating whether to exclude unavailable miners from the query. If set to True (default), any miners that are currently unavailable will be excluded from the query.

## Code examples

```bash
bitapai = BitAPAI_Wrapper()
bitapai.api_key = '<YOUR-BITAPAI-API-KEY>'

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
```

- Default settings (get one of responses from top-20 miners)
```bash
# Call the BitAPAI endpoint
response = bitapai(messages)
# Print the response
print('\n'.join(response))
```

- Specify `return_all` (get all responses from top-20 miners)
```bash
# Call the BitAPAI endpoint
response = bitapai(messages, return_all=True)
# Print the response
print('\n'.join(response))
```

- Specify `exclude_unavailable` and `count` (get all responses from top-50 miners, excluding unavaiable miners)
```bash
# Call the BitAPAI endpoint
response = bitapai(messages, return_all=True, exclude_unavailable=True, count=50)
# Print the response
print('\n'.join(response))
```

Please refer to the codebase for more detailed usage and implementation details.
