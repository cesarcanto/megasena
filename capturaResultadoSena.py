import requests
import sys
import time

# Mensagem indicando início da captura na API da Mega Sena
print("✅ Iniciando captura na API da Mega Sena")

# API da Caixa para obter o resultado mais recente da Mega Sena
url = 'https://apiloterias.com.br/app/v2/resultado?loteria=megasena'

# Função para buscar os dados da API da Mega Sena
def obter_dados_mega_sena():
    while True:  # Loop infinito para tentar obter os dados
        try:
            print("⚠️ Aguarde, carregando...")
            response = requests.get(url, timeout=40)  # Tempo limite de 40 segundos
            response.raise_for_status()  # Levanta uma exceção se a resposta indicar erro
            return response.json()
        except requests.exceptions.RequestException as e:
            print("❌ Falha ao obter os números sorteados:", e)
            time.sleep(5)  # Aguarda 5 segundos antes da próxima tentativa

# Obtém os dados da Mega Sena
dados_mega_sena = obter_dados_mega_sena()

# Se os dados foram obtidos com sucesso, prosseguir
if dados_mega_sena:
    numeros_sorteio = dados_mega_sena.get('dezenas', [])
    data_sorteio = dados_mega_sena.get('data_concurso')
    premiacao = dados_mega_sena.get('premiacao')

# Mensagem indicando finalização da captura na API da Mega Sena
print("✅ Finalizada a captura na API da Mega Sena")
