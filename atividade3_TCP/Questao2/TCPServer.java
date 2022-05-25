/**
 * Descrição: Faça uma aplicação (parte do servidor) com um servidor que gerencia um
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
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;

/**
 * Classe TCPServer: Servidor para conexão TCP com Threads.
 * Descrição: Recebe uma conexão, cria uma thread, recebe uma mensagem
 * e finaliza a conexão.
 */


public class TCPServer {

  public static void main(String[] args) {

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
 * Classe ClientThread: Thread responsável pela comunicação
 * Descrição: Recebe um socket, cria os objetos de leitura e escrita,
 * aguarda msgs clientes e responde com a msg dos comandos:
 * ADDFILE, DELETE, GETFILESLIST e GETFILE.
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
    File defaultDir = new File("src/Questao2/files");

    if (!defaultDir.exists()) {
      defaultDir.mkdirs();
    }

    try {

      Comando c = new Comando();
      Byte[] buffer = new Byte[254];

      while (true) {
        Byte Requisition = in.readByte();
        System.out.println(Requisition);

        if (Requisition.intValue() == TCPProtocol.RequisitionType.REQ.number) {
          Byte comando = in.readByte();
          System.out.println(comando);
          int responseType = TCPProtocol.RequisitionType.RES.number;

          int status = 2;

          // GETFILESLIST
          if (comando.intValue() == TCPProtocol.CommandIdentifier.GETFILESLIST.number) {
            status = c.getFilesList(defaultDir);

            File[] listFiles = defaultDir.listFiles();

            out.writeByte((byte) responseType);
            out.writeByte(comando);
            out.writeByte((byte) status);
            out.writeByte((byte) listFiles.length);

            for (int i = 0 ; i < listFiles.length ; i++) {
              byte[] bytesFileName = listFiles[i].getName().getBytes();

              // Envia os bytes do arquivo
              out.writeByte((byte) bytesFileName.length);

              for (int j = 0 ; j < bytesFileName.length ; j++) {
                // Envia byte a byte
                out.writeByte(bytesFileName[j]);
              }
            }
          }

          Byte tamanhoNome = in.readByte();

          byte[] nome = new byte[tamanhoNome];
          for (int i = 0; i < tamanhoNome; i++) {
            nome[i] = in.readByte();
          }

          // ADDFILE
          if (comando.intValue() == TCPProtocol.CommandIdentifier.ADDFILE.number) {
            status = c.addFile(defaultDir, nome);

            out.writeByte((byte) responseType);
            out.writeByte(comando);
            out.writeByte((byte) status);
          }

          // DELETE
          if (comando.intValue() == TCPProtocol.CommandIdentifier.DELETE.number) {
            status = c.delete(defaultDir, nome);

            out.writeByte((byte) responseType);
            out.writeByte(comando);
            out.writeByte((byte) status);
          }

          // GETFILE
          if (comando.intValue() == TCPProtocol.CommandIdentifier.GETFILE.number) {
            status = c.getFile(defaultDir, nome);

            String nomeString = new String(nome, StandardCharsets.UTF_8);
            File arquivoDownload = new File(defaultDir.getAbsolutePath() + "/" + nomeString);

            out.writeByte((byte) responseType);
            out.writeByte(comando);
            out.writeByte((byte) status);

            byte[] bytesArquivo = Files.readAllBytes(Path.of(arquivoDownload.getAbsolutePath()));

            // Tamanho do arquivo em bytes
            out.writeByte((byte) bytesArquivo.length);

            for (int i = 0 ; i < bytesArquivo.length ; i++) {
              // Envia arquivo byte a byte
              out.writeByte(bytesArquivo[i]);
            }

          }
        }
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
 */

class Comando {

  public Comando() {}

  /**
   * Método "getFilesList" obtem-se a lista de arquivos.
   *
   * @param defaultDir Diretorio dos arquivos.
   *
   * @return TCPPROTOCOL
   */
  public int getFilesList(File defaultDir) {
    File[] listFiles = defaultDir.listFiles();

    return TCPProtocol.StatusCode.SUCCESS.number;
  }

  /**
   * Método "addFile" adiciona um novo arquivo.
   *
   * @param defaultDir Diretorio dos arquivos.
   * @param nome Nome em bytes.
   *
   * @return TCPPROTOCOL
   */
  public int addFile(File defaultDir, byte[] nome) {
    String nomeArquivo = new String(nome, StandardCharsets.UTF_8);
    File novoArquivo = new File(defaultDir.getAbsolutePath() + "/" + nomeArquivo);

    // Verifica se o arquivo ja existe, senao, cria arquivo
    if (!novoArquivo.exists()) {
      try {
        novoArquivo.createNewFile();
        return TCPProtocol.StatusCode.SUCCESS.number;
      } catch (IOException e) {
        System.out.println("Erro ao criar arquivo!");
      }
    }

    return TCPProtocol.StatusCode.ERROR.number;
  }

  /**
   * Método "delete" deleta um arquivo.
   *
   * @param defaultDir Diretorio dos arquivos.
   * @param nome Nome em bytes.
   *
   * @return TCPPROTOCOL
   */
  public int delete(File defaultDir, byte[] nome) {
    String nomeArquivo = new String(nome, StandardCharsets.UTF_8);
    File arquivo = new File(defaultDir.getAbsolutePath() + "/" + nomeArquivo);

    if (arquivo.exists()) {
      arquivo.delete();
      return TCPProtocol.StatusCode.SUCCESS.number;
    } else {
      System.out.println("Arquivo nao existe!");
      return TCPProtocol.StatusCode.ERROR.number;
    }

  }

  /**
   * Método "getFile" faz download de um arquivo.
   *
   * @param defaultDir Diretorio dos arquivos.
   * @param nome Nome em bytes.
   *
   * @return TCPPROTOCOL
   */
  public int getFile(File defaultDir, byte[] nome) {
    // Verifica se o arquivo existe
    String nomeArquivo = new String(nome, StandardCharsets.UTF_8);
    File arquivo = new File(defaultDir.getAbsolutePath() + "/" + nomeArquivo);

    if (arquivo.exists()) return TCPProtocol.StatusCode.SUCCESS.number;

    return TCPProtocol.StatusCode.ERROR.number;
  }

}
