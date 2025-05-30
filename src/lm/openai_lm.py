import utils.logger as logger
import os
import time
import openai
import random
import utils.file_manager as fm
from lm.lm_base import LMBase
from lm.lm_embeddings import LMEmbeddings
from dotenv import load_dotenv
from openai import OpenAI
from lm.lm_response import LMResponse
import traceback

class OpenAILM(LMBase):
    def __init__(self, model_name="gpt-4o-mini-2024-07-18"):
        self._model_name = model_name
        load_dotenv(dotenv_path='./.env')
        self._client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self._emb_cache_dir = os.getenv("EMBEDDING_CACHE")
        if not os.path.exists(self._emb_cache_dir):
            os.makedirs(self._emb_cache_dir)
    
    def model_name(self):
        return self._model_name.replace("/","-")
    
    def run_prompt(self, messages: list[str], temperature: int = None) -> LMResponse:
        try:
            time.sleep(random.uniform(1.0,3.0))

            if self._output_format is not None:
                response=self.run_format_prompt(messages=messages, temperature=temperature)
            else:
                response=self.run_unformat_prompt(messages=messages, temperature=temperature)
            
            val=LMResponse()
            val.messages=messages
            # val.response=response.choices[0].message.parsed if self._output_format is not None else response.choices[0].message.content
            val.response=response.choices[0].message.parsed
            val.input_tokens=response.usage.prompt_tokens
            val.output_tokens=response.usage.completion_tokens
            logger.info(val, silent=True)
            return val
        except openai.APIConnectionError as e:
            logger.error(f"Failed to connect to OpenAI API: {e}")
            return None
        except openai.RateLimitError as e:
            logger.error(f"OpenAI API request exceeded rate limit: {e}")
            time.sleep(7)
            return self.run_prompt(messages=messages, temperature=temperature)
        except openai.APIError as e:
            logger.error(f"OpenAI API returned an API Error: {e}")
            return None
        except Exception as e:
            logger.error(f"run_prompt {self._model_name} error: {e}")
            return None
        
    def run_unformat_prompt(self, messages: list[str], temperature: int = None):
        if temperature == None:            
            response = self._client.chat.completions.create(
            model=self._model_name,
            messages=messages
            )
        else:
            response = self._client.chat.completions.create(
            model=self._model_name,
            messages=messages,
            temperature=temperature
            )
        return response

    def run_format_prompt(self, messages: list[str], temperature: int = None):
        if temperature == None:            
            response = self._client.beta.chat.completions.parse(
            model=self._model_name,
            messages=messages,
            response_format=self._output_format
            )
        else:
            response = self._client.beta.chat.completions.parse(
            model=self._model_name,
            messages=messages,
            temperature=temperature,
            response_format=self._output_format
            )
        return response
        
    def split_array(self, arr, max_size=50):
        return [arr[i:i + max_size] for i in range(0, len(arr), max_size)]

    def get_embeddings(self, messages, model_name:str="text-embedding-3-small") -> list:
        try:
            emb_cache:list[LMEmbeddings]=[]
            emb_file_path=os.path.join(self._emb_cache_dir, f'{model_name}.json')
            if os.path.exists(emb_file_path):
                emb_json=fm.read_json(emb_file_path)
                emb_cache=[LMEmbeddings(jstr=jstr) for jstr in emb_json]

            uncached_msgs=[]
            for msg in messages:
                found=next((emb for emb in emb_cache if emb.message==msg), None)
                if found is None:
                    uncached_msgs.append(msg)            
            
            if len(uncached_msgs)>0:
                uncached_msgs=list(set(uncached_msgs)) # remove duplicate
                msg_chunks=self.split_array(uncached_msgs, max_size=40)
                for chunk in msg_chunks:
                    time.sleep(random.uniform(1.0,3.0))
                    response=self._client.embeddings.create(input=chunk, model=model_name)
                    for i, data in enumerate(response.data):
                        embeddings=LMEmbeddings()
                        embeddings.message=chunk[i]
                        embeddings.embeddings=data.embedding
                        embeddings.input_tokens=response.usage.prompt_tokens
                        embeddings.output_tokens=response.usage.total_tokens
                        emb_cache.append(embeddings)
                    fm.write_json(path=emb_file_path, data=emb_cache, compressed=True)
            embeddings_list=[emb for emb in emb_cache if emb.message in messages]
            logger.info("get_embeddings: SUCCESS", silent=True)
            return embeddings_list
        except openai.APIConnectionError as e:
            logger.error(f"Failed to connect to OpenAI API: {e}")
            return None
        except openai.RateLimitError as e:
            logger.error(f"OpenAI API request exceeded rate limit: {e}")
            time.sleep(7)
            return self.get_embeddings(messages=messages, model_name=model_name)
        except openai.APIError as e:
            logger.error(f"OpenAI API returned an API Error: {e}")
            return None
        except Exception as e:
            logger.error(f"run_prompt {self._model_name} error: {e}")
            print(traceback.format_exc())
            return None