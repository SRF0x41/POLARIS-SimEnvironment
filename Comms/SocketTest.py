import socket

HOST = '127.0.0.1'  # Localhost (only accessible from this machine)
PORT = 12345      # Port number (can be any free port)

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))  # Bind to localhost and port
server_socket.listen(1)  # Listen for connections

print(f"Server listening on {HOST}:{PORT}...")

while True:
    client_socket, client_address = server_socket.accept()  # Accept a connection
    print(f"Connection from {client_address}")

    # Receive data
    data = client_socket.recv(1024).decode()
    if data:
        print(f"Received: {data}")

    # Send a response
    client_socket.sendall("Message received!".encode())

    # Close the connection
    client_socket.close()
