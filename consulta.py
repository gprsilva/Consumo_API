import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get('API_KEY')
url=f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'

res= requests.get(url).json()

moedas_desejadas = ["BRL", "EUR", "JPY"]
cotacoes_filtradas = {moeda: res["conversion_rates"][moeda] for moeda in moedas_desejadas}

print(cotacoes_filtradas)
