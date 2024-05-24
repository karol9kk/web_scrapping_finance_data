from openai import OpenAI
from config import OPENAI_API_KEY
client = OpenAI(api_key=OPENAI_API_KEY)

def get_stock_symbol(input):

    

    messages=[
        {
        "role": "system",
        "content": [
            {
            "type": "text",
            "text": "Give only a stock symbol, if there is no anwser no_data"
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": f"{input}"
            }
        ]
        }
    ]

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=1,
    max_tokens=10,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )


    symbol=response.choices[0].message.content

    return symbol