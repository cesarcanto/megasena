import requests

def obter_resultado_mega_sena():
    # Faz a requisição à API da Caixa para obter o resultado mais recente da Mega Sena
    url = 'https://apiloterias.com.br/app/v2/resultado?loteria=megasena'
    # Substitua 'SEU_TOKEN_AQUI' pelo seu token de acesso à API, caso seja necessário

    response = requests.get(url)
    if response.status_code == 200:
        resultado = response.json()
        # Imprime o resultado completo para entender sua estrutura
        # print(resultado)
        numeros_sorteio = resultado.get('dezenas', [])
        return numeros_sorteio
    else:
        print("Falha ao obter os números sorteados")
        return None

# Salva o resultado obtido em uma variável
resultado_mega_sena = obter_resultado_mega_sena()

# Se for rodar este script sozinho, pode imprimir os números sorteados
if resultado_mega_sena:
    print(f"Os números sorteados da Mega Sena foram: {', '.join(map(str, resultado_mega_sena))}")
