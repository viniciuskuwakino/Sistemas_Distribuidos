"""
  - Descrição: Parte do Cliente.
    Fazer um sistema de upload de arquivos via UDP. Um servidor UDP deverá receber as partes dos arquivos
    (1024 bytes), verificar ao final a integridade via um checksum (SHA-1) e armazenar o arquivo em uma pasta padrão.

  - Autores:
    Matheus Henrique Sechineli
    Vinicius Kuwakino

  - Data de criação: 16/04/2022
  - Data de atualização: 27/04/2022
"""

import os.path
import socket
import hashlib


def main():
    # AF_INET é o protocolo de endereço IP
    # SOCK_DGRAM utiliza o socket UDP
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:

        while True:
            msgClient = input("Informe o nome do arquivo para Upload:")

            # Sai do while se a mensagem for "EXIT"
            if msgClient == "EXIT":
                break

            # Obtem-se o caminho do arquivo
            path, _ = os.path.split(os.path.abspath(msgClient))
            path = path + "/teste/" + msgClient

            # Confere se o arquivo existe
            if os.path.exists(path):
                break
            else:
                print("Arquivo nao existe")

        # Converte a mensagem em Bytes
        msgBytes = msgClient.encode("utf-8")
        client.sendto(msgBytes, ("localhost", 20000))

        if msgClient == "EXIT":
            break

        # Tamanho em Bytes do arquivo
        tamanhoBytes = os.path.getsize(path)
        client.sendto(str(tamanhoBytes).encode("utf-8"), ("localhost", 20000))

        # Bytearray 
        ba = bytearray()
        
        # "r" -> read, "b" Bytes
        # Envia o arquivo em Bytes para o servidor
        with open(path, "rb") as arquivo:
            
            # Se o arquivo for menor que 1024 Bytes
            if tamanhoBytes < 1024:
                
                # Pega byte a byte e da push no bytearray
                for b in arquivo.read():
                    ba.append(b)

                # Envia o bytearray para o servidor
                client.sendto(ba, ("localhost", 20000))

            # Se o arquivo for maior que 1024 Bytes
            else:
                
                # Pega byte a byte e da push no Bytes
                for b in arquivo.read():
                    ba.append(b)
                    
                    # Quando o bytearray tiver 1023 Bytes,
                    # envia para o bytearray para o servidor e
                    # limpa o bytearray
                    if len(ba) > 1023:
                        client.sendto(ba, ("localhost", 20000))
                        ba.clear()

                # Se ainda tiver Bytes no bytearray, entao
                # envia o bytearray com os Bytes restantes 
                # para o servidor e limpa o bytearray
                if len(ba) > 0:
                    client.sendto(ba, ("localhost", 20000))
                    ba.clear()
            
            arquivo.close()

        # "r" -> read, "b" bytes
        # Checksum
        with open(path, "rb") as arquivo:
            dados = arquivo.read()
            sha1 = hashlib.sha1(dados).hexdigest()

            # Envia para o servidor o checksum do arquivo
            client.sendto(sha1.encode("utf-8"), ("localhost", 20000))

            arquivo.close()

    client.close()


if __name__ == '__main__':
    main()
