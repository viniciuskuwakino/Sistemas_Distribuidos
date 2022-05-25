/**
 * Descrição: Faça um servidor (parte do servidor) para processar as seguintes
 * mensagens dos clientes: CONNECT user,password; PWD; CHDIR path; GETFILES;
 * GETDIRS; EXIT. O servidor deve suportar mensagens de múltiplos clientes,
 * utilizando o TCP. As mensagens de solicitação estão no formato String UTF.
 *
 * @author Matheus Henrique Sechineli
 * @author Vinicius Kuwakino
 *
 * Data de criação: 06/04/2022
 * Data de atualização: 11/04/2022
 */

package Questao1;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.EOFException;
import java.io.File;
import java.io.IOException;
import java.math.BigInteger;
import java.net.ServerSocket;
import java.net.Socket;
import java.security.MessageDigest;
import java.util.ArrayList;
import java.util.List;

/**
 * TCPServer: Servidor para conexao TCP com Threads.
 * Descricao: Recebe uma conexao, cria uma thread, recebe uma mensagem
 * e finaliza a conexao.
 */

public class TCPServer {

  public static void main(String args[]) {

    try {
      int serverPort = 6666; // porta do servidor

      /* cria um socket e mapeia a porta para aguardar conexao */
      ServerSocket listenSocket = new ServerSocket(serverPort);

      while (true) {
        System.out.println("Servidor aguardando conexao ...");

        /* aguarda conexoes */
        Socket clientSocket = listenSocket.accept();

        System.out.println("Cliente conectado ... Criando thread ...");

        /* cria um thread para atender a conexao */
        ClientThread c = new ClientThread(clientSocket);

        /* inicializa a thread */
        c.start();
      } // while

    } catch (IOException e) {
      System.out.println("Listen socket:" + e.getMessage());
    } // catch
  } // main
} // class

/**
 * Classe ClientThread: Thread responsavel pela comunicacao
 * Descricao: Recebe um socket, cria os objetos de leitura e escrita,
 * aguarda msgs clientes e responde com a msg dos comandos:
 * CONNECT user,password; PWD; CHDIR path; GETFILES; GETDIRS; EXIT.
 */
class ClientThread extends Thread {

  DataInputStream in;
  DataOutputStream out;
  Socket clientSocket;

  public ClientThread(Socket clientSocket) {
    try {
      this.clientSocket = clientSocket;
      in = new DataInputStream(clientSocket.getInputStream());
      out = new DataOutputStream(clientSocket.getOutputStream());
    } catch (IOException ioe) {
      System.out.println("Connection:" + ioe.getMessage());
    } // catch
  } // construtor

  /* metodo executado ao iniciar a thread - start() */
  @Override
  public void run() {
    try {
      Comando c = new Comando();
      String buffer = "";
      while (true) {
        buffer = in.readUTF(); /* aguarda o envio de dados */

        // Variavel que recebe os dados do buffer
        String bufferClone = buffer;

        System.out.println("Cliente disse: " + buffer);

        // Armazena o comando que esta no buffer em letras minusculas
        c.setComando(buffer);

        // Split no clone do buffer para o funcionamento dos comandos: CONNECT e CHDIR
        String[] c_split = bufferClone.split(" ");

        if (c_split[0].equals("CONNECT"))
          buffer = c.connect();
        if (buffer.equals("PWD"))
          buffer = c.pwd();
        if (c_split[0].equals("CHDIR"))
          buffer = c.chdir();
        if (buffer.equals("GETFILES"))
          buffer = c.getfiles();
        if (buffer.equals("GETDIRS"))
          buffer = c.getdirs();
        if (buffer.equals("EXIT"))
          break;

        // Envia mensagem para o cliente
        out.writeUTF(buffer);
      }
    } catch (EOFException eofe) {
      System.out.println("EOF: " + eofe.getMessage());
    } catch (IOException ioe) {
      System.out.println("IOE: " + ioe.getMessage());
    } finally {
      try {
        in.close();
        out.close();
        clientSocket.close();
      } catch (IOException ioe) {
        System.err.println("IOE: " + ioe);
      }
    }
    System.out.println("Thread comunicação cliente finalizada.");
  } // run
} // class

/**
 * Classe Comando: Responsável pelo funcionamento dos comandos
 * Descrição: Recebe o comando contido no buffer e converte a String
 * em letras minúsculas; possui também os métodos dos comandos:
 * CONNECT, PWD, CHDIR, GETFILES e GETDIRS.
 */

class Comando {
  // Criação de lista de usuários
  List<TCPUser> arrayList = new ArrayList<TCPUser>();

  // Criação dos usuários: user e userAdmin
  TCPUser user = new TCPUser("user", "password");
  TCPUser userAdmin = new TCPUser("admin", "admin");

  // Lista de usuários
  TCPUser[] listUsers = { user, userAdmin };

  String comando;
  File file = new File("./");
  String rootPath = file.getAbsolutePath();

