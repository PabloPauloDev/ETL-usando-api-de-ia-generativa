import openai
import Extraction
from Loading import update_user

openai.api_key = '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'

def generate_text(user):
    completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
      
        {
            "role": "system", 
            "content": "Preciso que seja um especialista em marketing bancario."
        },

        {
            "role": "user", 
            "content": f'Crie uma mensagem citando o nome do cliente para {user["name"]} sobre a importancia dos investimentos (maximo de 100 caracteres)'
        },

        ]
    )
    return completion.choices[0].message.content.strip('\"')



for user in Extraction.users:
    news = generate_text(user)
    user['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-de-vweek-2023-api/credit.svg",
        "description": f"{news}"
    })
    success = update_user(user)
    print(f"User {user['name']} updated? {success}")
