from funcoes_mega_sena import *

dados_mega_sena = obter_dados_mega_sena()

if dados_mega_sena and 'dezenas' in dados_mega_sena:
    numeros_sorteados = dados_mega_sena['dezenas']
    resultados_sorteio = padronizar_numeros(numeros_sorteados)
    data_sorteio = dados_mega_sena.get('data_concurso')
    premiacao = dados_mega_sena.get('premiacao')

    nome_arquivo = 'massa/jogos.txt'
    lista_jogos = []

    try:
        with open(nome_arquivo, 'r') as file:
            linhas_arquivo = [linha.strip().split() for linha in file.readlines()]
            lista_jogos = [padronizar_numeros(numeros) for numeros in linhas_arquivo if validar_numeros(numeros)]
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")
        linhas_arquivo = []

    acertos = processar_resultados_acertos(resultados_sorteio, lista_jogos)

    print(f"⚠️ Atualizando sobre as apostas na Mega Sena:\n")
    print(f"⚠️ Quantidade de apostas realizadas: {len(linhas_arquivo)}\n")
    print(f"📅 Data do Sorteio: {data_sorteio}\n")
    print(f"🔢 Números Sorteados: {resultados_sorteio}\n")
    print(f"✅ Resultados: ")

    exibir_informacoes_acertos(acertos)

else:
    print("\n😞 Não foi possível obter os resultados desta vez!")
