if __name__ == '__main__':
    n = int(input())
    sn = str(n)
    valide = True
    if n<100000 or n > 999999:
        valide=False
    else:
        for i in range(0, len(sn)-1):
            if sn[i]== sn[i+1]:
                valide=False
                break
    print(valide)
