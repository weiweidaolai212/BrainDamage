import os
import Queue
import socket
import urllib2
import datetime
import threading
import subprocess
import portmap

router_list = []
router_webpage = []
router_logins = ["/login.htm","/login.html",]
links_router_page = []

SAVE_FILES = os.environ.get('HOMEDRIVE') + os.environ.get('HOMEPATH') + '\AppData\Local\CandC'
USERDATA_PATH = SAVE_FILES + "\\User Data\\"

class FindRouter():
    def __init__(self):
        pass
    
    
    def getPrivateIp(self):
        try:
            return socket.gethostbyname(socket.gethostname())
        except Exception as e:
            print e


    def getPublicIp(self):
        try:
            return urllib2.urlopen('http://ip.42.pl/raw').read()
        except Exception as e:
            print e


    def getRouterList(self):
        global router_list
        router_list = open(USERDATA_PATH + 'routerlist.txt','r').readlines()
        for i in range(len(router_list)):
            router_list[i] = router_list[i].rstrip().lower()


    def checkMyIp(self, ip_to_check):
        if ip_to_check[0] == '192' and ip_to_check[1] == '168':
            if int(ip_to_check[2]) >= 0 and int(ip_to_check[2]) <= 255:
                if int(ip_to_check[3]) >= 0 and int(ip_to_check[3]) <= 255:
                    print "[*] IP: %s is NAT'd" % (".".join(ip_to_check))
                    return True
                    
                    
        if ip_to_check[0] == '10':
            if int(ip_to_check[1]) >= 0 and int(ip_to_check[1]) <= 255:
                if int(ip_to_check[2]) >= 0 and int(ip_to_check[2]) <= 255:
                    if int(ip_to_check[3]) >= 0 and int(ip_to_check[3]) <= 255:
                        print "[*] IP: %s is NAT'd" % (".".join(ip_to_check))
                        return True
                        
        if ip_to_check[0] == '172':
            if int(ip_to_check[1]) >= 16 and int(ip_to_check[1]) <= 31:
                if int(ip_to_check[2]) >= 0 and int(ip_to_check[2]) <= 255:
                    if int(ip_to_check[3]) >= 0 and int(ip_to_check[3]) <= 255:
                        print "[*] IP: %s is NAT'd" % (".".join(ip_to_check))
                        return True
                        
        if ip_to_check[0] == '169' and ip_to_check[1] == '254':
            if int(ip_to_check[2]) >= 0 and int(ip_to_check[2]) <= 255:
                if int(ip_to_check[3]) >= 0 and int(ip_to_check[3]) <= 255:
                    print "[*] IP: %s is NAT'd (APIPA only)" % (".".join(ip_to_check))
                    return True
                    
        return False


    # Get default gateway address
    def pingDefaultGateway(self):
        ip_to_check = self.getPrivateIp()
        ip_to_check_split = self.getPrivateIp().split(".")
        if self.checkMyIp(ip_to_check_split):
            ipconfig_output = subprocess.check_output(["ipconfig",],).split('\r\n')
            # new changes starts
            dot_pos =  [pos for pos, char in enumerate(ip_to_check) if char == '.']
            for line in ipconfig_output:
                if 'Default Gateway' in line and ip_to_check[:dot_pos[1]+1] in line:
                    gatewayip = line[line.index(ip_to_check[ip_to_check.index(ip_to_check[0])]):].rstrip()
                    print '[*] Gateway IP: ' + gatewayip
                    return gatewayip


    # Get open ports on default gateway
    def openPorts(self, host, threads, ports):
        # global open_ports
        lp = portmap.PortMap()
        open_ports = lp.run(host, threads, ports)
        return open_ports


    # Request default gateway at specific ports
    def getRouterInfo(self, host, open_ports):
        global router_webpage
        global links_router_page
        for ports in open_ports:
            try:
                router_addr = 'http://' + host + ':' + str(ports)
                r = urllib2.Request(router_addr)
                response = urllib2.urlopen(r, timeout=7).read()
                router_webpage = response.split()
            
            except Exception as e:
                print '[*] Failed connection on host', host, 'port', ports
        return True
        
        
    # Request url fund in default gatways response
    def getRouterInfoUrl(self, url):
        global router_webpage
        router_webpage = []
        try:
            router_addr = url
            r = urllib2.Request(router_addr)
            response = urllib2.urlopen(r).read()
            router_webpage = response.split()
        except Exception as e:
            print '[*] Failed connection on host', url
        return True
    
    
    # Print the results
    def getResult(self):
        global router_webpage
        global router_list
        for i in router_list:
            for j in router_webpage:
                if i.lower() in j.lower():
                    print "[*] Router Found: %s" % i
                    return i
        return False
           
           
    def run(self):
        print '[*] Looking for router'
        host = self.pingDefaultGateway() #'127.0.0.1'
        open_ports = self.openPorts(host, 50, 10000) # [7777,8888]
        self.getRouterList()
        self.getRouterInfo(host, open_ports)
        
        router_found = self.getResult()
        return router_found

# a = FindRouter()
# b = a.run()
# print b
