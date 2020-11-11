import io
from base64 import urlsafe_b64encode, urlsafe_b64decode
import binascii


class FileNameCipher(object):
    ''' Simulate a cipher with base64 encode/decode
    '''

    def encode(self, name):
        return urlsafe_b64encode(name.encode('utf-8'))

    def decode(self, ciphertext):
        name = urlsafe_b64decode(ciphertext)
        return name.decode('utf-8')
