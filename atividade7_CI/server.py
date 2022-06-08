"""
    - Descrição: Implementação de um serviço de notificação de tweets de um determinado tópico,
    parte do servidor que prove as seguintes funcionalidades:
        - Consumo e processamento dos tweets por módulos do classificador.

    - Autores:
        Matheus Henrique Sechineli
        Vinicius Kuwakino

    - Data de criação: 04/06/2022
    - Data de atualização: 08/06/2022
"""


import json
import pika


# Sobrescrevendo a funcao de callback
def callback(ch, method, properties, body):    
  tweet = json.loads(body.decode())
  for hashtag in tweet['entities']['hashtags']:
    print(hashtag['text'].lower())
    if hashtag['text'].lower() == 'onepiece':
      ch.basic_publish(exchange='', routing_key='onepiece', body=body)
    if hashtag['text'].lower() == 'bleach':
      ch.basic_publish(exchange='', routing_key='bleach', body=body)


def run():
  # Estabelecendo uma conexao com o servidor
  connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
  channel = connection.channel()

  # Criando uma fila de mensagens
  channel.queue_declare(queue='tweets')
  channel.queue_declare(queue='onepiece')
  channel.queue_declare(queue='bleach')
  
  # Dizemos ao RabbitMQ que a funcao callback sobrescrita recebera as mensagens da fila "tweets"
  channel.basic_consume(queue='tweets', auto_ack=True, on_message_callback=callback)

  channel.start_consuming()


if __name__ == '__main__':
  run()
