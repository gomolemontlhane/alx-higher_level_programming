#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            print("{}".format(chr(ord(char) - 32)), end='')
        else:
            print("{}".format(char), end='')

    print()  # Print a new line at the end

if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
