- Como executar:
    Execute os seguintes comando em terminais diferentes:
        python main.py

- Bibliotecas usadas:
    import socket       -> Para comunicação entre cliente e servido utilizando socket UDP.
    import threading    -> Para manipular threads

- Exemplo de uso:
    Execute o comando em dois terminais, como por exemplo:

        -> Terminal 1

        DIGITE UMA PORTA PARA A APLICAÇÃO:
        > 3001

        DIGITE UMA PORTA DE DESTINO:
        > 3002

        DIGITE SEU APELIDO:
        > Matheus Sechineli

        SELECIONE O TIPO DE MENSAGEM:
        1 - MENSAGEM NORMAL
        2 - EMOJI
        3 - URL
        4 - ECHO
        > 1

        DIGITE A MENSAGEM:
        > Quem é voce?
    
    E no outro terminal que estará executando o main também, informe o que se pede,
    
        -> Terminal 2

        DIGITE UMA PORTA PARA A APLICAÇÃO:
        > 3002

        DIGITE UMA PORTA DE DESTINO:
        > 3001

        DIGITE SEU APELIDO:
        > Zabuza Momochi

        SELECIONE O TIPO DE MENSAGEM:
        1 - MENSAGEM NORMAL
        2 - EMOJI
        3 - URL
        4 - ECHO
        > 1

        DIGITE A MENSAGEM:
        > Eu sou zabuza momochi o demonio da nevoa oculta
        
    
    E assim, teremos as saídas as devidas mensagens em cada terminal, que neste caso seria:
        Terminal 2:
            -> Matheus Sechineli-1:Quem é voce?

        Terminal 1:
            -> Zabuza Momochi-1:Eu sou zabuza momochi o demonio da nevoa oculta

