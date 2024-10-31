import socket
import pickle
from player import Player

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.43.35"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self) -> Player:
        return self.p
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
            

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)