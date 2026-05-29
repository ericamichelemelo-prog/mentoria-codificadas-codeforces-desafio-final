n = int(input())
groups = list(map(int, input().split()))
g4 = groups.count(4)
g3 = groups.count(3)
g2 = groups.count(2)
g1 = groups.count(1)
taxis = g4
taxis += g3
g1 = max(0, g1 - g3)
taxis += g2 // 2
g2 = g2 % 2
if g2 == 1:
    taxis += 1
    g1 = max(0, g1 - 2)
if g1 > 0:
    taxis += (g1 + 3) // 4
print(taxis)