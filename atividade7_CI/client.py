"""
    - Descrição: Implementação de um serviço de notificação de tweets de um determinado tópico,
    parte do cliente que prove as seguintes funcionalidades:
        - Assinatura de clientes (Assinantes) para um ou mais tópicos no serviço de mensagens.
        - Recebimento dos tópicos de interesse pelos assinantes.
        
    - Autores:
        Matheus Henrique Sechineli
        Vinicius Kuwakino

    - Data de criação: 04/06/2022
    - Data de atualização: 09/06/2022
"""


import json
import pika


# Sobrescrevendo a funcao de callback do pika
def callback(ch, method, properties, body):    
  
  # Faz um parser do arquivo e converte num dicionario
  tweet = json.loads(body.decode())
  
  print('Created_at: ' + tweet['created_at'])
  print('Username: ' + tweet['user']['name'])
  print('Text: ' + tweet['text'])
  print('====================================================================================')


# Consome da fila de tweets do topico "onepiece"
def onepieceQueue(channel, queue):
  print('================================  Topic: One Piece  ================================')
  channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=callback)
  channel.start_consuming()

  
# Consome da fila de tweets do topico "bleach"
def bleachQueue(channel, queue):
  print('=================================  Topic: Bleach  =================================')
  channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=callback)
  channel.start_consuming()
  
  
# Consome da fila de tweets dos dois topicos
def ambosQueue(channel, queue):
  print('=================================  Topic: Ambos  =================================')
  channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=callback)
  channel.start_consuming()


def run():
  
  # Estabelecendo uma conexao com o servidor
  connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
  channel = connection.channel()

  # Declarando o nome do exchange e o tipo
  channel.exchange_declare(exchange='onepiece', exchange_type='fanout')
  channel.exchange_declare(exchange='bleach', exchange_type='fanout')
  channel.exchange_declare(exchange='ambos', exchange_type='fanout')

  # Criacao de uma fila com nome aleatorio, escolhido pelo servidor
  # Quando um consumidor encerra o servico, a fila é excluida
  queue_onepiece = channel.queue_declare(queue='', exclusive=True)
  queue_bleach = channel.queue_declare(queue='', exclusive=True)
  queue_ambos = channel.queue_declare(queue='', exclusive=True)

  # O exchange enviara mensagens para a fila 
  channel.queue_bind(exchange='onepiece', queue=queue_onepiece.method.queue)
  channel.queue_bind(exchange='bleach', queue=queue_bleach.method.queue)
  channel.queue_bind(exchange='ambos', queue=queue_ambos.method.queue)

  # Interface para informar quais tweets o cliente deseja receber
  print("Receber tweets digite:")
  print("1 - One Piece")
  print("2 - Bleach")
  print("3 - Ambos")

  # Recebe a opcao que o cliente selecionou
  option = input()

  # Dado a opcao selecionada, invoca as funcoes para consumir os tweets
  if option == '1':
    onepieceQueue(channel, queue_onepiece)
  if option == '2':
    bleachQueue(channel, queue_bleach)
  if option == '3':
    ambosQueue(channel, queue_ambos)


if __name__ == '__main__':
  run()
