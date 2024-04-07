from socket import *
import _thread as thread
import time

def now():
    """
    Returns current time. We will use this for logging to timestamp the server actions. 
    We use "import time" to get this.
    """
    return time.ctime(time.time())

def handle_client(connection):
    """
    We handle individual client request for each seperate thread. The function processes the HTTP requersts.
    Attempting to fetch the requested file and send the appropriate HTTP response. 
    
    Return "200 - OK", but if file not found, return "404 - not found". 

    """
    while True:
        try:
            message = connection.recv(1024).decode()
            if not message:
                break  # Breaking loop if message is not received. THis indicates that the client  the connection.
            print(f"Received message at {now()} = ", message)
            
            echo_message = f"Echo: {message}"
            connection.send(echo_message.encode())
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    connection.close()

def main():
    """
    Sets up the server socket.
    Listens for new connections. 
    Spawns a new thread for each connection.
    """

    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)  # Keeping a listen queue of 5
    print('The server is ready to receive at', now())
    
    while True:
        connectionSocket, addr = serverSocket.accept()
        print('Server connected by', addr, 'at', now())
        thread.start_new_thread(handle_client, (connectionSocket,))

if __name__ == '__main__':
    main()
