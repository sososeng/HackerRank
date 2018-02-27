import sys

def aVeryBigSum(n, ar):
    res=0
    for i in range(0,n):
        res = res + ar[i]
    return res

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
