message = input('What is the message?')
translated = ''
i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print('Your Encrypted Text Is:' " " +translated)
