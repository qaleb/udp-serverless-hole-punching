import socket

def start_client():
    # Get the user input for Device B's IP address or hostname
    device_B_ip = input("Enter the IP address or hostname of Device B: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(b"Connect", (device_B_ip, 5000))

    # Receive the response containing the client's public address
    data, server_address = client_socket.recvfrom(1024)
    server_address = eval(data.decode('utf-8'))

    print(f"Connected to server at {server_address}")

    # Now, you can use server_address to communicate directly with Device B

    client_socket.close()

if __name__ == "__main__":
    start_client()
