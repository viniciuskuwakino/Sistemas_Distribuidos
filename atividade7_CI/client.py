import json

import pika


# Sobrescrevendo a funcao de callback do pika
def callback(ch, method, properties, body):    
    tweet = json.loads(body.decode())
    print(tweet['text'])


def onepieceQueue(channel):
  channel.basic_consume(queue='onepiece', auto_ack=True, on_message_callback=callback)
  channel.start_consuming()
def bleachQueue(channel):
  channel.basic_consume(queue='bleach', auto_ack=True, on_message_callback=callback)
  channel.start_consuming()

def run():
    # Estabelecendo uma conexao com o servidor
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Criando uma fila de mensagens
    channel.queue_declare(queue='onepiece')
    channel.queue_declare(queue='bleach')

    print("Receber tweets digite:")
    print("1 - One Piece")
    print("2 - Bleach")
    print("3 - Ambos")

    option = input()

    if option == '1':
      onepieceQueue(channel)
    if option == '2':
      bleachQueue(channel)
    if option == '3':
      onepieceQueue(channel)
      bleachQueue(channel)


if __name__ == '__main__':
    run()
