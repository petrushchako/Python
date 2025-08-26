import socket
import threading

def handle_client(client_socket):
    try:
        data = client_socket.recv(1024).decode()
        print(f"Received from client: {data}")
        client_socket.sendall("Hey client".encode())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()


