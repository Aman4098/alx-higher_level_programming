#!/usr/bin/python3
# Author - Bamidele Adefolaju
def uppercase(str):
"""Print a string in uppercase."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122: 
            c= chr(ord(c) - 32)
        print("{}".format(c), end="")
print("")
#!/usr/bin/env python3
uppercase = __import__('8-uppercase').uppercase
uppercase("best")
uppercase("Best School 98 Battery street")
