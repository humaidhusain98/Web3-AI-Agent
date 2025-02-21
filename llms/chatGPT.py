from langchain_openai import ChatOpenAI

# Initialize a ChatOpenAI model
gpt4ominiLLM = ChatOpenAI(
    model="gpt-4o-mini", temperature=0
)

gpt4LLM= ChatOpenAI(
    model="gpt-4", temperature=0
)
