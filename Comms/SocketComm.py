import socket

class SocketComm:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        
        # setting up the socket
        # Create a TCP socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.HOST, self.PORT))  # Bind to localhost and port
        self.server_socket.listen(1)  # Listen for connections
        
        print(f"Server listening on {self.HOST}:{self.PORT}...")
        
        self.client_socket, self.client_address = self.server_socket.accept()  # Accept a connection
        print(f"Connection from {self.client_address}")
        
        # Close the connection
        self.client_socket.close()
        
    
        
        