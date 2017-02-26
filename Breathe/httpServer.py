import os
import threading
import SimpleHTTPServer
import SocketServer

# Default path
path = os.environ.get('HOMEDRIVE') + os.environ.get('HOMEPATH') + '\AppData\Local\CandC\Server'
port = 777
SERVER_SHUTDOWN = False

class SimpleServer():
    def __init__(self):
        pass
        
    def runServer(self, path, port):
        global SERVER_SHUTDOWN
        print '[*] Starting HTTP server'
        
        os.chdir(path)
        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        httpd = SocketServer.TCPServer(("", port), Handler)
        print "[*] Serving at port: ", port
        httpd.serve_forever()
        
    def stopServer(self):
        print "[*] Shutting down server..."
        self.httpd.shutdown()

# server = SimpleServer()
# server.runServer(path, port)
