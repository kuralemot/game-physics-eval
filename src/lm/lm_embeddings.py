class LMEmbeddings():
    def __init__(self, jstr:str=None) -> None:
        try:
            self._message=jstr['message']
            self._embeddings=jstr['embeddings']
            self._input_tokens=jstr['input_tokens']
            self._output_tokens=jstr['output_tokens']
        except:
            self._message=""
            self._embeddings=[]
            self._input_tokens=0
            self._output_tokens=0
    
    @property
    def message(self):
        return self._message
    
    @message.setter
    def message(self, value):
        self._message=value

    @property
    def embeddings(self):
        return self._embeddings
    
    @embeddings.setter
    def embeddings(self, value):
        self._embeddings=value

    @property
    def input_tokens(self):
        return self._input_tokens
    
    @input_tokens.setter
    def input_tokens(self, value):
        self._input_tokens=value
    
    @property
    def output_tokens(self):
        return self._output_tokens
    
    @output_tokens.setter
    def output_tokens(self, value):
        self._output_tokens=value
    
    def dict(self):
        return {"message":self._message,
                "embeddings":self._embeddings,
                "input_tokens":self._input_tokens,
                "output_tokens":self._output_tokens}
    
    def __repr__(self) -> str:
        return str(self.dict())
    
    def __str__(self) -> str:
        return str(self.dict())