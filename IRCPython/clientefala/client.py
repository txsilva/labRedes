# Importa a biblioteca para socket
import socket
# Defini o ip do host
HOST = '127.0.0.1'
# Porta que o Servidor fica escutando
PORT = 5000
# Armazena na variavel tcp. AF.NET defini a conexao IPV4 e SOCK_STREAM defini a conexao TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Armazena o ip e a porta para a conexao
dest = (HOST, PORT)
# Realiza a conexao TCP/IP
tcp.connect(dest)
# Imprimi mensage para o cliente
print 'Para sair use CTRL+X\n'
# Armazena o input do que foi digitado no teclado na variavel
msg = raw_input()
# Enquando tem mensagem, o cliente faz o envio
while msg <> '\x18':
    tcp.send (msg)
    msg = raw_input()
tcp.close()