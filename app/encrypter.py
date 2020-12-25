import sys
import getpass 
import my_aes

word = input('word> ');
password = getpass.getpass('encrypt password> ')

# 暗号化
# enc = my_aes.encrypt(sys.tsdin.buffer.read(), password)
# enc = my_aes.encrypt(word, password)
enc = my_aes.encrypt(word, password).decode(encoding='cp932')
sys.stdout.buffer.write(enc)
