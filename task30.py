arr = list(map(int, input().split()))
x = arr[0]
y = arr[1]
n = arr[2]
total = (x * 100 + y) * n
rubles = int(total // 100)
coins = total - rubles * 100 
print(rubles,"руб.",coins,"коп.")