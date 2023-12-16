from flask import Flask, render_template, request
from capturaResultadoSena import obter_dados_mega_sena

app = Flask(__name__)

# Função para validar se os números são válidos
def validar_numeros(numeros):
    return all(num.isdigit() for num in numeros)
# Função para processar os resultados e verificar acertos
def processar_resultados_acertos(resultados, linhas_arquivo):
    acertos = {6: [], 5: [], 4: [], 3: [], 2: [], 1: []}

    for linha in linhas_arquivo:
        numeros = linha.strip().split()  # Separa por espaços por padrão

        if validar_numeros(numeros):  # Verifica se os números são válidos
            try:
                numeros_do_jogo = set(map(int, numeros))
                qtd_acertos = len(resultados.intersection(numeros_do_jogo))

                # Garante que qtd_acertos esteja entre 1 e 6
                qtd_acertos = min(max(qtd_acertos, 1), 6)

                acertos[qtd_acertos].append(numeros_do_jogo)
            except ValueError:
                pass  # Ignora linhas que não puderem ser convertidas para números inteiros

    return acertos

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar o arquivo enviado pelo formulário
@app.route('/processar', methods=['POST'])
def processar_arquivo():
    arquivo = request.files['fileInput']

    if arquivo and arquivo.filename.endswith('.txt'):
        linhas_arquivo = arquivo.read().decode('utf-8').splitlines()

        # Obtém os dados da Mega Sena através da API da loteria
        dados_mega_sena = obter_dados_mega_sena()  # Chama a função da API da loteria

        if dados_mega_sena:
            resultados = set(dados_mega_sena.get('dezenas', []))  # Obtém os números sorteados
            acertos = processar_resultados_acertos(resultados, linhas_arquivo)

            # Retorna os acertos para exibir na página
            return render_template('resultados.html', acertos=acertos)
        
        return "Erro ao obter resultados da Mega Sena."

    return "Erro: Arquivo inválido ou não enviado corretamente."

if __name__ == '__main__':
    app.run(debug=True)
