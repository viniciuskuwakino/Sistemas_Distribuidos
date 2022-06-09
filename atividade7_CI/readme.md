## Ambiente
É necessário ter instalado o rabbitMQ.

## Executando o coletor 

Comando para executar o coletor:
```bash
$ python3 collector.py
```

## Executando o servidor

Comando para executar o servidor:
```bash
$ python3 server.py
```

## Executando o cliente 

Comando para executar o cliente:
```bash
$ python3 client.py
```

## Exemplo de uso


* Terminal que está executando o coletor:
  ```bash
    [x] Enviando Tweet!
    [x] Enviando Tweet!
    [x] Enviando Tweet!
  ```

* Terminal que está executando o servidor:
  ```bash
    [*] Tweet recebido!
    [x] Enviando tweet para fila!
    [*] Tweet recebido!
    [x] Enviando tweet para fila!
    [*] Tweet recebido!
    [x] Enviando tweet para fila!
  ```

* Terminal que está executando o cliente:
  ```bash
    Receber tweets digite:
    1 - One Piece
    2 - Bleach
    3 - Ambos
    Opcao: 1
  ```

* Resultado:
  ```bash
    ================================  Topic: One Piece  ================================
    Created_at: Tue Jun 07 11:56:11 +0000 2022
    Username: THA GUY
    Text: I've read this manga multiple times! You should check it out, too!
    
    #ONEPIECE #eurekaseven #Anipoke… https://t.co/xHP0u1dunt
    ====================================================================================
    Created_at: Tue Jun 07 11:55:13 +0000 2022
    Username: slothfulwaffle
    Text: #ONEPIECE 
    Oda really saw that Hunter x Hunter and Berserk was coming back from hiatus and said "My time has come"… https://t.co/nXzRXZHUBv
    ====================================================================================
    Created_at: Tue Jun 07 11:52:59 +0000 2022
    Username: Nitin D insaa
    Text: If law was a part of whitebeard's crew.
    #Onepiece https://t.co/4aocyW27DX
    ====================================================================================
  ```