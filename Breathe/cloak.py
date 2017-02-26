import os
import sys
import zlib

from optparse import OptionError
from optparse import OptionParser

class Cloaking():

    def __init__(self):
        pass

    def hideAscii(self, data):
        retVal = ""
        for i in xrange(len(data)):
            if ord(data[i]) < 128:
                retVal += chr(ord(data[i]) ^ 127)
            else:
                retVal += data[i]

        return retVal

    def obfs(self, inputFile=None, data=None):
        if data is None:
            with open(inputFile, "rb") as f:
                data = f.read()

        return self.hideAscii(zlib.compress(data))

    def deobfs(self, inputFile=None, data=None):
        if data is None:
            with open(inputFile, "rb") as f:
                data = f.read()
        try:
            data = zlib.decompress(self.hideAscii(data))
        except:
            print 'ERROR: the provided input file \'%s\' does not contain valid cloaked content' % inputFile
            sys.exit(1)
        finally:
            f.close()

        return data

    def run(self, inputF, outputF):

        inputFile = inputF
        outputFile = outputF
        
        data = self.obfs(inputFile)

        f = open(outputFile, 'wb')
        f.write(data)
        f.close()
