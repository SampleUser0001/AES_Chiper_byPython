# python -m pip uninstall Crypto
# python -m pip uninstall pycrypto
# python -m pip uninstall pycryptodome
# python -m pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def create_aes(password, iv):
    sha = SHA256.new()
    sha.update(password.encode())
    key = sha.digest()
    return AES.new(key, AES.MODE_CFB, iv)

def encrypt(data, password):
    iv = Random.new().read(AES.block_size)
    tmp = create_aes(password, iv).encrypt(data.encode(encoding='shift_jis'))
    return iv + tmp

def decrypt(data, password):
    iv, cipher = data[:AES.block_size], data[AES.block_size:]
    return create_aes(password, iv).decrypt(cipher)