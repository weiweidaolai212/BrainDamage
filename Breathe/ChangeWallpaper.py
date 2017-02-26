import os
import time
import urllib
import ctypes

SPI_SETDESKWALLPAPER = 20
# wallpaper_save_path = os.environ.get('HOMEDRIVE') + os.environ.get('HOMEPATH') + '\AppData\Local\CandC\wallpaper\\'
SAVE_FILES = os.environ.get('HOMEDRIVE') + os.environ.get('HOMEPATH') + '\AppData\Local\CandC'
CACHE_PATH = SAVE_FILES + "\\Cache\\"

class ChangeWallpaper():
    def __init__(self):
        pass

    def downloadWallpaper(self, url):
        print '[*] Inside change wallpaper'
        image_name = CACHE_PATH + url.rsplit('/', 1)[1]
        try:
            f = open(image_name, 'wb')
            f.write(urllib.urlopen(url).read())
            f.close()
            time.sleep(5)
            self.background(image_name)
            print '[*] Wallpaper changed'
        except Exception as e:
            print '==> Error in changing wallpaper'
            print e

    def background(self, path):
        try:
            time.sleep(1)
            ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, str(path), 0)
        except Exception as e:
            print e
            
# wallpaper = changewallpaper.ChangeWallpaper()
# wallpaper.downloadWallpaper(img_url)