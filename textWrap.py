import textwrap

def wrap(string, max_width):

    st = textwrap.wrap(string,max_width)

    st1 = ""

    for i in st:
        st1= st1+ i + "\n"

    return st1


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
