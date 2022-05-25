"""
  - Descrição:
    Fazer um chat P2P que possibilite os clientes trocarem mensagens entre si.
    As mensagens possuem o formato:
      - tipo de mensagem [1 byte]
      - tamanho apelido (tam_apl) [1 byte]
      - apelido [tam_apl (1 a 64) bytes ]
      - tamanho mensagem (tam_msg) [1 byte]
      - mensagem [tam_msg bytes]

    Os tipos de mensagem são:
      1: mensagem normal
      2: emoji
      3: URL
      4: ECHO (envia e recebe a mesma mensagem para indicar que usuário está ativo)

  - Autores:
    Matheus Henrique Sechineli
    Vinicius Kuwakino

  - Data de criação: 16/04/2022
  - Data de atualização: 27/04/2022
"""

import socket
import threading


# Função que retorna os campos do protocolo
def parseDatagram(data):
    messageType = int(data[0])
    nicknameSize = data[1]
    nickname = data[2:nicknameSize + 2]
    messageSize = data[nicknameSize + 2]
    message = data[nicknameSize + 3:nicknameSize + messageSize + 3]

    return (messageType, nicknameSize, nickname, messageSize, message)


# Cores para colorir o print
class bold_color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# Recebe a mensagem UDP e print no terminal com base no tipo.
def receiveUDPThread(socket):
    while (1):
        data, address = socket.recvfrom(1024)
        (messageType, nicknameSize, nickname, messageSize, message) = parseDatagram(data=data)

        # Mensagem normal = 1
        # Emoji = 2
        # URL = 3
        # ECHO = 4
        if messageType == 1:
            print(bold_color.BLUE + str(nickname.decode('UTF-8')) + '-' + bold_color.END + bold_color.RED + str(
                messageType) + bold_color.END + ':' + str(message.decode('UTF-8')))
        elif messageType == 2:
            print(bold_color.BLUE + str(nickname.decode('UTF-8')) + '-' + bold_color.END + bold_color.RED + str(
                messageType) + bold_color.END + ':' + str(message.decode('UTF-8')))
        elif messageType == 3:
            print(bold_color.BLUE + str(nickname.decode('UTF-8')) + '-' + bold_color.END + bold_color.RED + str(
                messageType) + bold_color.END + ':' + bold_color.UNDERLINE + str(
                message.decode('UTF-8')) + bold_color.END)
        elif messageType == 4:
            byteArray = bytearray(data)
            # Manda a mensagem como tipo normal
            byteArray[0] = 1
            socket.sendto(byteArray, address)


def main():
    # Captura informações da porta da aplicação e de destino
    print(bold_color.GREEN + "BEM VINDO AO CHAT UDP P2P" + bold_color.END)
    print(bold_color.CYAN + "DIGITE UMA PORTA PARA A APLICAÇÃO: " + bold_color.END)

    # Endereço IP
    localIP = "127.0.0.1"

    # AF_INET é o protocolo de endereço IP
    # SOCK_DGRAM utiliza o socket UDP
    socketUDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # "port" recebe a porta que será utilizada para a comunicação
    port = int(input())

    # Conexao passando o endereço IP e a porta
    socketUDP.bind((localIP, port))

    # "sendPort" recebe a porta destino
    print(bold_color.CYAN + "DIGITE UMA PORTA DE DESTINO: " + bold_color.END)
    sendPort = int(input())

    t = threading.Thread(target=receiveUDPThread, args=(socketUDP,), daemon=True)
    t.start()

    # Recebe o apelido que será usado no chat
    print(bold_color.GREEN + "DIGITE SEU APELIDO: " + bold_color.END)
    nickname = input()

    # Loop para captura de mensagens
    while (True):
        try:
            print(bold_color.RED + "SELECIONE O TIPO DE MENSAGEM: " + bold_color.END)
            print(bold_color.GREEN + "1 - MENSAGEM NORMAL" + bold_color.END)
            print(bold_color.CYAN + "2 - EMOJI" + bold_color.END)
            print(bold_color.YELLOW + "3 - URL" + bold_color.END)
            print(bold_color.DARKCYAN + "4 - ECHO" + bold_color.END)
            print(bold_color.PURPLE + "5 - EXIT" + bold_color.END)

            # Tipo de mensagem
            typeMessage = int(input())

            if typeMessage == 5:
                break
            if typeMessage > 5 or typeMessage < 1:
                raise Exception("Opção não encontrada")

            # Mensagem que sera enviada
            print("DIGITE A MENSAGEM: ")
            message = input()

            # "protocolo" contem um byte array, que recebera os dados do protocolo:
            # tipo de mensagem, tamanho do apelido, apelido, tamanho da mensagem e
            # mensagem.
            protocolo = bytearray(0)

            # Monta a mensagem com ajuda do byteArray colocando uma informação na frente da outra
            protocolo.append(typeMessage)
            nicknameBytes = nickname.encode()
            protocolo.append(len(nicknameBytes))
            for byte in nicknameBytes: protocolo.append(byte)
            messageBytes = message.encode()
            protocolo.append(len(messageBytes))
            for byte in messageBytes: protocolo.append(byte)

            # Envia os bytes do byteArray
            socketUDP.sendto(bytes(protocolo), (localIP, sendPort))
        except:
            # Erro de tipo de mensagem
            print(bold_color.RED + "Algo deu errado, tente novamente..." + bold_color.END)
            continue

    exit()


main()
