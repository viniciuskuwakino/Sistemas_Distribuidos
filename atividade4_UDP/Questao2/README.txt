- Como executar:
    Execute os seguintes comando em terminais diferentes:
        python UDPServer.py
        python UDPClient.py

- Bibliotecas usadas:
    import os       -> Para verificar arquivos existentes e obter os diretórios absolutos.
    import socket   -> Para comunicação entre cliente e servido utilizando socket UDP.
    import hashlib  -> Para obter fazer a verificação e integridade via um checksum (SHA-1).
    import math     -> Para utilizar o "floor" que arredonda para baixo um numero inteiro.

- Exemplo de uso:
    No terminal que estará executando o cliente, escolher algum arquivo na pasta teste, 
    como por exemplo:
        > rocklee.jpg
    
    E assim, teremos a imagem na pasta "uploads".