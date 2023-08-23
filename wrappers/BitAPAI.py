import http
import json
from typing import Any, List, Mapping, Optional

from langchain.llms.base import LLM


class BitAPAI_Wrapper(LLM):
    """Wrapper for the BitAPAI endpoint on the Bittensor network.
    Args:
        api_key: The API key for the BitAPAI endpoint.
    """
    api_key: str = ''

    @property
    def _llm_type(self) -> str:
        return "BitAPAI Wrapper"
    
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"model": 'Bittensor BitAPAI'}
    
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        """Run the LLM on the given prompt and input."""

    async def _acall(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        """Run the LLM on the given prompt and input."""
        raise NotImplementedError("Async generation not implemented for this LLM.")
    
    def __call__(
        self, 
        messages: List[Mapping[str, str]], 
        pool_id: Optional[int] = 0,
        uids: Optional[List[int]] = [], 
        count: Optional[int] = 20,
        return_all: Optional[bool] = False,
        exclude_unavailable: Optional[bool] = True
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
            "pool_id": pool_id,
            "uids": uids,
            "count": count,
            "return_all": return_all,
            "exclude_unavailable": exclude_unavailable
        })

        headers = {
          'Content-Type': 'application/json',
          'X-API-KEY': self.api_key
        }


        try:
            conn = http.client.HTTPSConnection("api.bitapai.io")
            conn.request("POST", "/text", payload, headers)
            res = conn.getresponse()
            if res.status != 200:
                raise http.client.HTTPException(f"HTTP error occurred: {res.status} {res.reason}")
        except Exception as e:
            print(f"An error occurred: {e}")
            return [str(e)]


        data = res.read()
        result = json.loads(data.decode("utf-8"))

        return [choice['message']['content'] for choice in result['choices']] if result['count'] > 0 else ["No response from BitAPAI"]
