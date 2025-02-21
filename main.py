from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI,Response,status
from .agents.reactAgent import get_agent_executor
from pydantic import BaseModel
from .models.response import APIResponse


class Body(BaseModel):
    query: str
    llmModel:str

app = FastAPI()

@app.post("/ask")
async def askQuestion(body:Body,response:Response):
    try:
        agent_executor = get_agent_executor(body.llmModel)
        if not agent_executor:
            apiResponse = APIResponse(status.HTTP_500_INTERNAL_SERVER_ERROR,"Response recieved from get_agent_executor is None",{})
            response.status_code = apiResponse.httpCode
            return apiResponse
        else:
            agentResponse = agent_executor.invoke({"input":body.query})
            apiResponse = APIResponse(status.HTTP_200_OK,"Successfully Generated Response",agentResponse)
            return apiResponse
    except:
        apiResponse = APIResponse(status.HTTP_500_INTERNAL_SERVER_ERROR,"Unexpected Error occured",{})
        response.status_code = apiResponse.httpCode
        return apiResponse
    


@app.get("/")
async def root():
    return {"message": "server started on port 8000"}