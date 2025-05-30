
class LMResponse:
    def __init__(self) -> None:
        self._messages=""
        self._response=""
        self._input_tokens=0
        self._output_tokens=0
        pass

    @property
    def messages(self):
        return self._messages
    
    @messages.setter
    def messages(self, value):
        self._messages=value

    @property
    def response(self):
        return self._response
    
    @response.setter
    def response(self, value):
        self._response=value
    
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
        return {"messages":self._messages,
                "response":self._response,
                "input_tokens":self._input_tokens ,
                "output_tokens":self._output_tokens}
    
    def __str__(self) -> str:
        return str(self.dict())
    
    def __repr__(self) -> str:
        return str(self.dict())