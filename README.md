# Web3-AI-Agent
Web3-AI-Agent is an intelligent AI-driven agent that queries real-time blockchain data using predefined tools. It follows the Reason + Action (ReAct) model, allowing it to analyze user queries, determine the right tool, fetch data, validate accuracy, and iterate until it produces a precise response.

Built on FastAPI, it supports multiple LLMs (Large Language Models) and leverages web3.py for seamless blockchain interactions. The agent is designed to integrate with local LLMs via Ollama and API-based LLMs like ChatGPT and Gemini for flexible AI-powered blockchain data retrieval.

## 🛠 Key Features
### 🔹 Multi-LLM Support
Web3-AI-Agent can work with multiple LLMs, both open-source and API-based:
- Locally Hosted (via Ollama): DeepSeek, Llama models 
- API-based (via API Keys): ChatGPT, Google Gemini models

Supported Models:\
&nbsp; ✅ gpt-4\
&nbsp; ✅ gpt-4o-mini\
&nbsp; ✅ deepseek-r1:latest\
&nbsp; ✅ deepseek-coder:latest\
&nbsp; ✅ deepseek-llm:7b\
&nbsp; ✅ gemini-1.5-pro\
&nbsp; ✅ gemini-1.5-flash\
&nbsp; ✅ gemini-2.0-flash\
&nbsp; ✅ gemini-2.0-flash-lite\
&nbsp; ✅ llama2-stable:13b\
&nbsp; ✅ llama3:latest\
&nbsp; ✅ llama3.3:latest

### 🤖 AI-Powered ReAct Agent
- Works on the Reason + Action (ReAct) model to understand, fetch, validate, and iterate on blockchain data queries.
- Dynamically selects tools based on the query to retrieve real-time information.
- Ensures high accuracy by cross-verifying responses before delivering the final output.

### 🔗 Real-Time Blockchain Querying
- Uses web3.py to fetch live blockchain data via HTTP providers.
- Supports multiple blockchain networks to retrieve:
	- Current block height
   	- Wallet balances

### 🌍 Supported Blockchain Networks
The agent can fetch real-time data from the following EVM-compatible networks: \
&nbsp; ✅ Ethereum Mainnet \
&nbsp; ✅ Polygon Mainnet \
&nbsp; ✅ Arbitrum Mainnet \
&nbsp; ✅ zkSync Mainnet \
&nbsp; ✅ Optimism Mainnet \
&nbsp; ✅ Fantom Opera Mainnet \
&nbsp; ✅ Mantle Mainnet \
&nbsp; ✅ Base Mainnet 

## 🔨 Built-in Tools
LLMs are trained on past data and do not have real-time awareness. To overcome this, Web3-AI-Agent is equipped with specialized tools that allow it to fetch live data from the blockchain and the internet.
### 🛠 Available Tools:
| Tool Name | Description |
| :--- | :--- |
| Get Current Time Tool | Fetches the current time, as LLMs do not inherently have real-time awareness.|
| Search Wikipedia Tool | Retrieves the latest Wikipedia information on a given topic. Returns a two-line summary of the requested subject.|
| Get Current Block Tool | Fetches the latest block number of a specified blockchain. Supported networks: Ethereum, Polygon, Arbitrum, zkSync, Optimism, Fantom, Mantle, Base.|
| Wallet Balance Tool | Retrieves the native token balance of a wallet address on a specified blockchain. Defaults to Ethereum if no network is provided.|

## ⚡ How It Works
1. `Query Processing:`
	- The agent receives a query related to blockchain data.
	- It analyzes the query using an LLM.
2. `Tool Selection:`
	- The agent determines which tool is needed for data retrieval.
	- Executes the tool to fetch real-time blockchain data.
3. `Validation & Iteration:`
   	- It verifies the retrieved data.
   	- If the response is inaccurate or incomplete, the agent repeats the process until it gets a reliable answer.
4. `Final Response:`
   	- The agent returns the final accurate answer to the user.

---



## Installation Instructions

### 1. Clone the Repository
```bash
git clone git@github.com:humaidhusain98/Web3-AI-Agent.git
cd Web3-AI-Agent
```

### 2. Create a Virtual Environment
It's best practice to create a virtual environment for your Python projects:
```bash
python3 -m venv env
# Activate the virtual environment
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
Install the required Python packages using pip and the requirements.txt
```bash
pip install -r requirements.txt
```

### 4.Set Up Environment Variables
Create a .env file in the root directory and add the details given in the .env.example file and fill the details. 
<br />
1. OpenAI API Key: Go to https://platform.openai.com/ and generate an API key
2. Gemini API Key: Go to https://aistudio.google.com/app/apikey and generate an API key
3. Blockchain Providers : You can fetch http blockchain providers from anywhere and fill the details. You can even go to Alchemy and fetch all the http providers for different networks
```env
OPENAI_API_KEY=
GEMINI_API_KEY=

