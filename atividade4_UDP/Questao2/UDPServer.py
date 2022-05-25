"""
  - Descrição: Parte do Servidor.
    Fazer um sistema de upload de arquivos via UDP. Um servidor UDP deverá receber as partes dos arquivos
    (1024 bytes), verificar ao final a integridade via um checksum (SHA-1) e armazenar o arquivo em uma pasta padrão.

  - Autores:
    Matheus Henrique Sechineli
    Vinicius Kuwakino

  - Data de criação: 16/04/2022
  - Data de atualização: 27/04/2022
"""

import socket
import os
import hashlib
import math


def main():
    # AF_INET é o protocolo de endereço IP
    # SOCK_DGRAM utiliza o socket UDP
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Conexão com o endereço IP e porta
    server.bind(("localhost", 20000))

    print("UDP Server está online!\n")

    while True:

        # Recebe os bytes do nome do arquivo
        msgBytes, _ = server.recvfrom(1024)

        # Decodifica de Bytes para String
        msgString = msgBytes.decode("utf-8")

        if msgString == "EXIT":
            print("Finalizando!")
            break

        # Cria diretorio "uploads" caso ele nao exista
        if not os.path.exists("uploads"):
            os.mkdir("uploads")

        # Recebe do cliente o tamanho do arquivo em Bytes
        tamBytes, _ = server.recvfrom(1024)

        # Obtem-se o caminho do arquivo
        path, _ = os.path.split(os.path.abspath(msgString))
        path = path + "/uploads/" + msgString

        # "w" -> write, "b" -> bytes
        with open(path, "wb") as arquivoBytes:

            # resto -> Para saber quantas vezes o cliente mandara o bytearray
            resto = int(tamBytes) / 1024
            
            # mod -> Para saber se o cliente mandara o bytearray com os bytes 
            # restantes do arquivo
            mod = int(tamBytes) % 1024
            
            contador = 0

            # Se o tamanho do arquivo for menor que 1024, recebe do cliente
            # o bytearray e escreve no novo arquivo
            if int(tamBytes) < 1024:
                arquivoDados, _ = server.recvfrom(1024)
                arquivoBytes.write(bytes(arquivoDados))
                
            else:
                
                # Recebe o bytearray do cliente e escreve no novo arquivo 
                while contador < math.floor(resto):
                    arquivoDados, _ = server.recvfrom(1024)

                    arquivoBytes.write(bytes(arquivoDados))
                    contador += 1
                    
                # Se tiver "mod", entao tem um bytearray com bytes,
                # desse modo, recebe do cliente o bytearray e escreve no
                # novo arquivo
                if mod:
                    arquivoDados, _ = server.recvfrom(1024)
                    arquivoBytes.write(bytes(arquivoDados))
                
            arquivoBytes.close()

        # Caminho do arquivo da pasta padrao
        defaultPath, _ = os.path.split(os.path.abspath(msgString))
        defaultPath = defaultPath + "/uploads/" + msgString

        # Verificar o checksum
        with open(defaultPath, "rb") as arquivo:
            dados = arquivo.read()
            checksumServidor = hashlib.sha1(dados).hexdigest()

            # Recebe os bytes do checksum
            checksumClient, _ = server.recvfrom(1024)

            # Decodifica de Bytes para String
            checksumClient = checksumClient.decode("utf-8")

            # Verifica o checksum
            if checksumServidor == checksumClient:
                print("Checksum verificado")
            else:
                print("Falha ao verificar Checksum!")

            arquivo.close()

    server.close()


if __name__ == '__main__':
    main()
