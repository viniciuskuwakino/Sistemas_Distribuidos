package Questao2;

enum TCPProtocol {

    TCPProtocol() {};

    /**
     * Enum "RequisitionType" para os tipos de requisição.
     *
     * @see RequisitionType#REQ
     * @see RequisitionType#RES
     */
    public enum RequisitionType {
        REQ(1), RES(2);

        public int number;

        /**
         * Construtor "RequisitionType" para armazenar o valor do tipo de requisição.
         *
         * @param valor Valor da requisição.
         */
        RequisitionType(int valor) {
            number = valor;
        }
    }

    /**
     * Enum "CommandIdentifier" para os comandos de manipulação de arquivos.
     *
     * @see CommandIdentifier#ADDFILE
     * @see CommandIdentifier#DELETE
     * @see CommandIdentifier#GETFILESLIST
     * @see CommandIdentifier#GETFILE
     */
    public enum CommandIdentifier {
        ADDFILE(1), DELETE(2), GETFILESLIST(3), GETFILE(4);

        public int number;

        /**
         * Construtor "CommandIdentifier" para armazenar o valor do comando.
         *
         * @param valor Valor do comando.
         */
        CommandIdentifier(int valor) {
            number = valor;
        }
    }

    /**
     * Enum "StatusCode" para os status do protocolo.
     *
     * @see StatusCode#SUCCESS
     * @see StatusCode#ERROR
     */
    public enum StatusCode {
        SUCCESS(1), ERROR(2);

        public int number;

        /**
         * Construtor "StatusCode" para armazenar o valor do protocolo.
         *
         * @param valor Valor do protocolo.
         */
        StatusCode(int valor) {
            number = valor;
        }
    }
}
