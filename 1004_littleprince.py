##두 점중 하나만 행성계 내부에 존재할 떄 res + 1

import math

def calc_dist(x,y,c1,c2):
    return math.sqrt((x-c1)**2 + (y-c2)**2)
    
trial = int(input())        #num of test case

for _ in range(trial):
    x1, y1, x2, y2 = input().split()
    x1, y1, x2, y2 =  int(x1), int(y1), int(x2), int(y2)
    n = int(input())
    cnt = 0

    for _ in range(n):
        din1, din2 = False, False
        c1, c2, r = input().split()
        c1, c2, r = int(c1), int(c2), int(r)

        d1 = calc_dist(x1,y1,c1,c2)
        d2 = calc_dist(x2,y2,c1,c2)

        if d1 > r : din1 = True
        if d2 > r : din2 = True

        cnt = cnt + (din1 ^ din2)

    print(cnt)