import sys

a = str(sys.argv[1])
b = str(sys.argv[2])
count = 0

for i in range(0, len(b)):
    if (a == b[i]):
        count += 1

print('String {} occurred {} times in string {}.'.format(a, count, b))