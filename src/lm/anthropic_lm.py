import utils.logger as logger
import os
from lm.lm_base import LMBase
from dotenv import load_dotenv
from anthropic import Anthropic

from lm.lm_response import LMResponse

class AnthropicLM(LMBase):
    def __init__(self, model_name):
        self._model_name = model_name
        load_dotenv(dotenv_path='./.env')
        self._client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    def model_name(self):
        return self._model_name.replace("/","-")
    
    def run_prompt(self, messages: list[str], temperature: int = None) -> LMResponse:
        try:
            if temperature == None:            
                response = self._client.messages.create(
                model=self._model_name,
                max_tokens=1024,
                messages=messages
                )
            else:
                response = self._client.messages.create(
                model=self._model_name,
                max_tokens=1024,
                temperature=temperature,
                messages=messages
                )
            
            val=LMResponse()
            val.messages=messages
            val.response=response.content[0].text
            val.input_tokens=response.usage.input_tokens
            val.output_tokens=response.usage.output_tokens
            logger.info(val, silent=True)
            return val
        except Exception as e:
            logger.error(f"run_prompt {self._model_name} error: {e}")
            return None
    
    def get_embeddings(self, messages) -> list:
        return None