# Regex Rule-Based Chatbot

![Python](https://img.shields.io/badge/Python-rule--based-3776AB?logo=python&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-pattern%20matching-lightgrey)

A lightweight command-line chatbot that matches user messages against regular-expression patterns. It is a beginner-friendly example of intent routing using explicit rules rather than machine learning or an LLM.

## Supported intents

- Greetings: hi, hello, hey, good morning, good evening
- Education: college, exam, study, project, subject
- Weather: weather, rain, temperature, climate
- Help: help, support, assist
- Exit: bye, exit, quit, goodbye

For each recognized intent, the program returns a predefined response. Unmatched input receives a fallback response. Weather replies are static; the chatbot does not retrieve current weather or use the user's location.

## Architecture

Terminal input → lowercase normalization → regex intent matching → predefined reply and intent → exit check or next prompt

All conversation logic is in main.py. The patterns and response text are regular Python dictionaries, so the behavior can be changed without a model or service.

## Run locally

Install Python 3 and run:

    python main.py

Type messages at the You prompt. Enter an exit phrase such as bye or quit to end the loop. There are no third-party dependencies.

## Project layout

- main.py — intent patterns, response mapping, response function, and interactive loop
- README.md — project guide

## Extend the chatbot

Add a pattern and a corresponding response entry for a new intent. Keep patterns specific enough to avoid matching common words accidentally. For more robust behavior, add input validation and unit tests around chatbot_response().

## Limitations

The bot uses substring-style regex intent matching, has no conversation memory, and always returns the first configured response for an intent. It does not use an NLP model, network access, or persistent storage. No automated tests or license file are listed.