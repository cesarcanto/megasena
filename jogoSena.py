from capturaResultadoSena import resultado_mega_sena, data_sorteio_mega_sena
    

def comparar_numeros(jogo_atual, numeros_jogo):
    numeros_acertados = len(jogo_atual.intersection(numeros_jogo))
    return numeros_acertados

# Abrir o arquivo com os jogos da Mega Sena
nome_arquivo = 'massa/jogos.txt'  # Nome do seu arquivo
with open(nome_arquivo, 'r') as file:
    jogos_da_mega_sena = file.readlines()

# Processar os números dos jogos da Mega Sena
for numeros in jogos_da_mega_sena:
    numeros = numeros.strip().split()  # Separa por espaços por padrão
    numeros_do_jogo = set(map(int, numeros))
    acertos = comparar_numeros(set(resultado_mega_sena), numeros_do_jogo)
    
    
    # Destacar se houver mais de 4 acertos no mesmo jogo
    if acertos >= 4:
        print("-----------------------------------------------------")
        print(f"A data do jogo Mega Sena é: {data_sorteio_mega_sena}")
        print("-----------------------------------------------------")
        print(f"No jogo {numeros}, você acertou {acertos} números.")
        print("-----------------------------------------------------")
    else:
        print("-----------------------------------------------------")
        print(f"A data do jogo Mega Sena é: {data_sorteio_mega_sena}")
        print("-----------------------------------------------------")
        print(f"Não houve nenhum jogo com 4 ou mais acertos!")
        print("-----------------------------------------------------")
        break
