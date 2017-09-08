import getpass
try:
    p=getpass.getpass()
except Exception as err:
    print('ERROR', err)
else:
    print('You Enter', p)