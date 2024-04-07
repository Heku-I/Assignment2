#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM) 

#Setting the IP and port.
server_ip = '127.0.0.1'
port = 12000

##Telling the socket on the server-side which local protocol (IP & Port) to listen to.
serverSocket.bind((server_ip, port))

##Preparing the server for listening to connect requests - at least 1 time. 
serverSocket.listen(1)

while True:
	#Establish the connection
	print('Ready to serve...')
	connectionSocket, addr = serverSocket.accept() 

	try:

		#Attemting to read data from the client
		message = connectionSocket.recv(1024).decode()
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()


		#Send one HTTP header line into socket
		connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
		connectionSocket.send(outputdata.encode())

		#Send the content of the requested file to the client 
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode()) 
		connectionSocket.send("\r\n".encode())
		connectionSocket.close()


	except IOError:
		#Send response message for file not found
		connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
		connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>".encode())
		print('File not found.')
		print('Closing the socket...')		
		#Close client socket
        
		connectionSocket.close()
serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data