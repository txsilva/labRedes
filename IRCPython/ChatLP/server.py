# encoding: utf-8

 
import os, sys, socket, select

HOST = '' 
SOCKET_LIST = []
RECV_BUFFER = 4096 
PORT = 9009

def chat_server():

   
#   Nesta linha criamos o nosso mecanismo de Socket para receber a conexão,onde na função passamos 2 argumentos,
#   AF_INET que declara a família do protocolo; se fosse um envio via Bluetooth por exemplo,
#   seria: AF_BLUETOOTH, SOCKET_STREAM, indica que será TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
#   Essa linha serve para zerar o TIME_WAIT do Socket, por exemplo, se o programa estiver aguardando uma conexão
#   e você der CTRL+C para interromper, o programa fecha porém o Socket continua na escuta e se você for usar a
#   mesma porta receberá a seguinte mensagem: socket.error: [Errno 98] Address already in use   
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   
#   Esta linha define para qual IP e porta o servidor deve aguardar a conexão, que no nosso caso é qualquer IP, 
#   por isso o Host é ''. 
    server_socket.bind((HOST, PORT))
  
    #Define o limite de conexões
    server_socket.listen(10)
    
    SOCKET_LIST.append(server_socket)
    os.system('cls' if os.name == 'nt' else 'clear')
    print "\nServidor do chat iniciado na porta: " + str(PORT)
 
    while 1:

        # Pega a lista de sockets que estão prontas para serem lidas através da seleção
        # 4th arg, time_out  = 0 : poll and never block
        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
      
        for sock in ready_to_read:
            # Uma nova requisição de conexão recebida
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print "Cliente (%s, %s) conectado" % addr
                 
                broadcast(server_socket, sockfd, "\n[%s:%s] entrou em nossa sala de bate-papo\n" % addr)
             
            # uma mensagem de um cliente, e não uma nova conexão
            else:
                # dados de processamento recebidos do cliente  
                try:
                    # Recebendo dados do socket. Aguarda um dado enviado pela rede de até 4096 Bytes, 
                    #a função 'recv' possui somente 1 argumento que é o tamanho do Buffer. 
                    data = sock.recv(RECV_BUFFER)

                    if data:
                        # há algo no socket
                        broadcast(server_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data)  
                    else:
                        # Remove o socket que está quebrado 
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)

                        # nesse estágio, sem dados, significa que provavelmente a conexão foi interrompida
                        broadcast(server_socket, sock, "\nCliente (%s, %s) está offline\n" % addr) 

                # excessão 
                except:
                    broadcast(server_socket, sock, "\nCliente (%s, %s) está offline\n" % addr)
                    continue

    server_socket.close()
    
# transmitir mensagens do chat para todos clientes conectados
def broadcast (server_socket, sock, message):
    for socket in SOCKET_LIST:
        # Envia a mensagem só para os outros conectados (não envia para que a escreveu)
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # Conexão com socket quebrada
                socket.close()
                # Socket quebrado, remova-o
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)
 
if __name__ == "__main__":

    sys.exit(chat_server())


         