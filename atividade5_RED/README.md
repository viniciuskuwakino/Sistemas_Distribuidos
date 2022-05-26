Comando para executar o protoc do arquivo faculdade.proto:
```bash
$ sh buildProto.sh
```

__Importante__: Acessar o arquivo "Database.java" e na linha 6, alterar o caminho absoluto do banco de dados.

Comando para compilar e executar o servidor (estar no diretório do servidor/src):
```bash
$ sh buildRunServer.sh
```

Comando para executar o cliente (executar no diretório do cliente):
```bash
$ python3 servico.py
```

Exemplo de uso:

  * Terminal que está executando o cliente (teste da opção 1):
  ```bash
    1 - Inserir na tabela Matrícula;
    2 - Alterar notas na tabela Matrícula;
    3 - Alterar faltas na tabela Matrícula;
    4 - Listagem de alunos;
    5 - Boletim;
    Cliente: 1
  ```

  * Preenchendo os dados:

  ```bash
    Informe o RA:2020200
    Informe o codigo da disciplina:BCC33A
    Informe o ano:2022
    Informe o semestre:2
  ```

  * Recebendo respota do servidor:

  ```bash
    MENSAGEM:Success
  ```

  * Terminal que está executando o servidor (teste da opção 1):
  ```bash
    Inserido com sucesso!
  ```

