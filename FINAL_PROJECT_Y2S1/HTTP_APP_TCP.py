import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8080        # The port used by the server

# Define the HTTP response
response = b"""\
HTTP/1.1 200 OK
Content-Type: text/html

<html>
<head>
<title>My Webpage</title>
</head>
<body>
<h1>Welcome to my webpage!</h1>
<p>Here is some content.</p>
<img src="http://other-server.com/image.jpg" alt="An image">
</body>
</html>
"""

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind the socket to a specific address and port
    server_socket.bind((HOST, PORT))

    # Listen for incoming connections
    server_socket.listen()

    print(f'Server listening on port {PORT}...')

    # Wait for a client connection
    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Connection from {client_address}')

        # Receive the client's request
        request = client_socket.recv(1024)

        # Send the HTTP response to the client
        client_socket.sendall(response)

        # Close the connection with the client
        client_socket.close()
