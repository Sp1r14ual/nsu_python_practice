n, k, m = map(int, input().split())
if k < m:
    path1 = n - m + k - 1
    path2 = m - k - 1
    print(min(path1, path2))
elif k > m:
    path1 = n - k + m - 1
    path2 = k - m - 1
    print(min(path1, path2))
else:
    print(0)