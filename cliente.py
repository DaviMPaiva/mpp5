import socket
import threading
import time
class UdpClientClass(threading.Thread):
    def __init__(self,addres,port):
        self.running = True
        self.addres = addres
        self.port = port

    def terminate(self):
        self.running = False

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print('porta UDP pronta')
        while self.running:
            break


class TcpClientClass(threading.Thread):
    def __init__(self,addres,port):
        self.running = True
        self.addres = addres
        self.port = port

    def terminate(self):
        self.running = False

    def run(self):
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((self.addres,self.port))
            print('conexao TCP estabelecida')
        except:
            print('falhou em fazer o a conexao TCP como cliente')
            #self.terminate()
        else:
            print('continuando')
            while self.running:
                break#a logica vem aqui

Tcp_class = TcpClientClass('127.0.0.1',32000)
Tcp = threading.Thread(target=Tcp_class.run)
Tcp.start()
Udp_class = UdpClientClass('127.0.0.1',30000)
Udp = threading.Thread(target=Udp_class.run)
Udp.start()
