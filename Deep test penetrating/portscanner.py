import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.settimeout(5)

host = input("please enter the IP you want to scan: ")
port = int(input("Please neterthe port you want to scan: "))

def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is safe")

portScanner(port)