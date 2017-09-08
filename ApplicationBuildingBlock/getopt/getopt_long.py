import getopt
opts, args = getopt.getopt(
    ['--noarg',
    '--witharg','val',
    '--withargs2=another'],
    '',
    ['noarg', 'witharg=', 'withargs2=']
)
for opt in opts:
    print(opt)