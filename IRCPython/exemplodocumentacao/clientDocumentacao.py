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
tcp.sendall('Hello, world')
# Armazena o input do que foi digitado no teclado na variavel
raw_input("digite uma mensagem para enviar ao servidor\n")
# Variavel que recebe a quantidade de bytes especificados, no caso 1024
data = tcp.recv(1024)
# Fecha a conexao com o objeto que veio com o TCP
tcp.close()
# Imprimi mensagem na tela do cliente
print 'Received', repr(data)