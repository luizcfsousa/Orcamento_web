import requests
import json

# Lista de todas as siglas de estados brasileiros
estados = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO",
    "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI",
    "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"
]

estados_cidades = {}

for sigla in estados:
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{sigla}/municipios"
    response = requests.get(url)
    if response.status_code == 200:
        municipios = response.json()
        estados_cidades[sigla] = [municipio['nome'] for municipio in municipios]
    else:
        print(f"Erro ao obter cidades de {sigla}")

# Salva em JSON
with open('estados_cidades.json', 'w', encoding='utf-8') as f:
    json.dump(estados_cidades, f, ensure_ascii=False, indent=2)

print("Arquivo estados_cidades.json gerado com sucesso!")
