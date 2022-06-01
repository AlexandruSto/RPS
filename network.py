import socket
import pickle
#stabileste conexiunea intre server si client,
#face transferu de date intre cele 2

class Network:
    def __init__(self,x):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#definim socketul serverului
        self.server = x#ip serverului
        self.port = 5555#portul de connectare
        self.addr = (self.server, self.port)#adresa e alcatuita din ip si port
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)#stabileste conexiunea la server
            return self.client.recv(2048).decode()#primeste id-ul de la server
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))#trimite la client id-ul
            return pickle.loads(self.client.recv(2048*2))#primeste data de la server
        except socket.error as e:
            print(e)