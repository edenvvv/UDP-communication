import socket

UDP_IP = '0.0.0.0'
UDP_PORT = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sock.bind((UDP_IP, UDP_PORT))
dict_db = {}

while True:
    data, addr = sock.recvfrom(1024)

    if addr in dict_db.values():
        message = (data.decode()).split(" ", 1)
        if message[0] in dict_db.keys():
            sock.sendto(f"receive message is: {message[1]}".encode(), dict_db[message[0]])
        else:
            sock.sendto(f"There is no user named {message[0]}".encode(), addr)
    else:
        # Add to db {name: address}
        dict_db[data.decode()] = addr
