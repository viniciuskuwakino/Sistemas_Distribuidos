/**
 * Descrição: Faça uma aplicação (parte do cliente) com um servidor que gerencia um
 * conjunto de arquivos remotos entre múltiplos usuários. O servidor deve responder
 * aos seguintes comandos:
 * -> ADDFILE (1): adiciona um arquivo novo.
 * -> DELETE (2): remove um arquivo existente.
 * -> GETFILESLIST (3): retorna uma lista com o nome dos arquivos.
 * -> GETFILE (4): faz download de um arquivo.
 *
 * @author Matheus Henrique Sechineli
 * @author Vinicius Kuwakino
 *
 * Data de criação: 10/04/2022
 * Data de atualização: 13/04/2022
 */

package Questao2;

import java.io.*;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;
import java.util.logging.FileHandler;
import java.util.logging.Logger;

/**
 * Classe ClientThread: Thread responsável pela comunicação
 * Descrição: Recebe um socket, cria os objetos de leitura e escrita,
 * aguarda msgs clientes e responde com a msg dos comandos:
 * ADDFILE, DELETE, GETFILESLIST e GETFILE.
 */

public class TCPClient {

  private final static Logger logs = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

  private static void setupLogger () {
    try {
      FileHandler logsFile = new FileHandler("logFile.log");
      logs.addHandler(logsFile);

    } catch (Exception e) {
      logs.info("Logs nao estao funcionando." + e);
    }
  }

  public static void main(String[] args) {

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

      /* protocolo de comunicação */
      while (true) {
        System.out.print("Mensagem: ");
        buffer = reader.nextLine(); // lê mensagem via teclado

        int requisitionType = TCPProtocol.RequisitionType.REQ.number;

        byte requisitionTypeByte = (byte) requisitionType;
        out.writeByte(requisitionTypeByte); // Envia o byte do tipo de requisição

        String[] comandoSplit = buffer.trim().split(" ");

        TCPProtocol.CommandIdentifier comando = TCPProtocol.CommandIdentifier.valueOf(comandoSplit[0]);
        System.out.println("COMANDO: " + comando);

        byte comandoByte = (byte) comando.number;

        out.writeByte(comandoByte); // Envia o byte do comando

        if (comando.number != 3) {

          byte[] nomeArquivoBytes = comandoSplit[1].getBytes();
          byte tamanhoNomeByte = (byte) comandoSplit[1].length();

          out.writeByte(tamanhoNomeByte); // Envia os bytes do tamanho do nome do arquivo

          for (int i = 0; i < nomeArquivoBytes.length; i++) {
            out.writeByte(nomeArquivoBytes[i]); // Envia os bytes do nome do arquivo
          }
        }

        if (buffer.equals("PARAR"))
          break;

        byte msgType = in.readByte();
        byte commandIdent = in.readByte();
        byte statusCode = in.readByte();

        // ADDFILE
        if (comando.number == 1) {
          System.out.println("msgType: " + msgType);
          System.out.println("commandIdent: " + commandIdent);
          System.out.println("statusCode: " + statusCode);
        }

        // DELETE
        if (comando.number == 2) {
          System.out.println("msgType: " + msgType);
          System.out.println("commandIdent: " + commandIdent);
          System.out.println("statusCode: " + statusCode);
        }
        
        // GETFILESLIST
        if (comando.number == 3) {
          byte numArquivos = in.readByte();

          System.out.println("msgType: " + msgType);
          System.out.println("commandIdent: " + commandIdent);
          System.out.println("statusCode: " + statusCode);
          System.out.println("Numero de arquivos: " + numArquivos);

          for (int i = 0 ; i < numArquivos; i++) {
            byte bytesArq = in.readByte();

            System.out.println("Tamanho do nome do arquivo: " + bytesArq);
            byte[] arr_arq = new byte[bytesArq];

            for (int j = 0 ; j < bytesArq ; j++) {
              arr_arq[j] = in.readByte();
            }

            String arquivo = new String(arr_arq);
            System.out.println("Nome do arquivo: " + arquivo);
          }
        }

        // GETFILE
        if (comando.number == 4) {
          File downloadsFile = new File("src/Questao2/downloads");

          if (!downloadsFile.exists()) {
            downloadsFile.mkdirs();
          }

          byte tamanhoArquivo = in.readByte();
          byte[] arrArqDownload = new byte[tamanhoArquivo];

          System.out.println("msgType: " + msgType);
          System.out.println("commandIdent: " + commandIdent);
          System.out.println("statusCode: " + statusCode);
          System.out.println("tamanho do arquivo: " + tamanhoArquivo);

          for (int i = 0 ; i < tamanhoArquivo ; i++) {
            arrArqDownload[i] = in.readByte();
          }

          byte[] nomeArquivoBytes = comandoSplit[1].getBytes();
          String nomeArquivo = new String(nomeArquivoBytes, StandardCharsets.UTF_8);
          Path path = Paths.get(downloadsFile.getAbsolutePath() + "/" + nomeArquivo);
          Files.write(path, arrArqDownload);

        }

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
      }
    }
  } // main
} // class

