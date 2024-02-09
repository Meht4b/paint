import threading
import socket
import pickle

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',8080))
server.listen()

clients = []
clientno = 0

def handleClient(conn,client):
    global clients
    
    while True:
        try:
            data = pickle.loads(conn.recv(50))
            if data != None:
                for i in range(len(clients)):
                    if i!=client:
                        clients[i].append(data)
            
            print(clients)
            conn.send(pickle.dumps(clients[client]))
            clients[client] = []

        except:
            conn.close()


while True:
    
    conn,addr = server.accept()
    thread = threading.Thread(target=handleClient,args=(conn,clientno))
    thread.start()
    clientno+=1
    clients.append([])
