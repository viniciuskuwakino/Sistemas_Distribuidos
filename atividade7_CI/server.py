"""
    - Descrição: Implementação de um serviço de notificação de tweets de um determinado tópico,
    parte do servidor que prove as seguintes funcionalidades:
        - Consumo e processamento dos tweets por módulos do classificador.

    - Autores:
        Matheus Henrique Sechineli
        Vinicius Kuwakino

    - Data de criação: 04/06/2022
    - Data de atualização: 09/06/2022
"""


import json
import pika


# Sobrescrevendo a funcao de callback
def callback(ch, method, properties, body):
  
  print(' [*] Tweet recebido!')
  
  # Faz um parser do arquivo e converte num dicionario
  tweet = json.loads(body.decode())
  
  print(' [x] Enviando tweet para fila!')
  for hashtag in tweet['entities']['hashtags']:
    if hashtag['text'].lower() == 'onepiece':
      ch.basic_publish(exchange='onepiece', routing_key='', body=body)
      ch.basic_publish(exchange='ambos', routing_key='', body=body)
    if hashtag['text'].lower() == 'bleach':
      ch.basic_publish(exchange='bleach', routing_key='', body=body)
      ch.basic_publish(exchange='ambos', routing_key='', body=body)


def run():
  # Estabelecendo uma conexao com o servidor
  connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
  channel = connection.channel()

  # Criando uma fila de mensagens
  channel.queue_declare(queue='tweets')

  # Declarando o nome do exchange e o tipo
  channel.exchange_declare(exchange='onepiece', exchange_type='fanout')
  channel.exchange_declare(exchange='bleach', exchange_type='fanout')
  channel.exchange_declare(exchange='ambos', exchange_type='fanout')

  # Dizemos ao RabbitMQ que a funcao callback sobrescrita recebera as mensagens da fila "tweets"
  channel.basic_consume(queue='tweets', auto_ack=True, on_message_callback=callback)

  channel.start_consuming()


if __name__ == '__main__':
  run()
