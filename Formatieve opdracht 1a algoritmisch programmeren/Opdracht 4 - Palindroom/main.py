import is_palindrome

string1 = input("geen een string: ");

def is_palindroom_zelf(s):
    if s == s[::-1]:
        print(s, "is een palindroom")
    else:
        print(s, "is geen palindroom")


def is_palindroom_lib(s):
    i = ''.join(reversed(s))

    if s == i:
        print(s, "is een palindroom")
    else:
        print(s, "is geen palindroom")


is_palindroom_zelf(string1)
is_palindroom_lib(string1)
