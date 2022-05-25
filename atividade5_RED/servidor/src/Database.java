import java.io.DataOutputStream;
import java.io.IOException;
import java.sql.*;

public class Database {
    private String url = "jdbc:sqlite:/home/vinicius/Documentos/bcc/semestre_6/SD/atividade5_red/atv/javacode/database/database_com_dados-contrib-Daniel-Farina.db";
    public Connection conn = DriverManager.getConnection(this.url);
    public Database() throws SQLException {
    }

    /**
     * Faz a inserção da matrícula no banco de dados.
     *
     * @param ra                ra da matrícula
     * @param cod_disciplina    cod_disciplina da matrícula
     * @param ano               ano da matrícula
     * @param semestre          semestre da matrícula
     *
     * @return "true" caso a operação foi executada, "false" caso não tenha executado com sucesso
     */
    public boolean insertMatricula(Integer ra, String cod_disciplina, Integer ano, Integer semestre) {

        String sql = "INSERT INTO Matricula (ra, cod_disciplina, ano, semestre, nota, faltas) VALUES (?,?,?,?,?,?);";
        boolean res = false;

        try{
            PreparedStatement pstmt = this.conn.prepareStatement(sql);
            pstmt.setInt(1, ra);
            pstmt.setString(2, cod_disciplina);
            pstmt.setInt(3, ano);
            pstmt.setInt(4, semestre);
            pstmt.setFloat(5, 0);
            pstmt.setInt(6, 0);

            pstmt.executeUpdate();

            System.out.println("Inserido com sucesso!");
            res = true;
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }

        return res;
        
    }

