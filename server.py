import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 5000))

    print("Server is listening...")

    data, client_address = server_socket.recvfrom(1024)
    print(f"Received connection request from {client_address}")

    # Respond to the client with its address
    server_socket.sendto(str(client_address).encode('utf-8'), client_address)

    server_socket.close()

if __name__ == "__main__":
    start_server()
