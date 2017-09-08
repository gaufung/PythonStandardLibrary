import getpass

p = getpass.getpass(prompt='What is your favorite color?: ')
if p.lower() == 'blue':
    print('Right, You can go')
else:
    print('Auugle')