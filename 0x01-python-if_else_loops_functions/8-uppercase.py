#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        get_ord = ord(str[i])
        if get_ord > 96:
            get_ord = 65 + (get_ord - 97)
        print("{}".format(chr(get_ord)), end="")
    print()
