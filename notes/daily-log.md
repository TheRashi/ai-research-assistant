# Day 1

## What I Learned ?
I learned:
1. What an LLM actually is and how it works.
2. What is RAG, Vector DB, data ingestion pipeline,retrieval pipeline,entire flowdiagram how the complete agents works from inside.

## Things I Found Confusing
1. I was initially confused about what is the use of LLM if we are buildint chatbot ourselves.
I understood as llm is the intelligence that generates the response after getting context from vector db using rag to prevent hallucination.

# Day 2

## What i learned ?
1. How do applications communicate with LLMs.
2. What an API is?
3. How Gemini API works?
4. How to securely store API keys?

## Key Insights
My chatbot is not intelligent.
Gemini is the intelligence
My chatbot just sends request and displays the response.

My application:
- Takes input
- Sends API request
- Receives response
- Displays output

# Day 3

# Day 3

## What I Learned

* Prompt Engineering
* System Prompts
* User Prompts
* AI Personas
* Error Handling

## Tasks Completed

* Created `prompts.py`
* Added DSA Mentor persona
* Added Career Coach persona
* Added GenAI Mentor persona
* Implemented persona selection in chatbot
* Dynamically generated prompts based on selected persona
* Added try-except error handling

## Biggest Insight

The same LLM can behave completely differently depending on the instructions (prompt) given to it.


## Progress Summary

My chatbot can now:

* Take user input
* Select different AI personas
* Generate responses using Gemini API
* Handle API errors gracefully

Today's work moved the project from a basic chatbot to a customizable AI assistant.
