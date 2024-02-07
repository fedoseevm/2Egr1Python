from calendar import c
from random import randint

#n = 6
#M = [[0 for _ in range(n)] for _ in range(n)]

#D = {}
#for d in range(1, n + 1):
#    D[d] = []

#ik = 1 + randint(0, 6) / 10 # 0.0 -.5 => 1.0 - 1.5 

#for i in range(1, n + 1):
#    for j in range(1, n + 1):
#        if i > j:
#            w = randint(0, 10) * ik
#            if w >= 5:
#                D[i].append[j]
#                D[j].append[i]


D = {}

n, m = map(int, input().split())

for i in range(n):
    D[i+1] = []
    # D.update({ i+1 : [] })

for _ in range(m):
    p, q = map(int, input().split())
    D[p].append(q)
    D[q].append(p)
print(D)

for i in range(1,n+1):
    if len(D[i]) == 0:
        print("Wiewior sam!")
    else:
        D[i].sort()
        for j in range(len(D[i])):
            print(D[i][j], end=" ")
        print()

# policz sume stopni wierzecholkow grafu
suma = 0
for i in range(1, n + 1):
    suma += len(D[i])
print("Suma stopni wierzecholkow grafu: ", suma)

# znajdz wierzcholek o najwyzszym stopniu
max = 0
for i in range(1, n + 1):
    if len(D[i]) > max:
        max = len(D[i])
print("\nWierzcholek/ki o najwyzszym stopniu: ")
for j in range(1, n + 1):
    if max == len(D[j]):
        wierzcholek = j
        print(wierzcholek)
print(f"o stopniu {max}")

# znajdz wierzcholki samodzielne
print("Wierzcholki samodzielne: ")
for i in range(1, n + 1):
    if len(D[i]) == 0:
        print(i)

# Sprawdz czy uda sie dojsc z wierzcholka x do y

Checked = []
x, y = map(int, input().split())

def dfs(x, y):
    if x == y: 
        Checked.append(y)
        return True
    Checked.append(x)
    for neighbour in D[x]:
        if neighbour not in Checked:
            if dfs(neighbour, y) == True:
                return True
    return False

print(dfs(x, y))
print("Wierzcholki spojne: ", Checked)

# Na lekcji
def DFS(D, visited, node):
    if visited == None:
        visited = []
    visited.append(node)
    for neighbour in D[node]:
        if neighbour not in visited:
            DFS(D, visited, neighbour)
    return visited

wynik = DFS(D, None, 1)
print(wynik)