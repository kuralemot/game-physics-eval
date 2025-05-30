from lm.lm_response import LMResponse
import utils.logger as logger
import os
import traceback
from lm.lm_base import LMBase
from dotenv import load_dotenv
from openai import OpenAI as openai

class LMStudio(LMBase):
    def __init__(self, model_name):
        self._model_name = model_name
        load_dotenv(dotenv_path='./.env')
        self._client = openai(base_url=os.getenv("LM_STUDIO_SERVER"), api_key="not-needed")
    
    def model_name(self):
        return self._model_name.replace("/","-")
    
    def run_prompt(self, messages: list[str], temperature: int = None) -> LMResponse:
        try:
            load_dotenv(dotenv_path='.\.env')

            if self._output_format is not None:
                response=self.run_format_prompt(messages=messages, temperature=temperature)
            else:
                response=self.run_unformat_prompt(messages=messages, temperature=temperature)

            val=LMResponse()
            val.messages=messages
            val.response=response.choices[0].message.content
            val.input_tokens=response.usage.prompt_tokens
            val.output_tokens=response.usage.completion_tokens
            logger.info(val, silent=True)
            return val
        except Exception as e:
            print(traceback.format_exc())
            logger.error(f"run_prompt {self._model_name} error: {e}")
            return None
    
    def run_unformat_prompt(self, messages: list[str], temperature: int = None):
        if temperature == None:            
            response = self._client.chat.completions.create(
            model="local-model", # this field is currently unused
            messages=messages
            )
        else:
            response = self._client.chat.completions.create(
            model="local-model", # this field is currently unused
            messages=messages,
            temperature=temperature
            )
        return response

    def run_format_prompt(self, messages: list[str], temperature: int = None):
        if temperature == None:            
            response = self._client.beta.chat.completions.parse(
            model="local-model", # this field is currently unused
            messages=messages,
            response_format=self._output_format
            )
        else:
            response = self._client.beta.chat.completions.parse(
            model="local-model", # this field is currently unused
            messages=messages,
            temperature=temperature,
            response_format=self._output_format
            )
        return response
    
    def get_embeddings(self, messages) -> list:
        return None