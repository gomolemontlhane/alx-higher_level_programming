#!/usr/bin/python3

for char in range(ord('a'), ord('z') + 1):
    if chr(char) not in ['q', 'e']:
        print(chr(char), end='')

print()  # Print a new line at the end