# Rename file
import os

# thisFile = __file__

def local_file(path,filename,newname):
    print '[*] Modifying local file'
    os.rename(os.path.join(path,filename),os.path.join(path,newname))
    
def myself(thisFile,newname):
    print '[*] Modifying itself'
    os.rename(thisFile,newname)
    
