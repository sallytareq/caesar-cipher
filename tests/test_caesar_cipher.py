from caesar_cipher import __version__
from caesar_cipher.caeser_cipher import *


def test_version():
    assert __version__ == '0.1.0'

def test_encrypt_one():
    actual = encrypt('Hello' , 1)
    expected = 'ifmmp'
    assert expected == actual

def test_encrypt_twenty_seven():
    actual = encrypt('Hello' , 27)
    expected = 'ifmmp'
    assert expected == actual

def test_encrypt_forty():
    actual = encrypt('Hello' , 30)
    expected = 'lipps'
    assert expected == actual

def test_decrypt_with_key():
    actual = decrypt('mjqqt' , 5)
    expected = "hello"
    assert expected == actual

def test_decrypt_no_key():
    actual = decrypt('QEB NRFZH YOLTK CLU GRJMP LSBO QEB ALD')
    expected = "Key: 23 \nDecrypted message: the quick brown fox jumps over the dog"
    assert expected == actual
