from lm.lm_response import LMResponse
import utils.logger as logger
import os
import ollama
import traceback
from lm.lm_base import LMBase
from dotenv import load_dotenv
from ollama import Client
from pydantic import BaseModel

class OllamaLM(LMBase):
    def __init__(self, model_name):
        self._model_name = model_name
        load_dotenv(dotenv_path='./.env')
        self._client = Client(host='http://localhost:11434',  headers={'x-some-header': 'some-value'})
    
    def model_name(self):
        return self._model_name.replace("/","-")
    
    def set_output_format(self, format):
        self._output_format=format.model_json_schema()
    
    def run_prompt(self, messages: list[str], temperature: int = None) -> LMResponse:
        try:
            load_dotenv(dotenv_path='.\.env')
            if temperature == None:            
                response = self._client.chat(
                model=self._model_name,
                messages=messages,
                format=self._output_format
                )
            else:
                response = self._client.chat(
                model=self._model_name,
                messages=messages,
                format=self._output_format,
                options={'temperature': temperature}
                )

                # format=Answer.model_json_schema()
            val=LMResponse()
            val.messages=messages
            val.response=response.message.content
            val.input_tokens=0
            val.output_tokens=0
            logger.info(val, silent=True)
            return val
        except Exception as e:
            print(traceback.format_exc())
            logger.error(f"run_prompt {self._model_name} error: {e}")
            return None
    
    def get_embeddings(self, messages) -> list:
        return None
    
    def build_prompt(self, prompts:list[str] = None, img_paths:list[str] = None):
        if img_paths is not None and len(img_paths)>0:
            messages=[{"role":"user",
                       "content":prompts[0],
                       "images":img_paths}]
        else:
            messages=[{"role":"user",
                       "content":prompts[0]}]
        return messages

    # def build_prompt(prompts:list[str] = None, img_paths:list[str] = None):
    #     if img_paths is not None and len(img_paths)>0:
    #         messages=[{"role":"user",
    #                    "content":prompts[0],
    #                    "images":img_paths}]
    #     else:
    #         messages=[{"role":"user",
    #                    "content":prompts[0]}]
    #     return messages