from random import randint

uid_chars = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0')


def long_uid():
    count = len(uid_chars) - 1
    c = ''
    for i in range(0, 40):
        c += uid_chars[randint(0, count)]
    return c
