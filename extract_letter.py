import sys

word = sys.argv[1]
letter = sys.argv[2]
new_word = ''.join([i for i in word if i != letter])

print(new_word)