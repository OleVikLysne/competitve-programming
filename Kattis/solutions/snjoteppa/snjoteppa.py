from sys import stdin, stdout



def yes():
    stdout.write("Jebb\n")

def no():
    stdout.write("Neibb\n")

n, k = map(int, stdin.readline().split())
m = {
    ".": 0,
    "o": 1
}
grid = [[m[x] for x in stdin.readline().rstrip()] for _ in range(2)]

def behind(i, j):
    if j-1 >= 0:
        return (i+1) % 2, j-1

def same(i, j):
    return (i+1) % 2, j

def front(i, j):
    if j+1 < n:
        return (i+1) % 2, j+1
    
    

def behind_same(i, j):
    b = behind(i, j)
    if b is not None:
        yield behind(i, j)
    yield same(i, j)

def around(i, j):
    yield from behind_same(i, j)
    f = front(i, j)
    if f is not None:
        yield f

blocked = 0

for i in range(2):
    for j in range(n):
        if grid[i][j]:
            for x, y in behind_same(i, j):
                if grid[x][y]: blocked += 1

for _ in range(k):
    inp = stdin.readline().split()
    if len(inp) == 1:
        if not blocked:
            yes()
        else:
            no()
        continue
    i, j = int(inp[1])-1, int(inp[2])-1
    if grid[i][j]:
        grid[i][j] = 0
        for x, y in around(i, j):
            if grid[x][y]:
                blocked -= 1
    
    else:
        grid[i][j] = 1
        for x, y in around(i, j):
            if grid[x][y]:
                blocked += 1






