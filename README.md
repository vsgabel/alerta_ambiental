# Alerta Ambiental

Este bot foi construído na live da DevStars em 02 de julho de 2022. A aula está disponível no link https://www.youtube.com/watch?v=aVvHRJhEcqY&t=1s. 

## Recomendações de Conhecimento

- Um conhecimento mínimo de Python (tipos de variáveis, listas, funções e loops __while__ e __for__)
- Saber utilizar o Telegram

## Configurações

É necessário ter o Python 3.6 (ou superior) instalado em sua máquina. Para instalar a biblioteca do Telegram no Python, digite:

> pip install pyTelegramBotApi

Para instalar a biblioteca __Requests__ do Python, digite:
> pip install requests

## Desafios

O código claramente não foi construído com eficiência em foco, mas sim com simplicidade. Algumas das coisas que você pode fazer são:
- **Otimizar o algoritmo de verificação das cidades**. Há necessidade de verificar a mesma cidade diversas vezes? É isso que vai acontecer se tivermos mais de um usuário na mesma cidade.
- **Implementar um banco de dados**. Bancos de dados provém um armazenamento rápido e eficaz se devidamente programados. Como você construiria as tabelas? Pense nisso.
- **Obter dados de outras fontes**. Um projeto como este não precisa ficar restrito a uma única fonte de dados. Sabemos que a API do OpenWeather fornece dados de temperatura, humidade e pressão atmosférica, mas não fornece dados pluviométricos (quantidade de chuvas). Que outra API poderíamos utilizar para isto?
- **Expandir para um contexto global**. Neste momento, nosso bot foi construído visando o público brasileiro. Como podemos expandir para uma audiência mundial?

## Considerações Finais

Espero que vocês tenham gostado dessa aula e espero que sintam interesse em trabalhar com esse código. Não tenham medo de me contatar pelo e-mail victor.gabel@gmail.com mostrando o que fizeram!
