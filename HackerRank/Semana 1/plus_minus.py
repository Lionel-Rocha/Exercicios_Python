def plusMinus(arr):
    size = len(arr)
    greater = 0
    equals = 0
    minor = 0
    for i in range (size):
        if arr[i] > 0:
            greater += 1
        elif arr[i] == 0:
            equals +=1
        else:
            minor += 1

    print("{:.5f}".format(greater/size))
    print("{:.5f}".format(minor/size))
    print("{:.5f}".format(equals/size))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
