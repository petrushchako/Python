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


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("localhost", 12345)
server_socket.bind(server_address)
server_socket.listen(5)

print("Server listen on: " + server_address[0])


# while True:
#     client_socket, client_address = server_socket.accept()
#     print("Connected by ", client_address)
#     client_handler = threading.Thread(target=handle_client, args=(client_socket,))
#     client_handler.start()


###########################################################################################

import requests

url = "http://google.com"
res = requests.get(url)

print("Response code: ", res.status_code)
print(res.text)