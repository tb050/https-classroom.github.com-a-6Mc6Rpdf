# Ty Brien
# Week 12 Assignment 
import socket

RHOST = '127.0.0.1'
RPORT = 5000
SND_DATA = ""

if __name__ == "__main__":
    C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    C_SOCK.connect((RHOST, RPORT))

    with open("transfer.txt", "rb") as transfer_file:
        SND_DATA = transfer_file.read()
    print(SND_DATA)
    C_SOCK.send(SND_DATA)
    print("Sent transfer file to server")

    C_SOCK.close()