import telebot
from arquivo import carrega, salva
from openweather import pega_tempo
from config import chave_api

bot = telebot.TeleBot(chave_api)

@bot.message_handler(commands=["start"])
def start(message):
    '''
    Mensagem de boas vindas
    '''
    bot.reply_to(message, "Bem-vindo ao Alerta Ambiental. Digite " +\
                        "o comando /cidade seguido do nome da cidade/estado (ex: Curitiba/Paraná) " +\
                        "onde você reside e eu te mandarei avisos caso o clima fique " +\
                        "ruim ou perigoso!"   
        )

@bot.message_handler(commands=["cidade"])
def cidade(message):
    '''
    Configura a cidade do usuário
    '''
    c = message.text
    c = c.replace("/cidade ", "").replace("/cidade", "")
    if c == "":
        bot.reply_to(message, "Digite uma cidade válida.")
    elif "/" not in c:
        bot.reply_to(message, "Digite a cidade/estado.")
    else:
        cid, est = c.split("/")
        dado = {"chat_id": str(message.chat.id), "city": cid, "state": est}
        salva(dado)
        bot.reply_to(message, f"A localização {c} foi registrada.")

@bot.message_handler(commands=['situacao', 'situação'])
def situacao(message):
    '''
    Verifica a situação da cidade do usuário
    '''
    dados = carrega()
    if str(message.chat.id) in dados.keys():
        dado = dados[str(message.chat.id)]
        tempo = pega_tempo(dado['city'], dado['state'])
        bot.reply_to(message, f"A temperatura em {dado['city']} é de {tempo['main']['temp']}° C.")
    else:
        bot.reply_to(message, "Registre uma cidade primeiro")

if __name__ == "__main__":
    bot.infinity_polling()