s = '8820410104084108421088204108421042042081021010840102102108421088410842088408821'
d = 'abcdefghijklmnopqrstuvwxyz'
m = ''
c = 0
for i in s:
    c = int(i) + c

    if i == '0':
        m = m + d[c-1]
        c = 0

print(m)



