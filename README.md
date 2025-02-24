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
#### Example 1: query = "What is the time now" and llmModel="gemini-1.5-flash" 
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

#### Example 2: query = "What is the time now" and llmModel="gpt-4o-mini" 
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

#### Example 3: query = "What is current block of polygon" and llmModel="gpt-4o-mini"
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

#### Example 4: query = "What is current block of Optimism" and llmModel="llama3"
**Curl Request**
```curl
curl --location 'http://localhost:8000/ask' \
--header 'Content-Type: application/json' \
--data '{
    "query":"What is current block of Optimism",
    "llmModel":"llama3"
}'
``` 

**Response**
```json
{
    "httpCode": 200,
    "msg": "Successfully Generated Response",
    "data": {
        "input": "What is current block of Optimism",
        "output": "The current block number of Optimism is 21910949."
    }
}
```

#### Example 5: query = "What is the current block of base mainnet" and llmModel="gemini-2.0-flash"
**Curl Request**
```curl
curl --location 'http://localhost:8000/ask' \
--header 'Content-Type: application/json' \
--data '{
    "query":"What is current block of base mainnet",
    "llmModel":"gemini-2.0-flash"
}'
``` 

**Response**
```json
{
    "httpCode": 200,
    "msg": "Successfully Generated Response",
    "data": {
        "input": "What is current block of base mainnet",
        "output": "26681533"
    }
}
```

#### Example 6: query = "What is current block of mantle mainnet" and llmModel="deepseek-r1"
**Curl Request**
```curl
curl --location 'http://localhost:8000/ask' \
--header 'Content-Type: application/json' \
--data '{
    "query":"What is current block of mantle mainnet",
    "llmModel":"deepseek-r1"
}'
``` 

**Response**
```json
{
    "httpCode": 200,
    "msg": "Successfully Generated Response",
    "data": {
        "input": "What is current block of mantle mainnet",
        "output": "The current block number for the Mantle network's mainnet is 21911088."
    }
}
```

#### Example 7: query = "When did Barack Obama die" and llmModel="gemini-1.5-flash"
**Curl Request**
```curl
curl --location 'http://localhost:8000/ask' \
--header 'Content-Type: application/json' \
--data '{
    "query":"When did Barack Obama die",
    "llmModel":"gemini-1.5-flash"
}'
``` 

**Response**
```json
{
    "httpCode": 200,
    "msg": "Successfully Generated Response",
    "data": {
        "input": "When did Barack Obama die",
        "output": "Barack Obama is still alive, so he has not died."
    }
}
```

#### Example 8: query = "Who is Nelson Mandela" and llmModel="deepseek-llm:7b"
**Curl Request**
```curl
curl --location 'http://localhost:8000/ask' \
--header 'Content-Type: application/json' \
--data '{
    "query":"Who is Nelson Mandela",
    "llmModel":"deepseek-llm:7b"
}'
``` 

**Response**
```json
{
    "httpCode": 200,
    "msg": "Successfully Generated Response",
    "data": {
        "input": "Who is Nelson Mandela",
        "output": "Nelson Mandela was a South African anti-apartheid activist and politician who served as the first president of South Africa from 1994 to 1999. He was a key figure in the fight against apartheid and spent 27 years in prison for his activism before becoming the country's first black head of state."
    }
}
```

#### Example 9: query = "What is the balance of 0x415c8893D514F9BC5211d36eEDA4183226b84AA7 on ethereum network" and llmModel="gpt-4o-mini"
**Curl Request**
```curl
curl --location 'http://localhost:8000/ask' \
--header 'Content-Type: application/json' \
--data '{
    "query":"What is the balance of 0x415c8893D514F9BC5211d36eEDA4183226b84AA7 on ethereum network",
    "llmModel":"gpt-4o-mini"
}'
``` 

**Response**
```json
{
    "httpCode": 200,
    "msg": "Successfully Generated Response",
    "data": {
        "input": "What is the balance of 0x415c8893D514F9BC5211d36eEDA4183226b84AA7 on ethereum network",
        "output": "The balance of the wallet address 0x415c8893D514F9BC5211d36eEDA4183226b84AA7 on the Ethereum network is 47.263273342183228043 Ether."
    }
}
```

#### Example 10: query = "What is the balance of 0x7a5Aa13a31155315B13cbFE163fc8222Ea1D8657 on base network" and llmModel="gpt-4o-mini"
**Curl Request**
```curl
curl --location 'http://localhost:8000/ask' \
--header 'Content-Type: application/json' \
--data '{
    "query":"What is the balance of 0x7a5Aa13a31155315B13cbFE163fc8222Ea1D8657 on base network",
    "llmModel":"gpt-4o-mini"
}'
``` 

**Response**
```json
{
    "httpCode": 200,
    "msg": "Successfully Generated Response",
    "data": {
        "input": "What is the balance of 0x7a5Aa13a31155315B13cbFE163fc8222Ea1D8657 on base network",
        "output": "The balance of 0x7a5Aa13a31155315B13cbFE163fc8222Ea1D8657 on the Base network is 0.010830224416519167 Ether."
    }
}
```

#### Example 11: query = "Fetch Optimism network balance of 0xeCDecb868503Ea7D81cb0573e367b536A820Af4E" and llmModel="gemini-2.0-flash"
**Curl Request**
```curl
curl --location 'http://localhost:8000/ask' \
--header 'Content-Type: application/json' \
--data '{
    "query":"Fetch Optimism network balance of 0xeCDecb868503Ea7D81cb0573e367b536A820Af4E ",
    "llmModel":"gemini-2.0-flash"
}'
``` 

**Response**
```json
{
    "httpCode": 200,
    "msg": "Successfully Generated Response",
    "data": {
        "input": "What is the balance of 0xeCDecb868503Ea7D81cb0573e367b536A820Af4E on Optimism network",
        "output": "The balance of 0xeCDecb868503Ea7D81cb0573e367b536A820Af4E on Optimism network is 0.069785790710600851 Ether"
    }
}
```

#### Example 12: query = "Fetch Optimism network balance of 0xeCDecb868503Ea7D81cb0573e367b536A820Af4E" and llmModel="llama3"
**Curl Request**
```curl
curl --location 'http://localhost:8000/ask' \
--header 'Content-Type: application/json' \
--data '{
    "query":"Who is John Wick",
    "llmModel":"llama3"
}'
``` 

**Response**
```json
{
    "httpCode": 200,
    "msg": "Successfully Generated Response",
    "data": {
        "input": "Who is John Wick",
        "output": "John Wick is an American neo-noir crime action film series and media franchise created by Derek Kolstad, centered on the titular character portrayed by actor Keanu Reeves."
    }
}
```

#### Example 12: query = "Fetch Optimism network balance of 0xeCDecb868503Ea7D81cb0573e367b536A820Af4E" and llmModel="deepseek-llm:7b"
**Curl Request**
```curl
curl --location 'http://localhost:8000/ask' \
--header 'Content-Type: application/json' \
--data '{
    "query":"Who is Nelson Mandela",
    "llmModel":"deepseek-llm:7b"
}'
``` 

**Response**
```json
{
    "httpCode": 200,
    "msg": "Successfully Generated Response",
    "data": {
        "input": "Who is Nelson Mandela",
        "output": "Nelson Mandela was a South African anti-apartheid activist and politician who served as the first president of South Africa from 1994 to 1999. He was a key figure in the fight against apartheid and spent 27 years in prison for his activism before becoming the country's first black head of state."
    }
}
```
