import urllib2

text = '''Dear Customer,

We could not deliver your item.
You can review and print complete details of shipping duty on your order.
Thanks
PDF Attachment:  update_Form.pdf'''


def setDefaultEmailTemplate(PATH_MAIL_TEMP):
    print '[*] Setting default email template'
    template_file = open(PATH_MAIL_TEMP,'w')
    template_file.write(text)
    template_file.close()
    
def setEmailTemplate(PATH_MAIL_TEMP, URL):
    print '[*] Setting email template'
    data = urllib2.urlopen(URL)
    data = data.split("\n")
    template_file = open(PATH_MAIL_TEMP,'w')
    template_file.write(data)
    template_file.close()
    
def updateEmailTemplate(PATH_MAIL_TEMP, data):
    print '[*] Updating email template'
    template_file = open(PATH_MAIL_TEMP,'w')
    template_file.write(data)
    template_file.close()