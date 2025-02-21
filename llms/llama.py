from langchain_ollama.llms import OllamaLLM

llama2_stable_beluga_13b_llm = OllamaLLM(model="stable-beluga:13b",temperature=0)
llama3_llm = OllamaLLM(model="llama3:latest",temperature=0)
llama3_point_3_llm = OllamaLLM(model="llama3.3:latest",temperature=0)