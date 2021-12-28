from socket import *
import struct
import keyboard
import sys
import select

from serverTest import FORMAT

HEADER = 0xabcddcba
MESSAGETYPE = 0x2
UDP_PORT = 13117
BUFF_SIZE = 2<<10
team_name = "Desperate Programming Apes"

class Client:
    
    def __init__ (self):
        self.connection_to_UPD()
  

    def connection_to_UPD(self):
        clientSocketUDP = socket(AF_INET, SOCK_DGRAM)
        clientSocketUDP.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        clientSocketUDP.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        print("Client started, listening for offer requests...")
        clientSocketUDP.bind(("", UDP_PORT))
        self.serverConUDP(clientSocketUDP)

    def serverConUDP (self,clientSocketUDP):
        try:
            pack, address = clientSocketUDP.recvfrom(BUFF_SIZE)
            print("Received offer from " + address[0]+", attempting to connect..")
            message = struct.unpack("IBH",pack)
            self.connect_to_TCP(('127.0.0.1',message[2]))
        except:
            pass


    def connect_to_TCP(self,address):
        clientSocketTCP=socket(AF_INET, SOCK_STREAM)
        clientSocketTCP.connect((address[0],address[1]))
        clientSocketTCP.send(str.encode(team_name))
        while True:
            message = clientSocketTCP.recv(BUFF_SIZE)
            print(message.decode(FORMAT))
            input = keyboard.read_key()
            clientSocketTCP.send(str.ecnode(input))



Client()