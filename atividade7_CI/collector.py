"""
    - Descrição: Implementação de um serviço de notificação de tweets de um determinado tópico,
    parte do coletor que prove as seguintes funcionalidades:
        - Coleta de tweets a partir do sítio original ou a partir da leitura de um arquivo (json).
        - Envio dos tweets coletados para uma fila de mensagens.

    - Autores:
        Matheus Henrique Sechineli
        Vinicius Kuwakino

    - Data de criação: 04/06/2022
    - Data de atualização: 08/06/2022
"""
    

import json
from time import sleep
import pika


# Estabelecendo uma conexao com o servidor
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Criando uma fila de mensagens
channel.queue_declare(queue='tweets')

# Abre o arquivo que contem o tweets
with open('tweets.json') as file:
  # Faz um parser do arquivo e converte num dicionario
  tweets = json.load(file)

  # Percorre o dicionario de tweets
  for tweet in tweets:

    # Converte o dicionario para string
    tweet_str = json.dumps(tweet)
    print(tweet_str)
    print("TWWWEEEET")
    sleep(5)

    # Utilizando a troca padrao declarando uma string vazia em "exchange",
    # definindo o nome da fila em "routing_key",
    # enviamos a mensagem em "body" com a mensagem "primeiro tweet"
    channel.basic_publish(exchange='', routing_key='tweets', body=tweet_str.encode())

# Encerra a conexao
connection.close()
