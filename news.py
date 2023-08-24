import pandas as pd
import requests
import json
import openai
import os

#link para a api REST
sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'
openai_api_key = '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'

df = pd.read_csv('sdw2023.csv')
user_ids = df['UserID'].tolist()

def get_user(id):
  response = requests.get(f'{sdw2023_api_url}/users/{id}')
  return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(user, indent=2))

#conectando com a API OpenAI
openai.api_key = openai_api_key

def generate_ai_news(user):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
          "role": "system",
          "content": "Você é um especialista em finanças pessoais do banco Santander."
          },
      {
          "role": "user",
          "content": f"Crie uma proposta de crédito pessoal para o usuário {user['name']} de acordo com seu limite de cartão que é {user['card']['limit']}"
          }
    ]
  )
  return completion.choices[0].message.content.strip('\"')

for user in users:
  news = generate_ai_news(user)
  print(news)
  user['news'].append({
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": news
  })