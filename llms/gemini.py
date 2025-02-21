import os
from langchain_google_genai import ChatGoogleGenerativeAI

gemini_api_key = os.getenv('GEMINI_API_KEY')
gemini_one_point_five_pro_llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",api_key=gemini_api_key)
gemini_one_point_five_flash_llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",api_key=gemini_api_key)
gemini_two_flash_llm =   ChatGoogleGenerativeAI(model="gemini-2.0-flash",api_key=gemini_api_key)
gemini_two_flash_lite_preview =  ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite-preview-02-05",api_key=gemini_api_key)