#!/usr/bin/python
# Coded by: Alisson Machado
# Contact: alisson.machado@responsus.com.br
#

import socket
ip = raw_input('digite o ip de conexao: ')
port = 7000
addr = ((ip,port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)
while True:
	mensagem = raw_input("digite uma mensagem para enviar ao servidor\n")
	client_socket.send(mensagem)
	print 'mensagem enviada'
print 'aguardando conexao do servidor'
raw_input("Aperte qualquer tecla para encerrar\n")
client_socket.close()