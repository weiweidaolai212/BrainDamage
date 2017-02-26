import socket
import Queue
import threading
import datetime

Flag = True
ports = Queue.Queue()
open_ports = []

class PortMap():
    def __init__(self):
        pass
        
    def build_portlist(self, no_ports):
        for p in range(no_ports):
            ports.put(p)
    
    def tcp_make_conn(self, host, no_ports):
        # TCP/IP socket
        global Flag
        global open_ports
        while not ports.empty():
            port = ports.get()
            if port == (no_ports-1):
                Flag = False
            sock_conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            try:
                sock_conn.settimeout(0.5)
                sock_conn.connect((host,port))
                print "[*] Connection Succesful! Port: %s " % port
                open_ports.append(port)
            except Exception as e:
                pass
    
    def run_threads(self, threads, host, no_ports):
        for i in range(threads):
            try:
                t = threading.Thread(target=self.tcp_make_conn, args=(host, no_ports, ))
                t.daemon = True
                t.start()
            except Exception as e:
                pass
            
    def run(self, host, threads, no_ports):
        print '[*] Mapping ports'
        if threads == None:
            threads = 50
        if no_ports == None:
            no_ports = 10000
        if host == None:
            host = "127.0.0.1"
        self.build_portlist(no_ports)
        self.run_threads(threads, host, no_ports)
        while Flag:
            pass
        print '[*] Returning ports'
        return open_ports
        
