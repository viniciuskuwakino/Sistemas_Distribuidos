/**
 * Descrição: Faça um servidor (parte do cliente) para processar as seguintes
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
import java.io.IOException;
import java.math.BigInteger;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.security.MessageDigest;
import java.util.Scanner;

/**
 * Classe ClientThread: Thread responsável pela comunicação
 * Descrição: Recebe um socket, cria os objetos de leitura e escrita,
 * aguarda msgs clientes e responde com a msg dos comandos:
 * CONNECT user,password; PWD; CHDIR path; GETFILES; GETDIRS; EXIT.
 */

public class TCPClient {

  /**
   * Método "getSHA512" para obter o password criptografado.
   *
   * @param password Password que será criptografado.
   * @return Retorna uma String do password criptografado.
   */
  static String getSHA512(String password) {
    String toReturn = null;
    try {
      MessageDigest digest = MessageDigest.getInstance("SHA-512");
      digest.reset();
      digest.update(password.getBytes("utf8"));
      toReturn = String.format("%0128x", new BigInteger(1, digest.digest()));
    } catch (Exception e) {
      e.printStackTrace();
    }

    return toReturn;
  }
  /**
   * Método "main" realizará a conexão com o servidor, em seguida no primeiro
   * laço de repetição, temos o login, e em seguida no segundo laço de
   * repetição, temos a parte em que o cliente mandará os comandos que
   * deseja realizar, como: PWD, CHDIR, GETFILES, GETDIRS e EXIT.
   *
   * @param args Mensagem do cliente.
   */
  public static void main(String args[]) {
    Socket clientSocket = null; // socket do cliente
    Scanner reader = new Scanner(System.in); // ler mensagens via teclado

    try {
      /* Endereço e porta do servidor */
      int serverPort = 6666;
      InetAddress serverAddr = InetAddress.getByName("127.0.0.1");
      String buffer = "";

      /* conecta com o servidor */
      clientSocket = new Socket(serverAddr, serverPort);

      /* cria objetos de leitura e escrita */
      DataInputStream in = new DataInputStream(clientSocket.getInputStream());
      DataOutputStream out = new DataOutputStream(clientSocket.getOutputStream());

      while (true) {
        System.out.println("CONNECT user,password");
        buffer = reader.nextLine(); // lê mensagem via teclado

        String[] command = buffer.split(" ");
        String[] userPassword = command[1].split(",");

        String passwordHash = getSHA512(userPassword[1]);

        out.writeUTF(command[0] + " " + userPassword[0] + "," + passwordHash); // envia a mensagem para o servidor

        buffer = "";

        buffer = in.readUTF(); // aguarda resposta "do servidor

        if (buffer.equals("SUCCESS")) {
          System.out.println("Conectado!");
          break;
        } else {
          System.out.println("Usuário ou senha incorretos.");
        }

        buffer = "";

      }

      /* protocolo de comunicação */
      while (true) {
        System.out.print("Mensagem: ");
        buffer = reader.nextLine(); // lê mensagem via teclado

        out.writeUTF(buffer); // envia a mensagem para o servidor

        if (buffer.equals("PARAR"))
          break;

        buffer = in.readUTF(); // aguarda resposta "do servidor
        System.out.println("Server disse: " + buffer);
      }
    } catch (UnknownHostException ue) {
      System.out.println("Socket:" + ue.getMessage());
    } catch (EOFException eofe) {
      System.out.println("EOF:" + eofe.getMessage());
    } catch (IOException ioe) {
      System.out.println("IO:" + ioe.getMessage());
    } finally {
      try {
        clientSocket.close();
      } catch (IOException ioe) {
        System.out.println("IO: " + ioe);
        ;
      }
    }
  } // main
} // class
