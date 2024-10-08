from socket import *
port = 12000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', port))
server_socket.listen(1)
print('The server is ready to receive')
while True:
    # acception the connection request
    connectionSocket, addr = server_socket.accept()
    
    message = connectionSocket.recv(2048)
    modified_message = message.decode().upper()
    connectionSocket.send(modified_message.encode())

    # close the connection
    connectionSocket.close()