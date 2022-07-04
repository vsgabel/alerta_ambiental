import json

def carrega():
    '''
    Carrega o arquivo "dados.json". Garanta que sempre exista pelo menos um conjunto
    de chaves ("{}") presente dentro deste arquivo.
    '''
    with open("dados.json", 'r') as arquivo:
        return json.load(arquivo)

def salva(dados):
    """
    Salva no arquivos "dados.json" os valores
    dados = {chat_id: "", "city": ""}
    """
    originais = carrega()
    originais[dados.pop('chat_id')] = dados

    with open("dados.json", 'w') as arquivo:
        json.dump(originais, arquivo)