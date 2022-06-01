import socket
from _thread import *
import pickle
from game import Game
#se ocupa de id-ul playerilor,id-ul jocului
#trateaza fiecare client in paralel
#transfer continuu de date cu clientul pe baza requestului

server = ""#ip server// ip la care te referi cand te conectezi: "" inseamna "0.0.0.0" adica allow all
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#decalram serveru

try:
    s.bind((server, port))# ii atribuim adresa
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0


def threaded_client(conn, p, gameId):#pentru fiecare client creeaza un nou thread// fiecare player comunica in paralel cu serveru
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()#primeste conexiunea de la client

            if gameId in games:
                game = games[gameId]#ia id-ul jocului, acesta creste pt fiecare 2 playeri

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()#reset game
                    elif data != "get":
                        game.play(p, data)#transfer continuu de date server client

                    conn.sendall(pickle.dumps(game))# trimite data catre network
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)#conexiune stabilita

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2#game id creste pt fiecare 2 playeri
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1


    start_new_thread(threaded_client, (conn, p, gameId))#creeaza thread pt fiecare player care se connecteaza