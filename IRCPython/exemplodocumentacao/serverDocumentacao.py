# Importa a biblioteca para socket
import socket
# Defini o ip do host
HOST = ''
# Porta que o Servidor fica escutando
PORT = 50007
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conexao do servico TCP ao endereco de IP, como uma tupla
tcp.bind((HOST, PORT))
# Quantidade de conexoes suportadas
tcp.listen(1)
# con serve como o objeto da conexao e cliente serve como os dados da conexao
conn, addr = tcp.accept()
# Imprimi na tela os dados da conexao realizada
print 'Connected by', addr
# Enquanto 
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()