import socket
import json

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
        
    def close_connection(self):
        # Close the client socket connection after communication is done
        self.client_socket.close()
        print("Connection closed.")
    
    def recieveDataPrint(self):
        # Receive data 1024 bytes this is s blocking command
        data = self.client_socket.recv(1024).decode()
        # decode bytes and print
        if data:
            print(f"Received: {data}")
            
    def recieveData(self):
        # Receive data 1024 bytes this is s blocking command
        data = self.client_socket.recv(1024)
        return data
        
    def sendMessage(self,message):
         # Send a response
        self.client_socket.sendall(message.encode())
    
    def sendJSON(self,message):
        self.client_socket.sendall(json.dumps(message).encode())
        
    def serializeData(self, obj):
        # Ensure obj is a list
        if not isinstance(obj, list):
            raise TypeError("Expected a list")

        data = []  
        data.append(bytes())  # Initialize with an empty bytes object

        for item in obj:
            if isinstance(item, str):  
                encoded = item.encode('utf-8')  # Convert string to bytes
            elif isinstance(item, int):
                encoded = item.to_bytes(4, byteorder='big', signed=True)  # Convert int to 4-byte representation
            elif isinstance(item, float):
                import struct
                encoded = struct.pack('f', item)  # Convert float to 4 bytes
            else:
                raise TypeError(f"Unsupported data type: {type(item)}")

            data.append(encoded)  

        return b''.join(data)  # Concatenate all byte sequences
