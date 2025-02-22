# Web3-AI-Agent
This repository contains a Web3-AI-Agent which can fetch realtime blockchain data with the help of set of tools defined which the Agent can use to query the Blockchain and fetch real time data. The Agent is built in a generic way through which it can work with different LLMs like deepseek, llama, Gemini, ChatGPT etc to solve queries. The Agent works on analyzing the query, reason out which Tool needs to be used, uses the tool and gets the data, reasons out if the answer is accurate for the query and repeats this cycle till the Agent is convinced that the current Answer is the correct answer.It works on the Reason and Action (React) Model. It has different blockchain http providers available to query real time data from the blockchain using those providers. The Agent has different tools through which it gets real time data from the blockchain using the http providers defined. It utilizes the web3.py package to query the blockchain. Built on fastapi, it can cater to different web3 AI applications. It leverages both LLMs installed locally using Ollama as well as LLMs like Gemini and ChatGPT through API Keys

## 🛠 Features
- Contains multiple LLM Models like chat gpt-4,gpt-4o-mini, deepseek-r1:latest, deepseek-coder:latest, deepseek-llm:7b , Google gemini-1.5-pro,gemini-1.5-flash,gemini-2.0-flash,gemini-2.0-flash-lite,llama2-stable:13b, llama3:latest, llama3.3:latest
- Open source LLM models like Deepseek, Llama etc are run locally using Ollama while Google Gemini and Chat GPT models are accessed through API keys generated from their respecitve websites. 
- Reason and Action (React) Agents being developed with Tools that understand the query and fetch real time data.
- Contain multiple LLM Tools which help the Agent get current data like getting current Time Tool, search Wikipedia Tool, Get Current Block of a network tool and Get Wallet Balance Tool
- Agent works on analyzing the query, reason out which Tool needs to be used, uses the tool and gets the data, reasons out if the answer is accurate for the query and repeats this cycle till the Agent is convinced he has got the current Answer.
- It supports Ethereum Mainnet, Polygon Mainnet, Arbitrum Mainnet, Zksync Mainnet, Optimism Mainnet , Fantom Opera Mainnet, Mantle Mainnet and Base Mainnet networks currently to fetch latest current block and native wallet balance. 
---

## Table of Contents

- [Installation Instructions](#installation-instructions)
- [Start Instructions](#start-instructions)
- [API Endpoints ](#all-endpoints)
	- [1. Server Check API](#1-server-check-api)
	- [2. Ask Model API ](#2-models--gpt-4o-mini-api)
 	


---


## 🔨 Tools 
LLMs are trained on previous data and so they are not able to fetch real time data. We can create specific agents using LLMs which have a set of tools to get real time data and perform a set of specific tasks the agent specializes. Our agent is a Web3 specific agent so it will have tools to query the blockchain and get data in real time. Below are the list of Tools the agent currently has:

- Get Current Time Tool : Useful for when the Agent needs to know the current time. Usually agents are not aware of the time as they are trained on past data. This tool helps the agent get the current time
- Search Wikipedia Tool : Useful for when the Agent needs to know information about a topic. The tool uses the Wikipedia package to get current data from Wikipedia. It requests summary of 2 lines on the input it recieves from the Agent
- Get Current Block Tool : Useful for when the Agent needs to know the current block number of a network.It supports 'ethereum','polygon','arbitrum','zksync','optimism','fantom','mantle','base' networks as input and returns a string output "The Current Block number for {networkName} ({chainId}) is {blockNumber}" based on network.
- Wallet Balance Tool : Useful for when when the Agent needs to know the balance of a address on a specific network.It takes in a string with network as input as the first parameter and the second parameter is the wallet address provided seperated by a comma. If no network is provided , it uses the Ethereum network.

## Packages
- FastAPI
- LangChain
- Web3.py
- python-dotenv
---

## LLM Models
- gpt-4:
- gpt-4o-mini
- deepseek-r1:latest
- deepseek-coder:latest
- deepseek-llm:7b
- gemini-1.5-pro
- gemini-1.5-flash
- gemini-2.0-flash
- gemini-2.0-flash-lite
- llama2-stable:13b
- llama3:latest
- llama3.3:latest
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
```env
OPENAI_API_KEY=
GEMINI_API_KEY=
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

## All Endpoints

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

This api exposes OpenAI's chatgpt-4o-mini model to be invoked and consumed by Applications. It takes the prompt in the request body and generates a response by the gpt-4o-mini model and returns back the results.

**HTTP Method Type** : POST

**Request Body Fields**

- query
- llmModel

**Endpoint**

```
http://localhost:8000/ask
```

**Curl Example**
```curl
curl --location 'http://localhost:8000/ask' \
--header 'Content-Type: application/json' \
--data '{
	"prompt": "What is 81 divided by 9"
}'
``` 

**Example Response**
```json
{
    "httpCode": 200,
    "msg": "Successfully Generated Response",
    "data": "81 divided by 9 is 9"
}
```

