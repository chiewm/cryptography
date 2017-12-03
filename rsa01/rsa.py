# @time    :  16:36
# @Autgor  : chiewm
# @File    : rsa.py
import binascii


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


c = '18216896340225001583503863656665847316130632221657655438240262205132406930975'

e = 65537
p = 239073084012164454487474328836629027299
q = 330547507357192934678966158075243820987
n = p * q

d = modinv(e, (p - 1) * (q - 1))

for i in range(len(c)):
    mm = list(c)
    newS = ""
    flag = ""
    fflag = ""
    for j in range(10):
        try:
            print(j)
            mm[i] = str(j)
            newS = ''.join(mm)
            print(newS)
            flag = pow(int(newS), d, n)
            fflag = str(hex(flag))[2:]
            print(binascii.unhexlify(fflag))
        except BaseException:
            pass
