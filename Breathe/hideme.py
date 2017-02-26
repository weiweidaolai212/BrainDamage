import ctypes
FILE_ATTRIBUTE_HIDDEN = 0x02

def hideFiles(folderPath):
    print '[*] Hiding files'
    try:
        ctypes.windll.kernel32.SetFileAttributesW.argtypes = (ctypes.c_wchar_p, ctypes.c_uint32)
        ret = ctypes.windll.kernel32.SetFileAttributesW(folderPath.encode('string-escape'), FILE_ATTRIBUTE_HIDDEN)
        if ret:
            print '[*] Folder is set to Hidden'
        else:  # return code of zero indicates failure, raise Windows error
            raise ctypes.WinError()
    except Exception as e:
        print '[*] Error in hiding files'
        print e
