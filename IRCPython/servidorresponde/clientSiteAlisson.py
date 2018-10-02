# Importa a biblioteca para socket
import socket
# Defini o ip do host
ip = raw_input('digite o ip de conexao: ')
# Porta que o Servidor fica escutando
port = 7000
# Armazena o ip e a porta para a conexao
addr = ((ip,port))
# Armazena na variavel tcp. AF.NET defini a conexao IPV4 e SOCK_STREAM defini a conexao TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Realiza a conexao TCP/IP
client_socket.connect(addr)
# Enquanto as mensagens enviadas pelo cliente nao tiverem erro, continuara a enviar para o servidor
while True:
	mensagem = raw_input("digite uma mensagem para enviar ao servidor\n")
	client_socket.send(mensagem)
	print 'mensagem enviada'
# Tentativa de receber algo do servidor
print 'aguardando conexao do servidor'
raw_input("Aperte qualquer tecla para encerrar\n")
# Fecha a conexao do socket
client_socket.close()