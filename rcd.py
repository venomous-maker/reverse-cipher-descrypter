print('   R E V E R S E  C I P H E R  D E S C R I P T O R')

print("""\
CODED BY:
  .___.     ..___ .___.___   .      ..___.   ..___..    .
  |    \   / |   \|   |    |  \    / |   |\  ||   ||\  /|
  |     \ /  |———/|———|———/    \  /  |———| \ ||   || \/ |
  |____  |   |___/|___|    \    \/   |___|  \||___||    |.
         @cybervenomous on telegram
         https://darktelegramvenomous my channel
""""")
message = input('Type or paste the cipher here:''  ')
translated = ''
i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print('''\
     ....................................................
     Your Encrypted Text Is:
''')
print("      "+translated)
print('     ....................................................')
print('''\
___________________________________________________________
___________________________________________________________
       T H A N K    Y O U    F O R   U S I N G    M E !
                  To be updated soon
                   Copy with credits
___________________________________________________________
___________________________________________________________
''')
