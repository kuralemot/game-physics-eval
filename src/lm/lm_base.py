from abc import ABC, abstractmethod
from lm.lm_response import LMResponse
from lm.lm_embeddings import LMEmbeddings
from utils import file_manager as fm
import base64

class LMBase(ABC):
    def __init__(self, model_name) -> None:
        super().__init__()

    @abstractmethod
    def model_name(self):
        return None

    @abstractmethod
    def run_prompt(self, messages:list[str], temperature:int = None) -> LMResponse:
        print(f"run prompt using: {__name__}")
        return None
    
    def set_output_format(self, format):
        self._output_format=format
        pass
    
    @abstractmethod
    def get_embeddings(self, messages:list)->list:
        return None    
    
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    
    def build_prompt(self, prompts:list[str] = None, img_paths:list[str] = None):
        content=[]
        if prompts is not None and len(prompts)>0:
            content.extend([{"type":"text", "text":p} for p in prompts])
        if img_paths is not None and len(img_paths)>0:
            encoded_imgs=[LMBase.encode_image(image_path=p) for p in img_paths]
            urls=[f"data:image/jpeg;base64,{img}" for img in encoded_imgs]
            content.extend([{"type":"image_url", "image_url":{"url":u}} for u in urls])

        messages=[{"role":"user",
                   "content":content}]
        return messages