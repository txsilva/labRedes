# Importa a biblioteca para socket
import socket
# Defini o ip do host
HOST = 'localhost'
# Porta que o Servidor fica escutando
PORT = 50007
# Armazena na variavel tcp. AF.NET defini a conexao IPV4 e SOCK_STREAM defini a conexao TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Armazena o ip e a porta para a conexao
tcp.connect((HOST, PORT))
# Envia todos os dados da string ate que termine ou ocorra um erro.
# Essa funcao e diferente de send() que envia e espera um retorno com 
# a quantidade de byte enviado, para saber se fara novo envio.

# Inicializa a opcao para funcionar o
opcao = 0
nregister = '0'
# Enquanto
while(True):
	print (30 * '-')
	print ("   B A T E - P A P O    ")
	print (30*'-')
	print (3*' '+ "1. Registrar Nick ")
	print (3*' '+"2. Entrar em uma sala ")
	print (3*' '+"3. Sair")
	print (30 * '-')
# Armazena o input do que foi digitado no teclado na variavel
	opcao = raw_input('Digite a sua escolha [1-3] : ')
	opcao = int(opcao)
	if opcao == 1:
		nick = raw_input("\nOla, seja bem vindo! Entre com o seu nick:\n")
		tcp.send(nick)
	elif opcao == 2:
		tcp.send('2')
	elif opcao == 3:
		print "Aguardando o fechamento do chat!\n\n"		
		tcp.send('3')
		if tcp.recv(1024) == '500':
			print "O chat esta fechado"
			break
	if tcp.recv(1024) == '400':
		print ("O chat esta cheio, tente novamente mais tarde")
# Fecha a conexao com o objeto que veio com o TCP
tcp.close()