  // Construtor vazio
  public Comando() {}

  /**
   * Método "setComando" transforma a String que está no buffer
   * em letras minúsculas.
   *
   * @param comando Comando enviado pelo cliente.
   */
  public void setComando(String comando) {
    this.comando = comando.toLowerCase();
  }

  /**
   * Método "connect" verifica se o usuário existe e se a senha
   * deste usuário está correta.
   *
   * @return Retorna mensagem de SUCCESS caso o usuário exista
   * e a senha esteja correta, caso contrário retorna ERROR.
   */
  public String connect() {
    try {

      String[] comando_split = comando.split(" ");
      String[] userPassword = comando_split[1].split(",");

      for (int i = 0; i < listUsers.length; i++) {
        if (listUsers[i].login.equals(userPassword[0]))
          if (listUsers[i].comparePassword(userPassword[1]))
            return "SUCCESS";
      }

      return "ERROR";
    } catch (Exception e) {
      return "ERROR" + e;
    }
  }

  /**
   * Método "pwd" mostra o diretório absoluto corrente
   * desde a raíz do sistema.
   *
   * @return Retorna o diretório absoluto.
   */
  public String pwd() {
    try {

      String t = file.getAbsolutePath();

      return t;
    } catch (Exception e) {
      return "ERROR:" + e;
    }
  }

  /**
   * Método "chdir" altera o diretório corrente para
   * "path".
   *
   * @return Retorna uma String "SUCCESS" caso tenha
   * alterado o diretório corrente, ou caso contrário,
   * retorna "ERROR".
   */
  public String chdir() {
    try {
      // Processo que ira executar o comando "chdir"
      String[] comando_split = comando.split(" ");

      file = new File(comando_split[1]);

      if (!file.exists())
        throw new Exception("ERRO");

      return "SUCCESS";

    } catch (Exception e) {
      return "ERROR:" + e;
    }
  }

  /**
   * Método "getfiles" mostra os arquivos do diretório
   * corrente.
   *
   * @return Retorna uma String contendo a quantidade de
   * arquivos no diretório corrente, e em seguida retorna
   * cada arquivo.
   */
  public String getfiles() {
    try {

      File[] listOfFiles = file.listFiles();
      int num = 0;

      String res = new String("");

      for (int i = 0; i < listOfFiles.length; i++) {
        if (listOfFiles[i].isFile()) {
          res = res.concat(listOfFiles[i].getName() + "\n");
          num++;
        }
        ;
      }

      res = "Numero de arquivos: " + num + "\n" + res;

      return res;
    } catch (Exception e) {
      return "ERROR:" + e;
    }
  }

  /**
   * Método "getdirs" mostra os diretórios do diretório
   * corrente.
   *
   * @return Retorna uma String contendo o número de
   * diretórios do diretório corrente, e em seguida
   * retorna cada diretório.
   */
  public String getdirs() {
    try {

      File[] listOfFiles = file.listFiles();
      int num = 0;

      String res = new String("");

      for (int i = 0; i < listOfFiles.length; i++) {
        if (listOfFiles[i].isDirectory()) {
          res = res.concat(listOfFiles[i].getName() + "\n");
          num++;
        }

      }

      res = "Numero de diretórios: " + num + "\n" + res;

      return res;

    } catch (Exception e) {
      return "ERROR:" + e;
    }
  }

}

/**
 * Classe TCPUser: Responsável por criar os usuários e criptografar
 * as senhas com hash SHA-512.
 * Descrição: Cria um usuário com o login e password, e possui os
 * métodos de criptografia e de comparação de senhas.
 *
 * Descrição: Recebe o comando contido no buffer e converte a String
 * em letras minúsculas; possui também os métodos dos comandos:
 * CONNECT, PWD, CHDIR, GETFILES e GETDIRS.
 */

class TCPUser {
  String login;
  String password;

  /**
   * Construtor: contém login e password
   *
   * @param user Login do usuário
   * @param password Senha do usuário
   */
  public TCPUser(String user, String password) {
    this.login = user;
    this.password = password;
  }

  /**
   * Método "getSHA512" para obter o password criptografado.
   *
   * @return Retorna uma String do password criptografado.
   */
  public String getSHA512() {
    String toReturn = null;
    try {
      MessageDigest digest = MessageDigest.getInstance("SHA-512");
      digest.reset();
      digest.update(this.password.getBytes("utf8"));
      toReturn = String.format("%0128x", new BigInteger(1, digest.digest()));
    } catch (Exception e) {
      e.printStackTrace();
    }

    return toReturn;
  }

  /**
   * Método "comparePassword" que compara os passwords.
   *
   * @param password Password recebido pelo cliente.
   *
   * @return Retorna um Boolean, True caso os passwords sejam iguais,
   * e False caso não sejam.
   */
  public Boolean comparePassword(String password) {
    String passwordHash = getSHA512();
    return passwordHash.equals(password);
  }

}
