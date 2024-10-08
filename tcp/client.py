from socket import *
server_name = "192.168.1.64"
server_port = 12000
client_socket = socket(AF_INET, SOCK_STREAM) # TCP
client_socket.connect((server_name, server_port)) # TCP
message = input("input lowercase sentence -> ")
client_socket.send(message.encode()) # TCP
modified_message, server_address= client_socket.recvfrom(2048)
print(modified_message.decode())
client_socket.close()