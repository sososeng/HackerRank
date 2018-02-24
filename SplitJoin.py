def split_and_join(line):

    st = line.split(" ")
    st1=""
    for i in st:
        st1 = st1+ i + "-"
    st1= st1[:-1]
    return st1

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
