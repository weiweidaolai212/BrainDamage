# BrainDamage
===
A python based backdoor which uses [Telegram](https://telegram.org/) as C&C server.

# Ability
===
* whoisonline- list active slaves
> This command will list all the active slaves.

* destroy- delete&clean up
> This command will remove the stub from host and will remove registry entries.

* #cmd- execute command on CMD
> Run shell commands on host

* #download- url (startup, desktop, default)
> This will download files in the host computer.

* #execute- shutdown, restart, logoff, lock
> This is to mess with the host :D or refresh if things are not working properly

* #screenshot- take screenshot
> Take screenshot of the host of computer.

* #send- passwords, drivetree, driveslist, keystrokes, openwindows
> This command will sends passwords (saved browser passwords, FTP, Putty..), directory tree of host (upto level 2), logged keystrokes and windows which are currently open

* #set- email (0:Default,1:URL,2:Update), filename (0: Itself, 1: Others), keystrokes (text)
> This command can set email template (default, download from url, update current template with text you'll send), rename filenames, insert keystrokes in host :D

* #start- website (URL), keylogger, recaudio (time), webserver (Port), spread
> This command can open website, start keylogger, record audio, start webserver, USB Spreading

* #stop- keylogger, webserver
> This command will stop keylogger or webserver

* #wallpaper- change wallpaper (URL)
> Changes wallpaper of host computer

* #find- openports (host, threads, ports), router
> This command will find open ports and the router the host is using

* #help- print this usage

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
--> Twitter: https://twitter.com/wayfarermj
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
# Requirements
* Install [PyHook](https://sourceforge.net/projects/pyhook/)
* Install [PyWin32](https://sourceforge.net/projects/pywin32/)
* Install [Microsoft Visual C++ Compiler for Python](https://www.microsoft.com/en-us/download/details.aspx?id=44266)
* Install [PyInstaller](http://www.pyinstaller.org/)
