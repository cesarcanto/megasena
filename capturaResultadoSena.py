import requests
import sys
import time

def obter_dados_mega_sena(opcao_usuario=None, numeros_digitados=None):
    if opcao_usuario == 'S':
        # Se o usuário optou por digitar manualmente, retorna os números fornecidos
        return {'dezenas': numeros_digitados}, 0
    
    url = 'https://apiloterias.com.br/app/v2/resultado?loteria=megasena'
    max_tentativas = 5
    tempo_espera = 5

    for tentativa in range(1, max_tentativas + 1):
        try:
            print("⚠️ Aguarde, carregando...")
            start_time = time.time()
            response = requests.get(url, timeout=40)
            response.raise_for_status()
            tempo_captura = round(time.time() - start_time, 2)
            return response.json(), tempo_captura
        except requests.exceptions.RequestException as e:
            print(f"❌ Falha ao obter os números sorteados: {e}")
            if tentativa < max_tentativas:
                print(f"⚠️ Tentando novamente em {tempo_espera} segundos...")
                time.sleep(tempo_espera)
            else:
                print("❌ Número máximo de tentativas atingido. Saindo...")
                sys.exit(1)

# Exemplo de uso:
opcao_usuario = input("Deseja digitar os números sorteados manualmente? (S/N): ").upper()

if opcao_usuario == 'S':
    # Validação e coleta dos números do usuário
    numeros_sorteio = []
    while len(numeros_sorteio) != 6:
        try:
            numero = int(input("Digite um número (entre 1 e 60): "))
            if 1 <= numero <= 60 and numero not in numeros_sorteio:
                numeros_sorteio.append(numero)
            elif numero in numeros_sorteio:
                print("Número já foi digitado. Tente novamente.")
            else:
                print("Por favor, digite um número entre 1 e 60.")
        except ValueError:
            print("Por favor, digite um número inteiro.")
    
    print("✅ Números escolhidos pelo usuário:", numeros_sorteio)

# Obtém os números da API ou os números digitados manualmente
dados_mega_sena, tempo_captura = obter_dados_mega_sena(opcao_usuario, numeros_sorteio if opcao_usuario == 'S' else None)

if dados_mega_sena:
    numeros_sorteio = dados_mega_sena.get('dezenas', [])
    data_sorteio = dados_mega_sena.get('data_concurso')
    premiacao = dados_mega_sena.get('premiacao')
    
    # Exibe os números sorteados
    if opcao_usuario != 'S':
        print("✅ Números sorteados:", numeros_sorteio)
        print("⏰ A captura na API da Mega Sena demorou", tempo_captura, "segundos")


print("✅ Finalizado o processo")
