import requests
import sys
import time

def obter_dados_mega_sena():
    url = 'https://apiloterias.com.br/app/v2/resultado?loteria=megasena'
    max_tentativas = 5
    tempo_espera = 5
    tentativas = 0

    while tentativas < max_tentativas:
        try:
            print("⚠️ Aguarde, carregando...")
            response = requests.get(url, timeout=40)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ Falha ao obter os números sorteados: {e}")
            tentativas += 1
            if tentativas < max_tentativas:
                print(f"⚠️ Tentando novamente em {tempo_espera} segundos...")
                time.sleep(tempo_espera)
            else:
                print("❌ Número máximo de tentativas atingido. Saindo...")
                sys.exit(1)

print("✅ Iniciando captura na API da Mega Sena")

dados_mega_sena = obter_dados_mega_sena()

if dados_mega_sena:
    numeros_sorteio = dados_mega_sena.get('dezenas', [])
    data_sorteio = dados_mega_sena.get('data_concurso')
    premiacao = dados_mega_sena.get('premiacao')

print("✅ Finalizada a captura na API da Mega Sena")
