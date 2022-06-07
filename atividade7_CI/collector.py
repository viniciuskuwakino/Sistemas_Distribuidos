import pika
import json

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

        # Utilizando a troca padrao declarando uma string vazia em "exchange",
        # definindo o nome da fila em "routing_key",
        # enviamos a mensagem em "body" com a mensagem "primeiro tweet"
        channel.basic_publish(exchange='', routing_key='tweets', body=tweet_str.encode())

# Encerra a conexao
connection.close()
