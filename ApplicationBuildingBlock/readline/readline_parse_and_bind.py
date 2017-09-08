try:
    from gnureadline import readline
except ImportError as err:
    import readline

readline.parse_and_bind('tab: complete')    
readline.parse_and_bind('set editing-mode vim')

while True:
    line = input('Prompt: ("stop" to quit): ')
    if line == 'stop':
        break
    print('ENTERED: {!r}'.format(line))