import zlib
import logging
import socketserver
import binascii

BLOCK_SIZE = 64

class ZlibRequestHandler(socketserver.BaseRequestHandler):
    logger = logging.getLogger('Server')
    
    def handle(self):
        compressor = zlib.compressobj(1)
        
        filename = self.request.recv(1024).decode('utf-8')
        self.logger.debug('Client asked for: %s', filename)
        
        with open(filename, 'rb') as input:
            while True:
                block = input.read(BLOCK_SIZE)
                if not block:
                    break
                self.logger.debug('RAW %r', block)
                compressed = compressor.compress(block)
                if compressed:
                    self.logger.debug('Sending %r', binascii.hexlify(block))
                    self.request.send(compressed)
                else:
                    self.logger.debug('buffered')
        remaining = compressor.flush()
        while remaining:
            to_send = remaining[:BLOCK_SIZE]
            remaining = remaining[BLOCK_SIZE:]
            self.logger.debug('FLUSHING %r', binascii.hexlify(to_send))
            self.request.send(to_send)
        return
if __name__ == '__main__':
    import socket
    import threading
    from io import BytesIO
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(name)s: %(message)s'
    )
    logger = logging.getLogger('Client')
    address = ('localhost', 0)
    server = socketserver.TCPServer(address, ZlibRequestHandler)
    ip, port = server.server_address
    
    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()
    
    logger.info('Contacting server on %s:%s',ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    
    requested_file ='zlib_server.py'
    logger.debug('sending filename: %r', requested_file)
    len_sent = s.send(requested_file.encode('utf-8'))
    
    buffer = BytesIO()
    decompressor = zlib.decompressobj()
    while True:
        response = s.recv(BLOCK_SIZE)
        if not response:
            break
        logger.debug('READ %r', binascii.hexlify(response))
        to_decompress = decompressor.unconsumed_tail + response
        while to_decompress:
            decompressed = decompressor.decompress(to_decompress)
            if decompressed:
                logger.debug('DECOMPRESSED %r', decompressed)
                buffer.write(decompressed)
                to_decompress = decompressor.unconsumed_tail
            else:
                logger.debug('BUFFERING')
                to_decompress = None
    remainder = decompressor.flush()
    if remainder:
        logger.debug('FLUSHED %r', remainder)
        buffer.write(remainder)
    full_response=buffer.getvalue()
    lorem = open('zlib_server.py', 'rb').read()
    logger.debug('response mathes file content: %s', full_response == lorem)
    
    s.close()
    server.socket.close()