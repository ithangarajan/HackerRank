def swap_case(s):
    result=""
    for counter in range(0,len(s)):
        if s[counter].isupper():
            result=result+(s[counter].lower())
        else:
            result=result+(s[counter].upper())
    return result