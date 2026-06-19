n = 3
lis = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        lis[i][j], lis[j][i] = lis[j][i], lis[i][j]
for i in range(n):
    lis[i].reverse()

print(lis)
