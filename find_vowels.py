import sys
count = 0
arg = sys.argv[1]
for i in arg:
    if i in 'aeiou':
        count += 1
print('{} contains {} vowels.'.format(arg, count))
