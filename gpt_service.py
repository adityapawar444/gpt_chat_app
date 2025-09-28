import os
import traceback

from openai import OpenAI, APIError, RateLimitError

MODE = os.environ['MODE']
if os.environ['MODE'] != 'dev':
    OPENAI_API_KEY = os.environ['OPEN_AI_API_KEY']
    print(OPENAI_API_KEY)

def get_gpt_response(input: str) -> str:

    if MODE == 'dev':
        return input

    client = OpenAI(api_key=OPENAI_API_KEY)

    try:
        completion = client.chat.completions.create(
          model="gpt-5",
          messages=[
            {"role": "developer", "content": "You are a helpful assistant."},
            {"role": "user", "content": input}
          ]
        )
        return completion.choices[0].message
    except APIError as e:
        return e.response.json()['error']['message']
    except Exception as e:
        return e.message

