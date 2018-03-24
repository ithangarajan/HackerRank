if __name__ == '__main__':
    alnum = False
    alpha = False
    digit = False
    upper = False
    lower = False
    s = input()
    for counter in range(0, len(s)):
        if s[counter].isalnum() == True:
            alnum = True
        if s[counter].isalpha() == True:
            alpha = True
        if s[counter].isdigit() == True:
            digit = True
        if s[counter].islower() == True:
            lower = True
        if s[counter].isupper() == True:
            upper = True

    if alnum == True:
        print("True")
    else:
        print("False")
    if alpha == True:
        print("True")
    else:
        print("False")

    if digit == True:
        print("True")
    else:
        print("False")

    if lower == True:
        print("True")
    else:
        print("False")

    if upper == True:
        print("True")
    else:
        print("False")