import pygame
import socket
import pickle

class ClientNetwork:
    def __init__(self,host='localhost',port=8080):

        try:

            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.sock.connect((host,port))

        except Exception as e:
            
            return e
        
    def recv(self):
        
        try:
            return self.sock.recv(1000)
        except:
            return None

        
    def send(self,data):
        self.sock.send(pickle.dumps(data))
