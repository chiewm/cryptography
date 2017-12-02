message = 'xfmdpnf_up_ipnf'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = message.upper()

for key in range(len(LETTERS)):
    translate = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key

            if num < 0:
                num = num + len(LETTERS)

            translate = translate + LETTERS[num]

        else:
            translate = translate + symbol

    print('key #{0}: {1}'.format(key, translate))
