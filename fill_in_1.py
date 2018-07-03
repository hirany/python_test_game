
def disp(list, l):
    for i in range(l):
        for k in range(l):
            print(list[k][i], end=' ')
        print()
    print()

def scan(list, l):
    x = int(input('x = '))
    y = int(input('y = '))
    print()
    if x < 0 or l-1 < x or y < 0 or l-1 < y:
        return 1
    rev(list, x, y, l)

def rev(list, x, y, l):
    if y:
        list[x][y-1] = int(not list[x][y-1])
    if not (y == l-1):
        list[x][y+1] = int(not list[x][y+1])
    if x:
        list[x-1][y] = int(not list[x-1][y])
    if not (x == l-1):
        list[x+1][y] = int(not list[x+1][y])

def filin(list, l):
    for i in range(l):
        for k in range(l):
            if list[i][k] == 0:
                return 0
    return 1

# mainprocessing
l = int(input('level = '))
list = [[0 for i in range(l)] for k in range(l)]
disp(list, l)
c = 0

while 1:
    if scan(list, l):
        c = 'miss'
        break
    c += 1
    disp(list, l)
    if filin(list, l):
        c = 'complete!!\ncount: ' + str(c)
        break

print(c)