if __name__ == '__main__':
    n = int(input())
    slist=[]
    for _ in range(0,n):
        templ = []
        name = input()
        score = float(input())
        templ.append(name)
        templ.append(score)
        slist.append(templ)

        first = 0.0
        sec = 0.0
    for i in range(0,len(slist)):
        if(first< slist[i][1]):
            sec = first
            first = slist[i][1]

    listp = []
    for i in range(0,len(slist)):
        if(sec == slist[i][1]):
            listp.append(slist[i][0])

    listp.sort()

    for i in range(0,len(listp)):
        print(listp[i])
