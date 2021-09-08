n, m = [int(i) for i in input().split(" ")]
windowCount = int(input())

wall = [[False for i in (m - 1)] for j in (n - 1)]
wall_is_good = True

for i in range(windowCount):
    minX, maxX, minY, maxY = [int(i) for i in input().split(" ")]
    for x in range(minX, maxX):
        for y in range(minY, maxY):
            if wall[x][y] == True:
                wall_is_good = False
            wall[x][y] = True

if wall_is_good:
    print("correct")
else:
    print("broken")