import selector
import socket

mysel = selector.DefaultSelector()
keep_running = True

outgoing = [
    b'It will be repeated.',
    b'this is the message.',
]
byte_sent = 0
byte_received = 0

server_address = ('localhost', 10000)
print('connection to {} port {}'.format(*server_address))
sock = socket.socket(socket.AF_INT, socket.SOCK_STREAM)
sock.connect(server_address)
sock.setblocking(False)

mysel.register(sock, 
               selectors.EVENT_READ | selectors.EVENT_WRITE,
              )
while keep_running:
    print('waiting for I/O')
    for key, mask in mysel.select(timeout=1):
        connection = key.fileobj
        client_address = connection.getpeername()
        print('client({})'.format(client_address))
        
        if mask & selectors.EVENT_READ:
            print('  ready to read')
            data = connection.recv(1024)
            if data:
                print(' received {!r}'.format(data))
                bytes_read += len(data)
            keep_running = not(
                data or (bytes_received and (byte_received==bytes_sent))
            )
        if mask & selector.EVENT_WRITE:
            print(' read to write')
            if not outgoing:
                print(' switching to read-only')
                mysel.modify(sock, selectors.EVENT_READ)
            else:
                next_msg = outgoing.pop()
                print('   sending {!r}'.format(next_msg))
                sock.sendall(next_msg)
                byte_sent += len(next_msg)
print('shutting down')
mysel.unregister(connection)
connection.close()
mysel.close()