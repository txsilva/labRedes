# Importa a biblioteca para socket
import socket
# Importa a biblioteca para modulo de dependencia do sistema operacional
import os
# Import a biblioteca para poder especificar parametros de sistema operacional
import sys
# Defini o ip do host
HOST = ''
# Porta que o Servidor fica escutando
PORT = 5000
# Armazena na variavel tcp. AF.NET defini a conexao IPV4 e SOCK_STREAM defini a conexao TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Armazena o ip e a porta para a conexao
orig = (HOST, PORT)
# Conexao do servico TCP ao endereco de IP, como uma tupla
tcp.bind(orig)
# Quantidade de conexoes suportadas
tcp.listen(1)
# Enquanto houver mensagem do cliente ou nenhum caracter estranho identificado
# o servidor ficara ouvindo a conexao, caso contrario a conexao sera fechada
while True:
    # con serve como o objeto da conexao e cliente serve como os dados da conexao
    con, cliente = tcp.accept()
    # fork e uma funao para replicar o processo, faz uma copia do programa e o executa como uma instancia
    pid = os.fork()
    if pid == 0:
        # Fecha os servicos TCP
        tcp.close()
        print 'Conectado por', cliente
        while True:
            # recv funciona para o saber o tamanho do buffer que sera lido por vez da mensagem do cliente
            msg = con.recv(1024)
            if not msg: break
            print cliente, msg
        print 'Finalizando conexao do cliente', cliente
        # Fecha a conexao com o objeto que veio com o TCP
        con.close()
        sys.exit(0)
    else:
        # Fecha a conexao com o objeto que veio com o TCPx
        con.close()