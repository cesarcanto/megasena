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

    # Lista para armazenar informações sobre os acertos
    acertos = {
        6: [],
        5: [],
        4: [],
        3: []
    }

    for linha in linhas_arquivo:
        quantidade_apostas += 1
        numeros = linha.strip().split()  # Separa por espaços por padrão
        numeros_do_jogo = set(map(int, numeros))
        qtd_acertos = len(resultados.intersection(numeros_do_jogo))

        if qtd_acertos in [3, 4, 5, 6]:
            acertos[qtd_acertos].append(numeros_do_jogo)

    # Exibir as informações consolidadas
    print(f"⚠️ Atualizando sobre as apostas na Mega Sena:\n")
    print(f"⚠️ Quantidade de apostas realizadas: {quantidade_apostas}\n")
    print(f"📅 Data do Sorteio: {data_sorteio}\n")  # Emoji de calendário na data
    print(f"🔢 Números Sorteados: {resultados}\n")
    print(f"✅ Resultados: ")

    acertos_totais = sum([len(acertos[i]) for i in range(3, 7)])
    
    for acerto, jogos in acertos.items():
        if jogos:
            if acerto == 6:
                print(f"\nSENA - 6 números: {acerto}")
            elif acerto == 5:
                print(f"\nQUINA - 5 números: {acerto}")
            elif acerto == 4:
                print(f"\nQUADRA - 4 números: {acerto}")
            elif acerto == 3:
                print(f"\nTerno - 3 números: {acerto}")
            
            for jogo in jogos:
                print(f"Números: {jogo}")
            
            print(f"Quantidade de jogos acertados: {len(jogos)}")
            acertos_totais += len(jogos)

    if acertos_totais == 0:
        print("\n😞 Que pena, não acertamos nada dessa vez!")
    else:
        print("\n🎉 Parabéns a todos! Comemoremos juntos! 🎉")
