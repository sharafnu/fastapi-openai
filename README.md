# FAST API with OpenAI

<div align="center">
  <a alt="FastAPI logo" href="https://fastapi.tiangolo.com/" target="_blank" rel="noreferrer">
    <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="100">
  </a>
  <a alt="OpenAI logo" href="https://openai.com/" target="_blank" rel="noreferrer">
    <img src="https://static.cdnlogo.com/logos/o/29/OpenAI-Logo_800x800.png" width="100">
  </a>

</div>

✨ **Tech Stack** ✨

- [FastAPI.js](https://fastapi.tiangolo.com/)
- [OpenAI](https://openai.com/)

## Introduction

This project has a basic FastAPI endpoint to interact with OpenAI. It connects to gpt-3.5-turbo model.

## Prerequisites

- Make sure Python setup (with Pip) is available
- Get your OpenAI API key [here](https://platform.openai.com/account/api-keys).
- Modify main.py to include the OPENAI_API_KEY
  

## Setup

### Create virtual environment:
```bash
python -m venv openaienv
```
### Activate virtual environment:
```bash
source openaienv/bin/activate
```

### Intall the following dependecies
```bash
pip install "fastapi[all]"
pip install openai
```


### Start the app
```bash
uvicorn main:app --reload
```


## Check the API and invoke from SwaggerUI or via Postman

 http://127.0.0.1:8000/docs
