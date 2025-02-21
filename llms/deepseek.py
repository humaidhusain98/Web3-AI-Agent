from langchain_ollama.llms import OllamaLLM

deepseek_r1_llm = OllamaLLM(model="deepseek-r1:latest",temperature=0)
deepseek_coder_llm = OllamaLLM(model="deepseek-coder:latest",temperature=0)
deepseek_7b_llm = OllamaLLM(model="deepseek-llm:7b",temperature=0)