import sys

def diagonalDifference(a):

    resa = 0
    resb = 0
    for i in range(0,len(a)):
        resa = resa + a[i][i]
    c = 0
    for j in range(len(a)-1,-1,-1):
        resb = resb + a[j][c]
        c=c+1

    res = abs(resa-resb)
    return res
if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
