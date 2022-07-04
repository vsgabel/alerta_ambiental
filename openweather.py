import requests
from config import chave_ow

def pega_tempo(cidade, estado, pais="BR"):
    geografica = geo(cidade, estado, pais)
    lat, lon = geografica[0]['lat'], geografica[0]['lon']

    return pega_tempo_lat_lon(lat, lon)

def pega_previsao(cidade, estado, pais="BR"):
    geografica = geo(cidade, estado, pais)
    lat, lon = geografica[0]['lat'], geografica[0]['lon']

    return pega_previsao_lat_lon(lat, lon)

def pega_tempo_lat_lon(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={chave_ow}&units=metric"
    return requests.get(url).json()

def pega_previsao_lat_lon(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={chave_ow}&units=metric"
    return requests.get(url).json()

def geo(cidade, estado, pais="BR"):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={cidade},{estado},{pais}&appid={chave_ow}"
    return requests.get(url).json()