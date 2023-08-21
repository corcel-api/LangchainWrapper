import http
import json
from typing import Any, List, Mapping, Optional

from langchain.llms.base import LLM


class LangChainBitAPAIWrapper(LLM):
    """Wrapper for the BitAPAI endpoint on the Bittensor network.
    Args:
        api_key: The API key for the BitAPAI endpoint.
    """
    api_key: str = '<YOUR-BITAPAI-API-KEY>'

    @property
    def _llm_type(self) -> str:
        return "BitAPAI"
    
    def _call(
        self,
        messages: List[Mapping[str, str]]
    ) -> str:
        
        """Call out to new BitAPAI endpoint on Bittensor network.
        
        Args:
            messages: List of message objects. Each message has a 'role' and 'content'.
        Returns:
            The string returned by BitAPAI.
        Example:
            .. code-block:: python
                conn.request("POST", "/text", payload, headers)
                res = conn.getresponse()
        """
            
        payload = json.dumps({
          "messages": messages,
        })

        headers = {
          'Content-Type': 'application/json',
          'X-API-KEY': self.api_key
        }
        
        conn = http.client.HTTPSConnection("api.bitapai.io")
        conn.request("POST", "/text", payload, headers)
        res = conn.getresponse()
        data = res.read()
        result = json.loads(data.decode("utf-8"))
        return result['messages'][0]['content'] if result['count'] > 0 else "No response from BitAPAI"
    
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"model": 'Bittensor BitAPAI'}
