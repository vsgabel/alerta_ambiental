import requests
from config import chave_api
from arquivo import carrega
from openweather import pega_previsao, pega_tempo
from time import sleep

def enviar(chave_api, chat_id, mensagem):
    '''
    Esta função envia uma mensagem para qualquer usuário do Telegram tendo sido fornecido
    um chat_id.
    '''
    return requests.post(f"https://api.telegram.org/bot{chave_api}/sendMessage",
                json={
                    "chat_id": str(chat_id),
                    "text": mensagem
                }
    )

def verificar():
    '''
    Esta função verifica se a cidade de algum usuário está passando por uma situação climática
    adversa. Para este caso específico, definimos temperaturas abaixo de 10° C ou maiores que
    30° C como adversa considerando um contexto brasileiro. Durante a execução das aulas, alteramos
    a menor temperatura para 30° C a fim de visualizar o seu funcionamento.
    '''
    dados = carrega()
    for chat_id in dados.keys():
        cidade, estado = dados[chat_id]['city'], dados[chat_id]['state']
        tempo = pega_tempo(cidade, estado)
        previsao = pega_previsao(cidade, estado)

        if tempo['main']['temp'] < 10:
            enviar(chave_api, chat_id, "A temperatura está menor que 10° C. Agasalhe-se!")

        if previsao['list'][0]['main']['temp'] < 10:
            enviar(chave_api, chat_id, f"A temperatura ficará menor que 10° C às {previsao['list'][0]['dt_txt']}. Leve um casaco!")
        
        if tempo['main']['temp'] > 35:
            enviar(chave_api, chat_id, "A temperatura está muito alta. Hidrate-se!")
        
        if previsao['list'][0]['main']['temp'] > 35:
            enviar(chave_api, chat_id, f"A temperatura ficará maior que 35° C às {previsao['list'][0]['dt_txt']}. Hidrate-se!")

while True:
    verificar()
    sleep(3600)

        

