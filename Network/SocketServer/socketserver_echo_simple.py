import socketserver

class EchoRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        self.request.send(data)
        return
    
if __name__ == '__main__':
    import socket
    import threading
    
    address = ('localhost', 0)
    server = socketserver.TCPServer(address, EchoRequestHandler)
    ip, port = server.server_address
    
    print('{} port {}'.format(ip,port))
    
    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)  # don't hang on exit
    t.start()
    
    # Connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Send the data
    message = 'Hello, world'.encode()
    print('Sending : {!r}'.format(message))
    len_sent = s.send(message)

    # Receive a response
    response = s.recv(len_sent)
    print('Received: {!r}'.format(response))

    # Clean up
    server.shutdown()
    s.close()
    server.socket.close()