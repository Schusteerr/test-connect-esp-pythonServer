from time import sleep
from socket import socket
from multiprocessing.dummy import Pool

def send_msg(tcp_socket):
    with tcp_socket:
        while True:
            try:
                umidade1= 80
                mensagem=umidade1
                tcp_socket.send(mensagem.encode("utf-8"))
                sleep(2)  #confirmação de mensagem enviada
                print("Mensagem Enviada!")
            except Exception as ex:
                print("schuster triste:(", ex)
                break

def recv_msg(tcp_socket):
    with tcp_socket:
        while True:
            #mensagem recebida do servidor e mensagem caso servidor for fechado
            try:
                data = tcp_socket.recv(1024)
                if data:
                    print("server Mensage:", data.decode("utf-8"))
            except Exception as ex:
                print("schuster triste:(", ex)
                break

def main():
    with socket() as tcp_socket:
        # conectado ao TCP Server
        tcp_socket.connect(("IP", 666))
        print("Connected TCP Server...") 

        pool = Pool()
        pool.apply_async(send_msg, args=(tcp_socket,))
        pool.apply_async(recv_msg, args=(tcp_socket,))
        pool.close()
        pool.join()

if __name__ == '__main__':
    main()