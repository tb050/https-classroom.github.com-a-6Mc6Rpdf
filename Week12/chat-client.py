# Ty Brien  
# Week 12 Assignment
import socket

RHOST = "127.0.0.1"
RPORT = 5000
RCV_DATA = ""

if __name__ == "__main__":
    C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    C_SOCK.connect((RHOST, RPORT))

    while True:
        user_input = input("Send a message [or exit]: ")
        if user_input == "exit":
            break
        C_SOCK.send(user_input.encode())
        RCV_DATA = C_SOCK.recv(1024)
        print(RCV_DATA.decode())

    C_SOCK.close()