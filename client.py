import socket

# Getting the server details to be able to run the request. 
serverName = input("Enter server IP (for example 127.0.0.1): ") #The server is open at IP 127.0.0.1
serverPort = int(input("Enter server port (for example 12000): ")) #The server is open at port 12000.
filename = input("Enter the filename to request: ") #Test index.html or testTask2.txt.

#Create a client socket and connect to the server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

#GET-request
httpGetRequest = f"GET /{filename} HTTP/1.1\r\nHost: {serverName}\r\n\r\n"

# Send the HTTP GET request to the server, then recieve. 
clientSocket.send(httpGetRequest.encode())
response = clientSocket.recv(1024)

#Printing response.
print("From Server:", response.decode())

# Closing the socket
clientSocket.close()