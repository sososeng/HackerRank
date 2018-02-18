if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr = list(arr)
    arr.sort()

    num = arr[len(arr)-1]
    for i in range(len(arr)-1, -1, -1):
        if arr[i] < num:
            print (arr[i])
            break
