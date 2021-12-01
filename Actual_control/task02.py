class Lantern:
    def __init__(self, IL):
        self.x = int(IL[0])
        self.y = int(IL[1])
        self.range = int(IL[2])

N, M = map(int, input().split())
K = int(input())
Lanterns = []
lightMap = [[False for y in range(M)] for x in range(N)]
darkCount = N * M
for i in range(K):
    nL = Lantern(input().split())
    for x in range(nL.x - nL.range, nL.x + nL.range + 1):
        for y in range(nL.y - nL.range, nL.y + nL.range + 1):
            if x >= 0 and y >= 0 and x < N and y < M:
                if lightMap[x][y] == False:
                    darkCount -= 1
                    lightMap[x][y] = True
print(darkCount)


