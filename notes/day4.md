# Day 4 - AI Agents and Tools (Generative AI  Vs  AI Agents  Vs  Agentic AI)

## Generative AI- 
To generate some new content like:
image,text,audio,video,frame,code etc.

it has certain libraries like:
LangChain, LangGraph, LLamaIndex,  GROQ, OpenAI


## AI Agents- 
Ans- An AI Agent is an AI System that can think, decide and use tools to get a task done insted of only generating text.
Note- as LLM is trained on some past data and is not connected to internet ,so it dosent has current knowledge and it wont be able to answer question like, what is the current latest news or where will the tommorow's ipl match hold?
And if we ask for some particular company's data it wont be able to provide information related to that as that data would be private to that company so only if its data is provided to llm through some external database only then will it be able to answer such question.

So when llm is not able to handle certain inputs it tries searching some third party api's or data source from which info can be fetched.That is where it will be making (tool call) and after getting the response from it llm will summarixe it and return the output. AND THIS COMPLETE PROCESS OF CALLING TOOL AND GETTING RESPONSE IS HANDLED BY A PARTICULAR AI AGENT.AI AGENT IS FOR A SPECIFIC TASK.


## Agentic AI- 
To automate the complex tasks, the entire workflow, by feeding human feedback.
 Suppose i need to convert a youtube video into a blog and then publish in my channel:

 YT -> Blog

 1. YT-> Transcript (AI Agent 1 will convert yt video by providing url to transcript)
 2. Creating Title  (AI Agent 2 will use llm and prompt to generate title from the transcript)
 3. Creating Description (AI Agent 3 will use llm and prompt to generate description from the transcript)
 4. Conclusion (AI Agent 4 will use llm and prompt to generate conclusion from the transcript)

 So here in Agentic ai we make ai agents communicate with each other to make task flow more effective and produces valuable result, by even adding human feedback.
 HERE AI AGENTS COLLABORATE WITH EACH OTHER TO ACHIEVE A GOAL.

 ## What is a Tool?
Ans- Its an external function or service that an AI can useto perform tasks such as calculations, searching web, or reading files.

## Why do LLMs need Tools?
Ans-LLM'S are great at generating texts but could not perform accurate calculations or fetch real time data or interact with external data on their own.

## Difference between an LLM and an Agent
Ans-
## llm                     ## Agents
 answer questions.            perform tasks.
 generate texts               use tools
 no actions                   perform actions
 limited knowledge            use external resources.

## Tasks Completed
1. Created tools.py
2. Implemented a Calculator Tool
3. Imported the calculator into the chatbot
4. Added rule-based tool routing

## Biggest Insight
A chatbot simply sends every query to an LLM.
An AI Agent first analyzes the user's request, decides whether a tool is needed, executes that tool if necessary, and only uses the LLM when required.