    /**
     * Faz uma verificação se a matrícula existe no banco de dados.
     * Caso exista, então faz a alteração da nota de uma matrícula no banco de dados.
     *
     * @param ra                ra da matrícula
     * @param cod_disciplina    cod_disciplina da matrícula
     * @param ano               ano da matrícula
     * @param semestre          semestre da matrícula
     * @param nota              nota da matrícula
     *
     * @return "true" caso a operação foi executada, "false" caso não tenha executado com sucesso
     */
    public boolean updateNotaMatricula(Integer ra, String cod_disciplina, Integer ano, Integer semestre, Float nota) {

        String sql_verify = "SELECT COUNT(*) AS num FROM Matricula WHERE ra = ? AND cod_disciplina = ? AND ano = ? AND semestre = ?;";
        boolean res = false;
        int num;

        try {
            Connection conn_verify = DriverManager.getConnection(url);
            PreparedStatement pstmt_verify = conn_verify.prepareStatement(sql_verify);
            pstmt_verify.setInt(1, ra);
            pstmt_verify.setString(2, cod_disciplina);
            pstmt_verify.setInt(3, ano);
            pstmt_verify.setInt(4, semestre);

            ResultSet result = pstmt_verify.executeQuery();
            num = result.getInt("num");

            conn_verify.close();

            if (num != 0) {
                String sql = "UPDATE Matricula SET nota = ? WHERE ra = ? AND cod_disciplina = ? AND ano = ? AND semestre = ?;";

                try {
//                    Connection conn = DriverManager.getConnection(url);
                    PreparedStatement pstmt = this.conn.prepareStatement(sql);

                    pstmt.setFloat(1, nota);
                    pstmt.setInt(2, ra);
                    pstmt.setString(3, cod_disciplina);
                    pstmt.setInt(4, ano);
                    pstmt.setInt(5, semestre);

                    pstmt.executeUpdate();
                    System.out.println("Alterado com sucesso!");
                    res = true;

                } catch (SQLException e) {
                    System.out.println(e.getMessage());
                }

            } else {
                System.out.println("Erro: Matricula nao existe!");
            }

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

        return res;


    }

    /**
     * Faz uma verificação se a matrícula existe no banco de dados.
     * Em seguida, faz a alteração das faltas de uma matrícula no banco de dados.
     *
     * @param ra                ra da matrícula
     * @param cod_disciplina    cod_disciplina da matrícula
     * @param ano               ano da matrícula
     * @param semestre          semestre da matrícula
     * @param faltas            faltas da matrícula
     *
     * @return "true" caso a operação foi executada, "false" caso não tenha executado com sucesso
     */
    public boolean updateFaltasMatricula(Integer ra, String cod_disciplina, Integer ano, Integer semestre, Integer faltas) {

        String sql_verify = "SELECT COUNT(*) AS num FROM Matricula WHERE ra = ? AND cod_disciplina = ? AND ano = ? AND semestre = ?;";
        boolean res = false;
        int num;

        try {
            Connection conn_verify = DriverManager.getConnection(url);
            PreparedStatement pstmt_verify = conn_verify.prepareStatement(sql_verify);
            pstmt_verify.setInt(1, ra);
            pstmt_verify.setString(2, cod_disciplina);
            pstmt_verify.setInt(3, ano);
            pstmt_verify.setInt(4, semestre);

            ResultSet result = pstmt_verify.executeQuery();
            num = result.getInt("num");

            conn_verify.close();

            if (num != 0) {
                String sql = "UPDATE Matricula SET faltas = ? WHERE ra = ? AND cod_disciplina = ? AND ano = ? AND semestre = ?;";

                try {
                    PreparedStatement pstmt = this.conn.prepareStatement(sql);
                    pstmt.setFloat(1, faltas);
                    pstmt.setInt(2, ra);
                    pstmt.setString(3, cod_disciplina);
                    pstmt.setInt(4, ano);
                    pstmt.setInt(5, semestre);

                    pstmt.executeUpdate();
                    System.out.println("Alterado com sucesso!");
                    res = true;
                } catch (SQLException e) {
                    System.out.println(e.getMessage());
                }
            } else {
                System.out.println("Erro: Matricula nao existe!");
            }

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

        return res;
    }

    /**
     * Conta quantos alunos estao matriculados numa disciplina dado a disciplina, ano e semestre.
     * Faz uma consulta dos alunos dado o codigo da disciplina, ano e semestre, e retorna os alunos para o cliente.
     *
     * @param cod_disciplina    cod_disciplina da matrícula
     * @param ano               ano da matrícula
     * @param semestre          semestre da matrícula
     * @param outClient         fluxo de saida de dados
     */
    public void listarAlunosDaDisciplina(String cod_disciplina, Integer ano, Integer semestre, DataOutputStream outClient) throws IOException {
        String sql_verify = "SELECT COUNT(ra) AS num FROM ALUNO WHERE ra = (" +
                "SELECT ra FROM Matricula WHERE cod_disciplina = ? AND ano = ? AND semestre = ?);";

        String sql = "SELECT ra, nome, periodo FROM ALUNO WHERE ra = (" +
                "SELECT ra FROM Matricula WHERE cod_disciplina = ? AND ano = ? AND semestre = ?);";

        int num;
        ResultSet result = null;

        try {
            Connection conn_verify = DriverManager.getConnection(url);
            PreparedStatement pstmt_verify = conn_verify.prepareStatement(sql_verify);

            pstmt_verify.setString(1, cod_disciplina);
            pstmt_verify.setInt(2, ano);
            pstmt_verify.setInt(3, semestre);

            ResultSet result_verify = pstmt_verify.executeQuery();
            num = result_verify.getInt("num");

            conn_verify.close();

            if (num != 0) {
                try {
                    PreparedStatement pstmt = this.conn.prepareStatement(sql);
                    pstmt.setString(1, cod_disciplina);
                    pstmt.setInt(2, ano);
                    pstmt.setInt(3, semestre);

                    result = pstmt.executeQuery();

                    Faculdade.Tamanho tam = Faculdade.Tamanho.newBuilder().setQuantidade(num).build();
                    outClient.write(tam.toByteArray());

                    while (result.next()) {
                        Faculdade.Aluno aluno = Faculdade.Aluno.newBuilder()
                                .setRa(result.getInt("ra"))
                                .setNome(result.getString("nome"))
                                .setPeriodo(result.getInt("periodo"))
                                .build();

                        outClient.write(aluno.toByteArray());
                    }
                } catch (SQLException e) {
                    System.out.println(e.getMessage());
                }

            } else {
                System.out.println("Erro: Nao ha alunos!");
            }

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

    }

    /**
     * Conta quantas disciplinas o aluno esta matriculado dado o ra, ano e semestre.
     * Faz uma consulta nas tabelas Disciplina e Matricula dado o ra, ano e semestre, e retorna os dados
     * das duas tabelas para o cliente.
     *
     * @param ra                ra da matrícula
     * @param ano               ano da matrícula
     * @param semestre          semestre da matrícula
     * @param outClient         fluxo de saida de dados
     */
    public void boletimAluno(Integer ra, Integer ano, Integer semestre, DataOutputStream outClient) throws IOException {
        String sql_verify = "SELECT count(*) as num FROM Disciplina, Matricula WHERE " +
                "Disciplina.codigo = Matricula.cod_disciplina AND ra = ? AND ano = ? AND semestre = ?;";

        String sql = "SELECT * FROM Disciplina, Matricula WHERE " +
                "Disciplina.codigo=Matricula.cod_disciplina AND ra = ? AND ano = ? AND semestre = ?;";

        int num;
        ResultSet result = null;

        try {
            Connection conn_verify = DriverManager.getConnection(url);
            PreparedStatement pstmt_verify = conn_verify.prepareStatement(sql_verify);

            pstmt_verify.setInt(1, ra);
            pstmt_verify.setInt(2, ano);
            pstmt_verify.setInt(3, semestre);

            ResultSet result_verify = pstmt_verify.executeQuery();
            num = result_verify.getInt("num");

            conn_verify.close();

            if (num != 0) {

                try {
                    PreparedStatement pstmt = this.conn.prepareStatement(sql);
                    pstmt.setInt(1, ra);
                    pstmt.setInt(2, ano);
                    pstmt.setInt(3, semestre);

                    result = pstmt.executeQuery();

                    Faculdade.Tamanho tam = Faculdade.Tamanho.newBuilder().setQuantidade(num).build();
                    outClient.write(tam.toByteArray());

                    while (result.next()) {
                        Faculdade.Matricula matricula = Faculdade.Matricula.newBuilder()
                                .setRa(result.getInt("ra"))
                                .setCodDisciplina(result.getString("cod_disciplina"))
                                .setFaltas(result.getInt("faltas"))
                                .setNota(result.getFloat("nota"))
                                .setAno(result.getInt("ano"))
                                .setSemestre(result.getInt("semestre"))
                                .build();

                        Faculdade.Disciplina disciplina = Faculdade.Disciplina.newBuilder()
                                .setCodigo(result.getString("codigo"))
                                .setNome(result.getString("nome"))
                                .setCodCurso(result.getInt("cod_curso"))
                                .setProfessor(result.getString("professor"))
                                .build();

                        outClient.write(matricula.toByteArray());
                        outClient.write(disciplina.toByteArray());
                    }

                } catch (SQLException e) {
                    System.out.println(e.getMessage());
                }

            } else {
                System.out.println("Erro: Matricula nao existe!");
            }

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

    }

}
