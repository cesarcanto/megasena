from capturaResultadoSena import obter_dados_mega_sena

# Mensagem indicando que o programa está rodando
print("✅ Programa para verificação de resultados da Mega Sena em andamento...")

# Obtém os dados da Mega Sena
dados_mega_sena = obter_dados_mega_sena()

# Verifica se os dados foram obtidos com sucesso
if dados_mega_sena:
    resultados = set(dados_mega_sena.get('dezenas', []))
    data_sorteio = dados_mega_sena.get('data_concurso')
    premiacao = dados_mega_sena.get('premiacao')

    # Restante do seu código
    nome_arquivo = 'massa/jogos.txt'

    quantidade_apostas = 0
    jogos_da_mega_sena = []

    with open(nome_arquivo, 'r') as file:
        linhas_arquivo = file.readlines()

    # Listas para armazenar informações sobre os acertos
    acertos_6 = []
    acertos_5 = []
    acertos_4 = []

    for linha in linhas_arquivo:
        quantidade_apostas += 1
        numeros = linha.strip().split()  # Separa por espaços por padrão
        numeros_do_jogo = set(map(int, numeros))
        acertos = len(resultados.intersection(numeros_do_jogo))

        if acertos == 6:
            acertos_6.append(numeros)

        elif acertos == 5:
            acertos_5.append(numeros)

        elif acertos == 4:
            acertos_4.append(numeros)

    # Exibir as informações consolidadas
    print("🎉 Resultados da Mega Sena - 500 Apostas 🎉\n")
    print("Oi pessoal,")
    print("Atualizando sobre as apostas na Mega Sena: \n")
    print(f"Data do Sorteio: {data_sorteio}\n")
    print(f"🔢 Números Sorteados: {resultados}\n")
    print("✅ Acertos:")

    if acertos_6:
        print("\nSENA - 6 números:")
        for numeros in acertos_6:
            print(f"{numeros}")
    
    if acertos_5:
        print("\nQUINA - 5 números:")
        for numeros in acertos_5:
            print(f"{numeros}")

    if acertos_4:
        print("\nQUADRA - 4 números:")
        for numeros in acertos_4:
            print(f"{numeros}")

    print("\n🎉 Parabéns a todos! Comemoremos juntos! 🎉")
    print(f"\n✅ Quantidade de jogos realizados: {quantidade_apostas}")

else:
    print("❌ Falha ao obter os números sorteados da Mega Sena")
