import fnmatch
import os
pattern = 'fnmatch_*.py'
print('pattern', pattern)
print()

files = os.listdir('.')
for name in files:
    print('Filename: {:<25} {}'.format(
        name, fnmatch.fnmatch(name, pattern)))
