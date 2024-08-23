import socket

port = 53
ip = "127.0.0.1"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # AF_INET: IPv4, SOCK_DGRAM: UDP, set up a UDP socket
sock.bind((ip, port))

def buildresponse(data):
    transactionId = data[:2]
    modifiedTransactionId = ''
    for i in transactionId: # remove the first 2 char in each byte of transactionId
        modifiedTransactionId += hex(i)[2:]  
    print(transactionId)

while True:
    data, addr = sock.recvfrom(512) # recieve 512 bytes
    response = buildresponse(data)
    sock.sendto(data, addr)