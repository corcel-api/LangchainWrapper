# Bittensor LangChain Wrapper

This project contains a language model wrapper for the BitAPAI endpoint on the Bittensor network. The `LangChainBitAPAIWrapper` class allows for easy interaction with the BitAPAI endpoint, enabling the sending and receiving of messages. The wrapper uses an API key for authentication and supports secure HTTPS connections. 

Example usage involves creating an instance of the `LangChainBitAPAIWrapper` class with your API key, and then calling the `_call` method with a list of message objects. Each message object should have a 'role' and 'content'. The `_call` method returns the response from the BitAPAI endpoint.

Please refer to the codebase for more detailed usage and implementation details.
