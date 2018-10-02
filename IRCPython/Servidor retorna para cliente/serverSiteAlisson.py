#!/usr/bin/python 
# 
# Coded by: Alisson Machado
# Contact: alisson.machado@responsus.com.br
# servidor que recebe mensagens de aplicacao client parecido com o netsend
#
import socket
host = '127.0.0.1'
port = 7000
addr = (host,port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
	serv_socket.bind(addr)
	serv_socket.listen(3)
	print 'Aguardando conexao'
	(obj, cliente) = serv_socket.accept()
	print 'Conectado'
	while True:
		print 'Aguardando mensagem de %s' %cliente[0]
		recebe = obj.recv(1024)
		if not recebe: break
		print 'Mensagem recebida: '+ recebe
		mensagem = raw_input('Digite uma mensagem para enviar ao cliente\n')
		print 'Mensagem enviada, aguardando a proxima mensagem.\n'
	print 'Encerrando a conexao.\n'
	serv_socket.close()
except Exception as erro:
	print erro
	serv_socket.close()