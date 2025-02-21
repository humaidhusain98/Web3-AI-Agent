
class APIResponse:
    def __init__(self,httpCode,msg,data):
        self.httpCode = httpCode
        self.msg = msg
        self.data = data