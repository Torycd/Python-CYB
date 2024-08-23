import socket

server_socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#  this is the same as host : "socket.gethostbyname()"
host = "192.168.0.4"
port = 444

server_socket_object.bind((host, port))

server_socket_object.listen(3)

while True:
    clientsocket, address = server_socket_object.accept()

    print("recieved connection from %r " % str(address))
    message = 'Thank you for connecting to the server, this is an example of a server' + '\r\n'

    clientsocket.send(message.encode('ascii'))

    clientsocket.close()