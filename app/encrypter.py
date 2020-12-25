import sys
import getpass 

word = input()
password = getpass.getpass('encrypt password> ')

# 暗号化
enc = 'hoge'

sys.stdout.buffer.write(enc)
