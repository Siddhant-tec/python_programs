def gcd():
    arr = [5, 2, 4, 3, 1]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            while arr[j] != 0:
                (arr[i], arr[j]) = (arr[j], arr[i] % arr[j])
        print(arr[i])


gcd()
