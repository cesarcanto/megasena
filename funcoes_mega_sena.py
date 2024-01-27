from capturaResultadoSena import obter_dados_mega_sena

def validar_numeros(numeros):
    return all(str(num).isnumeric() for num in numeros) and len(numeros) == 6

def padronizar_numeros(numeros):
    return list(map(int, numeros))

def exibir_informacoes_acertos(acertos):
    quantidade_total_jogos = sum(len(jogos) for jogos in acertos.values())
    acertos_quadra_quina_sena = sum(len(jogos) for acerto in range(4, 7) for jogos in acertos[acerto])
    
    for acerto, jogos in acertos.items():
        if jogos:
            print(f"\n{nome_acerto(acerto)}: {len(jogos)}")
            for jogo in jogos:
                print(f"Jogo: {jogo}")

    # Adicione a verificação para acertos abaixo de quadra
    for acerto in range(1, 4):
        jogos = acertos.get(acerto, [])
        if jogos:
            print(f"\n{nome_acerto(acerto)}: {len(jogos)}")
            for jogo in jogos:
                print(f"Jogo: {jogo}")

    if acertos_quadra_quina_sena > 0:
        print("\n🎉 Parabéns a todos! Comemoremos juntos! 🎉")
    else:
        print("\n😞 Que pena, não acertamos nada dessa vez!")

    print(f"\nQuantidade de jogos acertados no total: {quantidade_total_jogos}")


def nome_acerto(acerto):
    acertos_nomes = {
        6: "SENA - 6",
        5: "QUINA - 5",
        4: "QUADRA - 4",
        3: "Terno - 3",
        2: "Duque - 2",
        1: "1 número"
    }
    return acertos_nomes.get(acerto, "")

try:
    # Obtém os números da API
    dados_mega_sena, _ = obter_dados_mega_sena()
    if not dados_mega_sena or 'dezenas' not in dados_mega_sena:
        raise Exception("Não foi possível obter os números sorteados.")
    
    resultados_da_api = dados_mega_sena['dezenas']

    # Leitura dos números do arquivo "jogos.txt"
    with open("massa/jogos.txt", "r") as arquivo_jogos:
        linhas_arquivo = [list(map(int, linha.strip().split())) for linha in arquivo_jogos]

    # Processamento de resultados
    acertos = {acerto: [] for acerto in range(1, 7)}

    for numeros_do_jogo in linhas_arquivo:
        # Suponha que as validações já foram feitas anteriormente
        qtd_acertos = len(set(resultados_da_api) & set(numeros_do_jogo))

        if 3 <= qtd_acertos <= 6:
            acertos[qtd_acertos].append(numeros_do_jogo)

    # Exibição de resultados
    exibir_informacoes_acertos(acertos)

except Exception as e:
    print(f"❌ Ocorreu um erro: {e}")
