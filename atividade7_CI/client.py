"""
    - Descrição: Implementação de um serviço de notificação de tweets de um determinado tópico,
    parte do cliente que prove as seguintes funcionalidades:
        - Assinatura de clientes (Assinantes) para um ou mais tópicos no serviço de mensagens.
        - Recebimento dos tópicos de interesse pelos assinantes.
        
    - Autores:
        Matheus Henrique Sechineli
        Vinicius Kuwakino

    - Data de criação: 04/06/2022
    - Data de atualização: 08/06/2022
"""


import json
import pika


# Sobrescrevendo a funcao de callback do pika
def callback(ch, method, properties, body):    
  tweet = json.loads(body.decode())
  print(tweet['text'])


# Consome da fila de tweets do topico "onepiece"
def onepieceQueue(channel):
  channel.basic_consume(queue='onepiece', auto_ack=True, on_message_callback=callback)
  channel.start_consuming()

  
# Consome da fila de tweets do topico "bleach"
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

  # Interface para informar quais tweets o cliente deseja receber
  print("Receber tweets digite:")
  print("1 - One Piece")
  print("2 - Bleach")
  print("3 - Ambos")

  # Recebe a opcao que o cliente selecionou
  option = input()

  # Dado a opcao selecionada, invoca as funcoes para consumir os tweets
  if option == '1':
    onepieceQueue(channel)
  if option == '2':
    bleachQueue(channel)
  if option == '3':
    onepieceQueue(channel)
    bleachQueue(channel)


if __name__ == '__main__':
  run()
