from capturaResultadoSena import obter_dados_mega_sena

def padronizar_numeros(numeros):
    return set(map(int, numeros))

def validar_numeros(numeros):
    return all(num.isdigit() for num in numeros)

def exibir_informacoes_acertos(acertos):
    quantidade_total_jogos = sum([len(jogos) for jogos in acertos.values()])
    
    for acerto, jogos in acertos.items():
        if jogos:
            if acerto == 6:
                print(f"\nSENA - 6: {len(jogos)}")
            elif acerto == 5:
                print(f"\nQUINA - 5: {len(jogos)}")
            elif acerto == 4:
                print(f"\nQUADRA - 4: {len(jogos)}")
            elif acerto == 3:
                print(f"\nTerno - 3: {len(jogos)}")
            elif acerto == 2:
                print(f"\nDuque - 2: {len(jogos)}")
            elif acerto == 1:
                print(f"\n1 número: {len(jogos)}")

            for jogo in jogos:
                print(f"Números: {jogo}")
            
            print(f"Quantidade de jogos acertados: {len(jogos)}")

    if quantidade_total_jogos == 0:
        print("\n😞 Que pena, não acertamos nada dessa vez!")
    else:
        print("\n🎉 Parabéns a todos! Comemoremos juntos! 🎉")


def processar_resultados_acertos(resultados, linhas_arquivo):
    acertos = {
        6: [],
        5: [],
        4: [],
        3: [],
        2: [],
        1: []
    }

    for linha in linhas_arquivo:
        numeros = linha.strip().split()  # Separa por espaços por padrão

        if validar_numeros(numeros):
            numeros_do_jogo = set(map(int, numeros))
            qtd_acertos = len(resultados.intersection(numeros_do_jogo))

            if qtd_acertos in range(1, 7):
                acertos[qtd_acertos].append(numeros_do_jogo)

    return acertos

# Mensagem indicando que o programa está rodando
print("✅ Programa para verificação de resultados da Mega Sena em andamento...")

# Obtém os dados da Mega Sena
dados_mega_sena = obter_dados_mega_sena()

if dados_mega_sena:
    resultados = padronizar_numeros(dados_mega_sena.get('dezenas', []))
    resultados = set(resultados)
    data_sorteio = dados_mega_sena.get('data_concurso')
    premiacao = dados_mega_sena.get('premiacao')

    nome_arquivo = 'massa/jogoteste.txt'

    quantidade_apostas = 0

    with open(nome_arquivo, 'r') as file:
        linhas_arquivo = file.readlines()

    acertos = processar_resultados_acertos(resultados, linhas_arquivo)

    print(f"⚠️ Atualizando sobre as apostas na Mega Sena:\n")
    print(f"⚠️ Quantidade de apostas realizadas: {len(linhas_arquivo)}\n")
    print(f"📅 Data do Sorteio: {data_sorteio}\n")  
    print(f"🔢 Números Sorteados: {resultados}\n")
    print(f"✅ Resultados: ")

    exibir_informacoes_acertos(acertos)
else:
    print("\n😞 Não foi possível obter os resultados desta vez!")
