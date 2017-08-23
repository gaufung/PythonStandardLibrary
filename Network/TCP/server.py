import socket
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print('start up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)
while True:
    print('waiting for connecting')
    connection, clinet_address = sock.accept()
    try:
        print('connect from', clinet_address)
        while True:
            data = connection.recv(16)
            print('receive {!r}'.format(data))
            if data:
                print('send data back to client')
                connection.sendall(data)
            else:
                print('no data from', clinet_address)
                break
    finally:
        connection.close()