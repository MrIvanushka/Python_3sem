n, m = map(int, input().split())
windowCount = int(input())

wall = [[False for i in range(m)] for j in range(n)]
wall_is_good = True

for i in range(windowCount):
    minX, maxX, minY, maxY = map(int, input().split())
    for x in range(minX, maxX):
        for y in range(minY, maxY):
            if x >= 0 and y >= 0 and x < n and y < m:
                if wall[x][y] == True:
                    wall_is_good = False
                    break
                wall[x][y] = True
            else:
                wall_is_good = False

if wall_is_good:
    print("correct")
else:
    print("broken")