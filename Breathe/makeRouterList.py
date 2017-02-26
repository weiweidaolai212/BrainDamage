import os
rl = '''2wire
3com
asmax
asus
belkin
bhu
billion
cisco
cisco
comtrend
dlink
fortinet
grandstream
huawei
ipfire
juniper
linksys
multi
netcore
netgear
netsys
shuttle
technicolor
thomson
tplink
ubiquiti
zte
AirLive
D-Link
Huawei
Pentagram
TP-Link
ZynOS
ZyXEL
Quantum
Array Networks
Array
Barracuda
Ceragon
DASDEC
Vagrant
LevelOne
Diamond
SerComm
Azmoon
cyberoam'''
SAVE_FILES = os.environ.get('HOMEDRIVE') + os.environ.get('HOMEPATH') + '\AppData\Local\CandC'
USERDATA_PATH = SAVE_FILES + "\\User Data\\"

def makeRList():
    try:
        rlist = os.listdir(USERDATA_PATH)
        if 'routerlist.txt' not in rlist:
            file = open(USERDATA_PATH+'routerlist.txt','w')
            file.write(rl)
            file.close()
    except Exception as e:
        print e