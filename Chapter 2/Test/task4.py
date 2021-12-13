figura = input()
slon = input()

print("YES" if abs(ord(figura[0]) - ord(slon[0])) == abs(int(figura[1]) - int(slon[1])) else "NO")