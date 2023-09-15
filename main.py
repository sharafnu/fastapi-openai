from fastapi import FastAPI, Query
import openai
import os
import sys

OPENAI_API_KEY = ""  ## Refer readme

openai.api_key = OPENAI_API_KEY

app = FastAPI(
    title="Simple API",
)


def get_response_openai(prompt):
    try:
        prompt = prompt
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            n=1,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert sports analyst, covering football and cricket. Answer in elegant and consise sentences to the questions being asked by the end user.",
                },
                {"role": "user", "content": prompt},
            ],
        )
    except Exception as e:
        print("Error in creating response from openAI:", str(e))
        return 503
    return response["choices"][0]["message"]["content"]


@app.get(
    "/chat/",
    tags=["APIs"],
    response_model=str,
)
def chat(query: str = Query()):
    return get_response_openai(query)
