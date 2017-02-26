import win32api, win32con, win32gui
from ctypes import *
import os

#
# Device change events (WM_DEVICECHANGE wParam)
#
DBT_DEVICEARRIVAL = 0x8000
DBT_DEVICEQUERYREMOVE = 0x8001
DBT_DEVICEQUERYREMOVEFAILED = 0x8002
DBT_DEVICEMOVEPENDING = 0x8003
DBT_DEVICEREMOVECOMPLETE = 0x8004
DBT_DEVICETYPESSPECIFIC = 0x8005
DBT_CONFIGCHANGED = 0x0018

#
# type of device in DEV_BROADCAST_HDR
#
DBT_DEVTYP_OEM = 0x00000000
DBT_DEVTYP_DEVNODE = 0x00000001
DBT_DEVTYP_VOLUME = 0x00000002
DBT_DEVTYPE_PORT = 0x00000003
DBT_DEVTYPE_NET = 0x00000004

#
# media types in DBT_DEVTYP_VOLUME
#
DBTF_MEDIA = 0x0001
DBTF_NET = 0x0002

WORD = c_ushort
DWORD = c_ulong

DRIVE = ""
FLAG = False

class DEV_BROADCAST_HDR (Structure):
  _fields_ = [
    ("dbch_size", DWORD),
    ("dbch_devicetype", DWORD),
    ("dbch_reserved", DWORD)
  ]

class DEV_BROADCAST_VOLUME (Structure):
  _fields_ = [
    ("dbcv_size", DWORD),
    ("dbcv_devicetype", DWORD),
    ("dbcv_reserved", DWORD),
    ("dbcv_unitmask", DWORD),
    ("dbcv_flags", WORD)
  ]

def drive_from_mask (mask):
  n_drive = 0
  while 1:
    if (mask & (2 ** n_drive)): return n_drive
    else: n_drive += 1

def write_drive_name (dname):
    config_file = open(os.path.join(PATH,FILE),'a')
    config_file.write("External Drive Found: %s\n" % dname)
    config_file.close()
    
class Notification:

  def __init__(self):
    message_map = {
      win32con.WM_DEVICECHANGE : self.onDeviceChange
    }
    
    wc = win32gui.WNDCLASS ()
    hinst = wc.hInstance = win32api.GetModuleHandle (None)
    wc.lpszClassName = "DeviceChangeDemo"
    wc.style = win32con.CS_VREDRAW | win32con.CS_HREDRAW;
    wc.hCursor = win32gui.LoadCursor (0, win32con.IDC_ARROW)
    wc.hbrBackground = win32con.COLOR_WINDOW
    wc.lpfnWndProc = message_map
    classAtom = win32gui.RegisterClass (wc)
    style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
    self.hwnd = win32gui.CreateWindow (
      classAtom,
      "Device Change Demo",
      style,
      0, 0,
      win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,
      0, 0,
      hinst, None
    )

  def onDeviceChange (self, hwnd, msg, wparam, lparam):
    global DRIVE
    global FLAG
    dev_broadcast_hdr = DEV_BROADCAST_HDR.from_address (lparam)

    if wparam == DBT_DEVICEARRIVAL:
      if dev_broadcast_hdr.dbch_devicetype == DBT_DEVTYP_VOLUME:
        dev_broadcast_volume = DEV_BROADCAST_VOLUME.from_address (lparam)
        drive_letter = drive_from_mask (dev_broadcast_volume.dbcv_unitmask)
        DRIVE = chr (ord ("A") + drive_letter)
        print "[*] Drive Found: ", DRIVE + ":\\"
        FLAG = True
        win32gui.PostQuitMessage(0)
        #win32gui.PostQuitMessage(0)
    return 1