import math
n, m, a = map(int, input().split())
flagStones = math.ceil(n/a)*math.ceil(m/a)

print(flagStones)
