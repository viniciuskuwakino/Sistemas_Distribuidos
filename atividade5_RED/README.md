protoc --java_out=servidor/src faculdade.proto
protoc --python_out=cliente/ faculdade.proto

* Executar no diretório: servidor
javac -cp .:protobuf-java-3.13.0.jar *.java
java -cp .:protobuf-java-3.13.0.jar ServerTcpFacul 
java -cp .:protobuf-java-3.13.0.jar:sqlite-jdbc-3.38.1.jar ServerTcpFacul

* Executar no diretório: cliente
python3 servico.py