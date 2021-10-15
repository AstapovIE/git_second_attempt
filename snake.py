n = int(input())
m = int(input())
a = [[0]*m for q in range(n)]
k = 1
i = 0
j = 0
while j < m and i < n:
    if j == m-1:
        i += 1
        while i < n and j >= 0 :
            a[i][j] = k
            i += 1
            j -= 1
            k += 1
        i -= 1
        j += 1
    if i == 0:
        j += 1
        while i < n and j >= 0 :
            a[i][j] = k
            i += 1
            j -= 1
            k += 1
        i -= 1
        j += 1
    if i == n-1:
        j += 1
        while i >= 0 and j < m:
            a[i][j] = k 
            i -= 1
            j += 1
            k += 1
        i += 1
        j -= 1
    else:
        i += 1
        while i >= 0 and j < m:
            a[i][j] = k
            i -= 1
            j += 1
            k += 1
        i += 1
        j -= 1

for q in range(n):
    print(a[q])
