def increasing_substring():
    size = int(input())
    alphabets = list(input())
    count = [1] * size
    for i in range(1, size):
        if alphabets[i - 1] < alphabets[i]:
            count[i] = count[i - 1] + 1
    return " ".join(map(str, count))


inp = int(input())
for value in range(0, inp):
    print("Case #" + str(value + 1) + ":", end=" ")
    print(increasing_substring())