#PROVIDERS OF DIFFERENT BLOCKCHAIN FETCHED FROM ALCHEMY
PROVIDER_ETH_MAINNET_URL=
PROVIDER_POLYGON_POS_MAINNET_URL=
PROVIDER_POLYGON_zKEVM_MAINNET_URL=
PROVIDER_ARBITRUM_MAINNET_URL=
PROVIDER_ARBITRUM_NOVA_MAINNET_URL=
PROVIDER_ZKSYNC_MAINNET_URL=
PROVIDER_OPTIMISM_MAINNET_URL=
PROVIDER_FANTOM_OPERA_MAINNET_URL=
PROVIDER_MANTLE_MAINNET_URL=
PROVIDER_BASE_MAINNET_URL=
```
### Running Locally with Ollama
If using locally hosted LLMs like deepseek and llama models, install Ollama and ensure the required models are available:
```bash
ollama pull deepseek-llm:7b
ollama pull deepseek-coder:latest
ollama pull deepseek-r1:latest
ollama pull llama3:latest
ollama pull llama3.3:latest
ollama pull stable-beluga:13b
```

## Start Instructions
### 1. Run the FastAPI Development Server
Use the following command in root folder terminal to run the development server
```bash
fastapi dev main.py
```

### 2. Access the API
Once the server is running, the API will be available at:
```arduino
http://127.0.0.1:8000
```

### 3. Explore the Documentation
FastAPI automatically generates interactive API docs:
- Swagger UI: http://127.0.0.1:8000/docs

### 4. Run the Production Server
Use the following command in root folder terminal to run the production server
```bash
fastapi run main.py
```

## 🚀 Usage

### 1. Server Check API

This api is used to check if the server is running correctly.

**HTTP Method Type** : GET

**Endpoint**

```
http://localhost:8000
```

**Response**
<br/>
It will display the following JSON Response
```json
{
"message": "server started on port 8000"
}
```

### 2. Ask API 

The /ask api takes in the query (prompt) and llmModel in the request body and generates an accurate response. It works on the  Reason + Action (ReAct) model to understand, fetch, validate, and iterate on data queries with the help of the llm model specified in the request body to generate the response. The Agent thinks till it gets the final answer

**HTTP Method Type** : POST

**Request Body Fields**

- query
- llmModel

**Endpoint**

```
http://localhost:8000/ask
```
#### Example 1: query = "What is the time now" , llmModel="gemini-1.5-flash" and tool used = Time 
**Curl Request**
```curl
curl --location 'http://localhost:8000/ask' \
--header 'Content-Type: application/json' \
--data '{
    "query":"What is the time now",
    "llmModel":"gemini-1.5-flash"
}'
``` 

**Response**
```json
{
    "httpCode": 200,
    "msg": "Successfully Generated Response",
    "data": {
        "input": "What is the time now",
        "output": "07:09 PM"
    }
}
```

#### Example 2: query = "What is the time now", llmModel="gpt-4o-mini" and tool used = Time 
**Curl Request**
```curl
curl --location 'http://localhost:8000/ask' \
--header 'Content-Type: application/json' \
--data '{
    "query":"What is the time now",
    "llmModel":"gpt-4o-mini"
}'
``` 

**Response**
```json
{
    "httpCode": 200,
    "msg": "Successfully Generated Response",
    "data": {
        "input": "What is the time now",
        "output": "The current time is 07:25 PM."
    }
}
```

#### Example 3: query = "What is current block of polygon", llmModel="gpt-4o-mini" and tool used = Get Current Block 
**Curl Request**
```curl
curl --location 'http://localhost:8000/ask' \
--header 'Content-Type: application/json' \
--data '{
    "query":"What is current block of polygon",
    "llmModel":"gpt-4o-mini"
}'
``` 

**Response**
```json
{
    "httpCode": 200,
    "msg": "Successfully Generated Response",
    "data": {
        "input": "What is current block of polygon",
        "output": "The current block of the Polygon network is 68196058."
    }
}
```

#### Example 4: query = "What is the time now" and llmModel="gpt-4o-mini"
**Curl Request**
```curl
curl --location 'http://localhost:8000/ask' \
--header 'Content-Type: application/json' \
--data '{
    "query":"What is the time now",
    "llmModel":"gpt-4o-mini"
}'
``` 

**Response**
```json
{
    "httpCode": 200,
    "msg": "Successfully Generated Response",
    "data": {
        "input": "What is the time now",
        "output": "The current time is 07:25 PM."
    }
}
```

#### Example 5: query = "What is the time now" and llmModel="gpt-4o-mini"
**Curl Request**
```curl
curl --location 'http://localhost:8000/ask' \
--header 'Content-Type: application/json' \
--data '{
    "query":"What is the time now",
    "llmModel":"gpt-4o-mini"
}'
``` 

**Response**
```json
{
    "httpCode": 200,
    "msg": "Successfully Generated Response",
    "data": {
        "input": "What is the time now",
        "output": "The current time is 07:25 PM."
    }
}
```



