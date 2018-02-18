if __name__ == '__main__':
    mylist=[]
    N = int(input())

    for i in range(0,N):
        st = str(input())
        st1 = st.split(" ")
        if mylist != None:
            if st1[0] == "insert":
                mylist.insert(int(st1[1]),int(st1[2]))
            elif st1[0] == "print":
                print(mylist)
            elif st1[0] == "remove":
                mylist.remove(int(st1[1]))
            elif st1[0] == "append":
                mylist.append(int(st1[1]))
            elif st1[0] == "sort":
                mylist.sort()
            elif len(mylist)>0 and  st1[0] == "pop":
                mylist.pop()
            elif st1[0] == "reverse":
                mylist.reverse()
