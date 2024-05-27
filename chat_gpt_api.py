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
            "text": "Respond only by ticker symbol, if does not exsists anwser no_data"
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": f"Give me ticker symbol of {input}."
            }
        ]
        }
    ]

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=1,
    max_tokens=20,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    symbol=response.choices[0].message.content

    return symbol


def get_company(input):

    
    messages=[
        {
        "role": "system",
        "content": [
            {
            "type": "text",
            "text": "You are a finance bot/ Answer only by one of: company name, crypto currency name, etf name or finance index name "
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": f"About what the text is? {input}"
            }
        ]
        }
    ]

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=1,
    max_tokens=130,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    symbol=response.choices[0].message.content

    return symbol