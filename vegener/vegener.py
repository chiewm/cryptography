
# @Time    : 2017/11/09 11:26
# @Author  : chiewm
# @File    : vigenere.py

ascii = 'abcdefghijklmnopqrstuvwxyz'


keys = [x + y + z for x in ascii for y in ascii for z in ascii]  # aaa-zzz 所有可能的密钥
key_len = 3
# print(keys)

cipher_text = 'edcfaubjaolqfjcoza'
ct_len = len(cipher_text)

for key in keys:
    print(key)
    i = 0
    plaintext = ''
    while i < ct_len:
        j = i % key_len
        k = ascii.index(key[j])
        m = ascii.index(cipher_text[i])
        if m < k:
            m += 26
        plaintext += ascii[m - k]
        i += 1
    print(plaintext)
