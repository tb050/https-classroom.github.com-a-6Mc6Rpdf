# Ty Brien
import socket

LHOST = ''
LPORT = 5000
RCV_DATA = ""

L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
L_SOCK.bind((LHOST, LPORT))

while(True):
    L_SOCK.listen(1)
    L_CONN, addr = L_SOCK.accept()
    print("Connected by", addr)
    while 1:
        RCV_DATA = L_CONN.recv(1024)
        if not RCV_DATA:
            print("Did not receive data. Exiting")
            break
        with open("transfer-destination.txt", "wb") as transfer_file:
            transfer_file.write(RCV_DATA)
        print(f"File received from client")
    L_CONN.close()