/**
 * Descrição: O serviço será gerenciado em um servidor que receberá as informações via TCP.
 * O serviço deverá prover as seguintes funcionalidades remotas:
 * 1 - Inserção na tabela Matricula (notas e faltas são inseridas com valor padrão 0).
 * 2 - Alteração notas na tabela Matricula.
 * 3 - Alteração faltas na tabela Matricula.
 * 4 - Listagem de alunos (RA, nome, período) de uma disciplina informado a disciplina, ano e semestre.
 * 5 - Listagem de disciplinas, faltas e notas (RA, nome, nota, faltas) de um aluno informado o ano e semestre.
 *
 * @author Matheus Henrique Sechineli
 * @author Vinicius Kuwakino
 *
 * Data de criação: 08/05/2022
 * Data de atualização: 25/05/2022
 *
 * */

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.EOFException;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.sql.ResultSet;
import java.sql.SQLException;

/**
 * ServerTcpFacul: Servidor para conexao TCP com Threads.
 * Descricao: Recebe uma conexao, cria uma thread, recebe uma mensagem
 * e finaliza a conexao.
 */

public class ServerTcpFacul {

    private static Database database;

    static {
        try {
            database = new Database();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    public ServerTcpFacul() throws SQLException {
    }

    public static void main(String args[]) {

        try {
            int serverPort = 7000; // porta do servidor

            /* cria um socket e mapeia a porta para aguardar conexao */
            ServerSocket listenSocket = new ServerSocket(serverPort);

            while (true) {
                System.out.println("Servidor aguardando conexao ...");

                /* aguarda conexoes */
                Socket clientSocket = listenSocket.accept();

                System.out.println("Cliente conectado ... Criando thread ...");

                /* cria um thread para atender a conexao */
                ClientThread c = new ClientThread(clientSocket, database);

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
 */
class ClientThread extends Thread {

    ServerSocket listenSocket;
    DataInputStream inClient;
    DataOutputStream outClient;
    Socket clientSocket;
    Database database;

    public ClientThread(Socket clientSocket, Database database) {
        try {
            this.database = database;
            this.clientSocket = clientSocket;
            inClient = new DataInputStream(clientSocket.getInputStream());
            outClient = new DataOutputStream(clientSocket.getOutputStream());
        } catch (IOException ioe) {
            System.out.println("Connection:" + ioe.getMessage());
        } // catch
    } // construtor

    /**
     * Cria uma nova matrícula e retorna para o cliente uma resposta da operação realizada.
     */
    public void inserirMatricula() throws IOException {
        Faculdade.Resposta res = null;
        boolean db_operacao = false;

        // Recebe o array de bytes dos dados da matrícula
        String valueStr = inClient.readLine();
        int sizeBuffer = Integer.valueOf(valueStr);
        byte[] buffer = new byte[sizeBuffer];
        inClient.read(buffer);

        // Parser do buffer
        Faculdade.Matricula matricula = Faculdade.Matricula.parseFrom(buffer);

        // Executa a operação de inserir matrícula e retorna um boleano
        db_operacao = this.database.insertMatricula(
                matricula.getRa(),
                matricula.getCodDisciplina(),
                matricula.getAno(),
                matricula.getSemestre()
        );

        // Faz um marshalling da resposta, dependendo do valor boleano em "db_operacao"
        if (db_operacao) {
            res = Faculdade.Resposta.newBuilder().setMensagem("Success").build();
        } else {
            res = Faculdade.Resposta.newBuilder().setMensagem("Fail").build();
        }

        // Envia para o cliente um array de bytes da resposta
        outClient.write(res.toByteArray());
    }

    /**
     * Altera as notas de um aluno e retorna para o cliente uma resposta da operação realizada.
     */
    public void alterarNotas() throws IOException {
        Faculdade.Resposta res = null;
        boolean db_operacao = false;

        // Recebe o array de bytes dos dados da matrícula
        String valueStr = inClient.readLine();
        int sizeBuffer = Integer.valueOf(valueStr);
        byte[] buffer = new byte[sizeBuffer];
        inClient.read(buffer);

        // Parser do buffer
        Faculdade.Matricula matricula = Faculdade.Matricula.parseFrom(buffer);

        // Executa a operação de atualizar notas de uma matrícula e retorna um boleano
        db_operacao = this.database.updateNotaMatricula(
                matricula.getRa(),
                matricula.getCodDisciplina(),
                matricula.getAno(),
                matricula.getSemestre(),
                matricula.getNota()
        );

        // Faz um marshalling da resposta, dependendo do valor boleano em "db_operacao"
        if (db_operacao) {
            res = Faculdade.Resposta.newBuilder().setMensagem("Success").build();
        } else {
            res = Faculdade.Resposta.newBuilder().setMensagem("Fail").build();
        }

        // Envia para o cliente um array de bytes da resposta
        outClient.write(res.toByteArray());
    }

    /**
     * Altera as faltas de um aluno e retorna para o cliente uma resposta da operação realizada.
     */
    public void alterarFaltas() throws IOException {
        Faculdade.Resposta res = null;
        boolean db_operacao = false;

        // Recebe o array de bytes dos dados da matrícula
        String valueStr = inClient.readLine();
        int sizeBuffer = Integer.valueOf(valueStr);
        byte[] buffer = new byte[sizeBuffer];
        inClient.read(buffer);

        // Parser do buffer
        Faculdade.Matricula matricula = Faculdade.Matricula.parseFrom(buffer);

        // Executa a operação de atualizar faltas de uma matrícula e retorna um boleano
        db_operacao = this.database.updateFaltasMatricula(
                matricula.getRa(),
                matricula.getCodDisciplina(),
                matricula.getAno(),
                matricula.getSemestre(),
                matricula.getFaltas()
        );

        // Faz um marshalling da resposta, dependendo do valor boleano em "db_operacao"
        if (db_operacao) {
            res = Faculdade.Resposta.newBuilder().setMensagem("Success").build();
        } else {
            res = Faculdade.Resposta.newBuilder().setMensagem("Fail").build();
        }

        // Envia para o cliente um array de bytes da resposta
        outClient.write(res.toByteArray());
    }

    /**
     * Lista os alunos de uma disciplina e retorna-os para o cliente.
     */
    public void listarAlunos() throws IOException, SQLException {
        Faculdade.Resposta res = null;

        // Recebe o array de bytes dos dados da matrícula
        String valueStr = inClient.readLine();
        int sizeBuffer = Integer.valueOf(valueStr);
        byte[] buffer = new byte[sizeBuffer];
        inClient.read(buffer);

        // Parser do buffer
        Faculdade.Matricula matricula = Faculdade.Matricula.parseFrom(buffer);

        // Chama a funcao de listar alunos matriculados de uma disciplina
        this.database.listarAlunosDaDisciplina(
                matricula.getCodDisciplina(),
                matricula.getAno(),
                matricula.getSemestre(),
                outClient
        );
    }

    /**
     * Mostra o boletim de um aluno
     */
    public void boletimAluno() throws IOException, SQLException {
        Faculdade.Resposta res = null;

        // Recebe o array de bytes dos dados da matrícula
        String valueStr = inClient.readLine();
        int sizeBuffer = Integer.valueOf(valueStr);
        byte[] buffer = new byte[sizeBuffer];
        inClient.read(buffer);

        // Parser do buffer
        Faculdade.Matricula matricula = Faculdade.Matricula.parseFrom(buffer);

        // Chama a funcao de mostrar o boletim de um aluno
        this.database.boletimAluno(
                matricula.getRa(),
                matricula.getAno(),
                matricula.getSemestre(),
                outClient
        );
    }

    /* metodo executado ao iniciar a thread - start() */
    @Override
    public void run() {
        try {
            while (true) {
                String valueStr = inClient.readLine();
                int sizeBuffer = Integer.valueOf(valueStr);

                byte[] buffer = new byte[sizeBuffer];
                inClient.read(buffer);

                Faculdade.Op op = Faculdade.Op.parseFrom(buffer);

                switch (op.getTipo()) {
                    case 1:
                        inserirMatricula();
                        break;

                    case 2:
                        alterarNotas();
                        break;

                    case 3:
                        alterarFaltas();
                        break;

                    case 4:
                        try {
                            listarAlunos();
                        } catch (SQLException e) {
                            throw new RuntimeException(e);
                        }
                        break;

                    case 5:
                        try {
                            boletimAluno();
                        } catch (SQLException e) {
                            throw new RuntimeException(e);
                        }
                        break;

                    default:
                        System.out.println("Erro na operacao!");
                        break;
                }
            }

        } catch (EOFException eofe) {
            System.out.println("EOF: " + eofe.getMessage());
        } catch (IOException ioe) {
            System.out.println("IOE: " + ioe.getMessage());
        } finally {
            try {
                inClient.close();
                outClient.close();
                clientSocket.close();
            } catch (IOException ioe) {
                System.err.println("IOE: " + ioe);
            }
        }
        System.out.println("Thread comunicação cliente finalizada.");
    } // run
} // class
