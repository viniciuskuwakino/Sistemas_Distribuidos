## Preparando o ambiente

Comando para instalar o gRPC no python:
```bash
$ python -m pip install grpcio
```

Comando gerar os codigos de marshalling e unmarshalling, e do gRPC:
```bash
$ sh buildPythonProto.sh
```

No diretório "servidor", executar o comando, para instalar as dependências:
```bash
$ yarn
```

## Executando o servidor

No diretório "servidor", para executar o servidor, utilizar o comando:
```bash
$ yarn start
```

## Executando o cliente

Comando para executar o cliente (executar no diretório do cliente):
```bash
$ python3 servico.py
```

## Exemplo de uso


* Terminal que está executando o cliente (teste da opção 1):
  ```bash
    1 - Inserir na tabela Matrícula;
    2 - Alterar notas na tabela Matrícula;
    3 - Alterar faltas na tabela Matrícula;
    4 - Listagem de alunos;
    5 - Boletim;
    Cliente: 5
  ```

* Preenchendo os dados:
  ```bash
    Informe o RA: 35
    Informe o ano: 2018
    Informe o semestre: 8
  ```

* Recebendo respota do servidor:
  ```bash
    ------------BOLETIM------------
    RA: 35
    Ano: 2018
    Semestre: 8
    ----------DISCIPlINAS----------
    Codigo: EL36I
    Nome: TERMODINÂMICA 2 (IG6A_CM)
    Professor: prof264
    Nota: 9.6
    Faltas: 7
    -------------------------------
    Codigo: EL37L
    Nome: INSTRUMENTAÇÃO INSDUSTRIAL E CONTROLE DE PROCESSOS (IG7A_CM)
    Professor: prof275
    Nota: 2.5
    Faltas: 3
    -------------------------------
    ------------BOLETIM------------
  ```