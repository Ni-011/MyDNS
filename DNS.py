import socket

port = 53
ip = "127.0.0.1"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # AF_INET: IPv4, SOCK_DGRAM: UDP, set up a UDP socket
sock.bind((ip, port))

while True:
    data, addr = sock.recvfrom(512) # recieve 512 bytes
    print(data)