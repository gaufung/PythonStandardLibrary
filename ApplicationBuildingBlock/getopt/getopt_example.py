from getopt import getopt, GetoptError
import sys

version = '1.0'
verbose = False
output_stream = 'default.out'
print('ARG:         ', sys.argv[1:])

try:
    options, reminder = getopt(
        sys.argv[1:],
        'o:v',
        ['output=',
        'verbose',
        'version=']
        )
except GetoptError as err:
    print('Errors:', err)

for opt, arg in options:
    if opt in ('-o', '--output'):
        output_stream = arg
    elif opt in ('-v', 'verbose'):
        verbose = True
    elif opt == '--version':
        version = arg

print('VERSION   :', version)
print('VERBOSE   :', verbose)
print('OUTPUT    :', output_stream)
print('REMAINING :', reminder)