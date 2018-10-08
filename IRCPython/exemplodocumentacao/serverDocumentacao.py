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
print 'Conectado pelo cliente e porta', addr

nick = ['0', '1', '2']
count = 4
# Enquanto 
while True:
	data = conn.recv(1024)
	if not data: break
	if (nick[0] == '0' and data != '3'):
		nick[0] = data
		print "Nick registrado com sucesso\n"
		conn.send(nick[0])
		count = 0		
	elif (nick[1] == '1' and data != '3'):
		nick[1] = data
		print "Nick registrado com sucesso\n"
		count = 1
		conn.send(nick[1])
	elif (nick[2] == '2' and data != '3'):
		nick[2] = data
		print "Nick registrado com sucesso\n"
		count = 2
		conn.send(nick[2])
	elif (nick[0] != '0' and nick[1] != '1' and nick [2] != '2'):
		print ('O chat esta sem vaga, tente novamente')
		conn.send('400')
	if data == '2':
		print ("Segunda opcao")	
	if data == '3':
		print ("Usuario saindo do chat\nDeve liberar para novo usuario")
		conn.send("500")
	print ("Usuarios logados ", nick)
print ("Servidor desligado")
conn.close()
