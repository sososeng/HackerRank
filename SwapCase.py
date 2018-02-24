def swap_case(s):
    st = ""
    for i in range(0,len(s)):
        if s[i].isupper():
            st= st+ s[i].lower()
        elif s[i].islower():
            st= st + s[i].upper()

        else:
            st= st + s[i]
    return st

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
