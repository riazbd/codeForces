n = int(input())

count = 0
i = 0
while i < n:
    a, b, c = map(int, input().split())
    solves = [a, b, c]

    if solves.count(1) >= 2:
        count += 1
    i += 1
print(count)
