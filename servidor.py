import socket
import threading
import time
class UdpServerClass(threading.Thread):
    def __init__(self,addres,port):
        self.running = True
        self.addres = addres
        self.port = port

    def terminate(self):
        self.running = False

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((self.addres, self.port))
        print('Servidor UDP pronto')
        while self.running:
            break

class TcpServerClass(threading.Thread):
    def __init__(self,addres,port):
        self.running = True
        self.addres = addres
        self.port = port

    def terminate(self):
        self.running = False

    def run(self):
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.bind((self.addres, self.port))
            s.listen()
            clientSocket,clientAddress = s.accept()
            print('conexao TCP estabelecida')
        except:
            print('falhou em fazer o a conexao TCP como servidor')
            #self.terminate()
        else:
            print('continuando')
            while self.running:          
                break#a logica vem aqui

Tcp_class = TcpServerClass('127.0.0.1',32000)
Tcp = threading.Thread(target=Tcp_class.run)
Tcp.start()
Udp_class = UdpServerClass('127.0.0.1',30000)
Udp = threading.Thread(target=Udp_class.run)
Udp.start()
time.sleep(20)