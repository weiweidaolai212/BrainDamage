import os
import time
from datetime import datetime, timedelta

try:
  import win32file, win32con
  __use_win_32 = True
except:
  __use_win_32 = False


def changeTimestamp(path,fileName,daylimit):
    print '[*] Inside changeTimestamp'
    dates = {}
    fileName = os.path.join(path, fileName)
    dates['tdata'] = getDate(fileName,daylimit)
    dates['ctime'] = datetime.utcfromtimestamp(os.path.getctime(fileName))
    
    # print "[*] Original time: ",str(dates['ctime'])
    
    if __use_win_32:
        filehandle = win32file.CreateFile(fileName, win32file.GENERIC_WRITE, 0, None, win32con.OPEN_EXISTING, 0, None)
        win32file.SetFileTime(filehandle, dates['tdata'],dates['tdata'],dates['tdata'])
        filehandle.close()
        print "[*] Timestamps changed!!"
    else:
        os.utime(fileName, (time.mktime(dates['tdata'].utctimetuple()),)*2)
    
    dates['mtime'] = datetime.utcfromtimestamp(os.path.getmtime(fileName))    
    # print "[*] Modified time: ",str(dates['mtime'])

def getDate(path, daylimit):
    diff = timedelta(days=daylimit) # Time difference from current date and time and not the folders date
    timeStamp = datetime.now()
    return timeStamp-diff
