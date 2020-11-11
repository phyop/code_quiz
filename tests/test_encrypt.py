import pytest

from base64 import urlsafe_b64encode, urlsafe_b64decode

from quiz.encrypt import FileNameCipher


@pytest.fixture
def cipher():
    return FileNameCipher()


def test_name_cipher_encode(cipher):
    expected = 'MyFilename'
    ciphertext = cipher.encode(expected)
    plaintext = urlsafe_b64decode(ciphertext).decode('utf-8')
    assert plaintext == expected


def test_name_cipher_decode(cipher):
    expected = 'MyFilename'
    ciphertext = urlsafe_b64encode(expected.encode('utf-8'))
    plaintext = cipher.decode(ciphertext)
    assert plaintext == expected
