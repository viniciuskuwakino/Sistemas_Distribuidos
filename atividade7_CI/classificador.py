import pika
import json


# Sobrescrevendo a funcao de callback do pika
def callback(ch, method, properties, body):
    print("[x] Received %r" % body.decode())


def run():
    # Estabelecendo uma conexao com o servidor
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Criando uma fila de mensagens
    channel.queue_declare(queue='tweets')

    # Dizemos ao RabbitMQ que a funcao callback sobrescrita recebera as mensagens da fila "tweets"
    channel.basic_consume(queue='tweets', auto_ack=True, on_message_callback=callback)

    channel.start_consuming()


if __name__ == '__main__':
    run()
