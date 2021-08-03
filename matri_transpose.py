n = int(input().strip())
#m = int(input().strip())
a = [[0]*n for _ in range(n)]
for i in range(n):
    a[i] = list(input().strip())
print(' '.join(a.__str__()))
print(*zip(*a))