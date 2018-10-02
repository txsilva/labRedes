# Importa a biblioteca para socket
import socket
# Defini o ip do host
host = '127.0.0.1'
# Porta que o Servidor fica escutando
port = 7000
# Armazena o ip e a porta para a conexao
addr = (host,port)
# AF.NET defini a conexao IPV4 e SOCK_STREAM defini a conexao TCP
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Defini o valor de opcao do socket, pode ser uma string ou um numero
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Try para trabalhar com excecoes
try:
	# Conexao do servico TCP ao endereco de IP, como uma tupla
	serv_socket.bind(addr)
	# Quantidade de conexoes suportadas
	serv_socket.listen(3)
	print 'Aguardando conexao'
	# obj serve como o objeto da conexao e cliente serve como os dados da conexao
	(obj, cliente) = serv_socket.accept()
	print 'Conectado'
	while True:
		print 'Aguardando mensagem de %s' %cliente[0]
		# recv funciona para o saber o tamanho do buffer que sera lido por vez da mensagem do cliente
		recebe = obj.recv(1024)
		if not recebe: break
		print 'Mensagem recebida: '+ recebe
		# Espera uma string digitada
		mensagem = raw_input('Digite uma mensagem para enviar ao cliente\n')
		print 'Mensagem enviada, aguardando a proxima mensagem.\n'
	print 'Encerrando a conexao.\n'
	# Encerra a conexao com o servidor ao final do while
	serv_socket.close()
except Exception as erro:
	print erro
	# Encerra a conexao com o servidor porque houve uma excecao do try 
	serv_socket.close()