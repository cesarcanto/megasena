import requests
import sys

# Mensagem indicando início da captura na API da Mega Sena
print("✅ Iniciando captura na API da Mega Sena. Aguarde, carregando...")

# API da Caixa para obter o resultado mais recente da Mega Sena
url = 'https://apiloterias.com.br/app/v2/resultado?loteria=megasena'

# Função para buscar os dados da API da Mega Sena
def obter_dados_mega_sena():
    try:
        response = requests.get(url, timeout=40)  # Tempo limite de 10 segundos
        response.raise_for_status()  # Levanta uma exceção se a resposta indicar erro
        return response.json()
    except requests.exceptions.RequestException as e:
        print("❌ Falha ao obter os números sorteados:", e)
        sys.exit(1)  # Encerra o programa com código de erro 1
    

# Obtém os dados da Mega Sena
dados_mega_sena = obter_dados_mega_sena()

# Se os dados foram obtidos com sucesso, prosseguir
if dados_mega_sena:
    numeros_sorteio = dados_mega_sena.get('dezenas', [])
    data_sorteio = dados_mega_sena.get('data_concurso')
    premiacao = dados_mega_sena.get('premiacao')

    # Aqui você pode usar os dados obtidos da API da Mega Sena como necessário

# Mensagem indicando finalização da captura na API da Mega Sena
print("✅ Finalizada a captura na API da Mega Sena.")
