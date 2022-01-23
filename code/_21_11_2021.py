import cv2
import random
import numpy as np
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
SCALE = 10
S = 800
h = 10
w = 20
mult = min(S//h, S//w)
h1 = h*mult
w1 = w*mult
def paint(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if nul[y//mult][x//mult] == 0:
            nul[y//mult][x//mult] = 255
        else:
            nul[y//mult][x//mult] = 0
nul = np.zeros((h, w))
w = 0
cv2.namedWindow('im')
cv2.setMouseCallback('im', paint)
while(1):
    img = cv2.resize(nul, (w1, h1), interpolation=cv2.INTER_AREA)
    cv2.imshow('im', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

def findCrossroads(im):
    start = []
    f = im.shape
    le = f[1]
    wid = f[0]
    k = 0
    for i in range(0, wid):
        for j in range(0, le):
            for di, dj in moves:
                if wid > i + di >= 0 \
                    and le > j + dj >= 0 \
                    and sum(nul[i+di][j+dj]) == 255*3:
                    k += 1
            if k > 2:
                im[i][j][0] = random.randint(0,255)
                im[i][j][1] = random.randint(0,255)
                im[i][j][2] = random.randint(0,255)
                start.append([i, j])
            k = 0
    return start

def findColoredPixels(im):
    st = []
    f = im.shape
    le = f[1]
    wid = f[0]
    for i in range (1, wid-1):
        for j in range (1, le-1):
            if sum(img[i][j]) != 255*3:
                st.append([i, j])
    return st

def bfs(im, start):
    w, h = im.shape[:2]
    queue = start
    while len(queue) > 0:
        x, y = queue.pop(0)
        for dx, dy in moves:
            if w > x + dx >= 0 \
               and h > y + dy >= 0 \
               and sum(nul[x+dx][y+dy]) == 255*3:
                im[x+dx][y+dy] = im[x][y]
                queue.append([x+dx, y+dy])

nul3 = np.asarray([[[nul[i][j], nul[i][j], nul[i][j]] for i in range(w) ] for j in range(h)])
print(nul)
print(nul3)
cv2.waitKey(0)

start = findCrossroads(nul3)
bfs(nul3, start)

nul3 = cv2.resize(nul3, (w1, h1), interpolation=cv2.INTER_AREA)
cv2.imshow("haha", nul3)
cv2.waitKey(0)
cv2.destroyAllWindows()