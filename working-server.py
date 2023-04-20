import socket, select

def main():
    CONNECTION_LIST = []
    RECV_BUFFER = 1024 
    PORT = 666
         
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("IP", PORT))
    server_socket.listen(10)
 
    CONNECTION_LIST.append(server_socket)
 
    print("Conecção na porta: " + str(PORT))
 
    while 1:
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
 
        for sock in read_sockets:
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print("Client (%s, %s) concetado" % addr)
                 
            else:
                try:
                    data = sock.recv(RECV_BUFFER)
                    print(data)


                except:
                    print("Client (%s, %s) morreu" % addr)
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue
         
    server_socket.close()
    
if __name__ == "__main__":
    main()