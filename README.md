# BrainDamage
A python based backdoor which uses [Telegram](https://telegram.org/) as C&C server.

<pre>
                           /\
                          /_.\
                    _,.-'/ `",\'-.,_
                 -~^    /______\`~~-^~:

  ____            _       _____                                   
 |  _ \          (_)     |  __ \                                  
 | |_) |_ __ __ _ _ _ __ | |  | | __ _ _ __ ___   __ _  __ _  ___ 
 |  _ <| '__/ _` | | '_ \| |  | |/ _` | '_ ` _ \ / _` |/ _` |/ _ \
 | |_) | | | (_| | | | | | |__| | (_| | | | | | | (_| | (_| |  __/
 |____/|_|  \__,_|_|_| |_|_____/ \__,_|_| |_| |_|\__,_|\__, |\___|
                                                        __/ |     
                                                       |___/      

--> Coded by: Mehul Jain(mehulj94@gmail.com)
--> Github: https://github.com/mehulj94
--> Twitter: https://twitter.com/_b00geyman_
--> For windows only

  ______         _                       
 |  ____|       | |                      
 | |__ ___  __ _| |_ _   _ _ __ ___  ___ 
 |  __/ _ \/ _` | __| | | | '__/ _ \/ __|
 | | |  __/ (_| | |_| |_| | | |  __/\__ \
 |_|  \___|\__,_|\__|\__,_|_|  \___||___/
                                         

--> Persistance
--> USB spreading
--> Port Scanner
--> Router Finder
--> Run shell commands
--> Keylogger
--> Insert keystrokes
--> Record audio
--> Webserver
--> Screenshot logging
--> Download files in the host
--> Execute shutdown, restart, logoff, lock
--> Send drive tree structure
--> Set email template
--> Rename Files
--> Change wallpaper
--> Open website
--> Send Password for
    • Chrome
    • Mozilla
    • Filezilla
    • Core FTP
    • CyberDuck
    • FTPNavigator
    • WinSCP
    • Outlook
    • Putty
    • Skype
    • Generic Network
--> Cookie stealer
--> Send active windows
--> Gather system information
    • Drives list
    • Internal and External IP
    • Ipconfig /all output
    • Platform
</pre>

# Setup
* Telegram setup:
  * Install [Telegram](https://telegram.org/) app and search for "BOTFATHER".
  * Type /help to see all possible commands.
  * Click on or type /newbot to create a new bot.
  * Name your bot.
  * You should see a new API token generated for it.
* Dedicated Gmail account. Remember to check "allow connection from less secure apps" in gmail settings.
* Set access_token in eclipse.py to token given by the botfather.
* Set CHAT_ID in eclipse.py. Send a message from the app and use the telegram api to get this chat id.

> bot.getMe() will give output {'first_name': 'Your Bot', 'username': 'YourBot', 'id': 123456789}

* Set copied_startup_filename in Eclipse.py.
* Set Gmail password and Username in /Breathe/SendData.py


# Abilities
* whoisonline- list active slaves
> This command will list all the active slaves.

* destroy- delete&clean up
> This command will remove the stub from host and will remove registry entries.

* cmd- execute command on CMD
> Run shell commands on host

* download- url (startup, desktop, default)
> This will download files in the host computer.

* execute- shutdown, restart, logoff, lock
> Execute the following commands

* screenshot- take screenshot
> Take screenshot of the host of computer.

* send- passwords, drivetree, driveslist, keystrokes, openwindows
> This command will sends passwords (saved browser passwords, FTP, Putty..), directory tree of host (upto level 2), logged keystrokes and windows which are currently open

* set- email (0:Default,1:URL,2:Update), filename (0: Itself, 1: Others), keystrokes (text)
> This command can set email template (default, download from url, update current template with text you'll send), rename filenames or insert keystrokes in host.

* start- website (URL), keylogger, recaudio (time), webserver (Port), spread
> This command can open website, start keylogger, record audio, start webserver, USB Spreading

* stop- keylogger, webserver
> This command will stop keylogger or webserver

* wallpaper- change wallpaper (URL)
> Changes wallpaper of host computer

* find- openports (host, threads, ports), router
> This command will find open ports and the router the host is using

* help- print this usage

# Requirements
* [Telepot](https://github.com/nickoala/telepot)
* [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/)
* [PyCrypto](http://www.voidspace.org.uk/python/modules.shtml#pycrypto)
* [Pyasn1](https://pypi.python.org/pypi/pyasn1)
* [Pillow](https://pillow.readthedocs.io/en/latest/installation.html)
* Install [PyHook](https://sourceforge.net/projects/pyhook/)
* Install [PyWin32](https://sourceforge.net/projects/pywin32/)
* Install [Microsoft Visual C++ Compiler for Python](https://www.microsoft.com/en-us/download/details.aspx?id=44266)
* Install [PyInstaller](http://www.pyinstaller.org/)

# Screenshots

![Setup](https://image.ibb.co/mkWNRF/Capture.png)

![Notification](https://image.ibb.co/kCey0a/IMG_0009.jpg)

![Who is Online Telegram](https://image.ibb.co/f20GmF/IMG_0006.jpg)

![Help Telegram](https://image.ibb.co/bZHJ0a/IMG_0004.jpg)

![Record Audio Telegram](https://image.ibb.co/dA3fDv/IMG_0005.jpg)

![Take screenshot Telegram](https://image.ibb.co/buPntv/IMG_0007.jpg)

# For educational purposes only, use at your own responsibility.

