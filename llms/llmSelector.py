from ..llms.chatGPT import gpt4ominiLLM,gpt4LLM
from ..llms.deepseek import deepseek_r1_llm,deepseek_7b_llm,deepseek_coder_llm
from ..llms.gemini import gemini_one_point_five_flash_llm,gemini_one_point_five_pro_llm,gemini_two_flash_llm,gemini_two_flash_lite_preview
from ..llms.llama import llama2_stable_beluga_13b_llm,llama3_llm, llama3_point_3_llm

def getLLMFromModelName(modelname:str):
    if(modelname=="gpt-4o-mini"):
        return gpt4ominiLLM
    elif (modelname=="gpt-4"):
        return gpt4LLM
    elif (modelname=="deepseek-r1"):
        return deepseek_r1_llm
    elif (modelname=="deepseek-llm:7b"):
        return deepseek_7b_llm
    elif (modelname=="deepseek-coder"):
        return deepseek_coder_llm
    elif (modelname=="gemini-1.5-flash"):
        return gemini_one_point_five_flash_llm
    elif (modelname=="gemini-1.5-pro"):
        return gemini_one_point_five_pro_llm
    elif (modelname=="gemini-2.0-flash"):
        return gemini_two_flash_llm
    elif (modelname=="gemini-2.0-flash-lite"):
        return gemini_two_flash_lite_preview
    elif (modelname=="deepseek-llm:7b"):
        return deepseek_7b_llm
    elif (modelname=="llama2-stable:13b"):
        return llama2_stable_beluga_13b_llm
    elif (modelname=="llama3"):
        return llama3_llm
    elif (modelname=="llama3.3"):
        return llama3_point_3_llm
    else:
        return None
    
    