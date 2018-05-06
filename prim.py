MAX = 10000
INF = 10000-1
low_cost = [0,0,0,0,0,0,0]
adjacent = [[INF,   8,   5,   1, INF, INF, INF],
            [  8, INF, INF,   6,   2, INF, INF],
            [  5, INF, INF,   6, INF,   4, INF],
            [  1,   6,   6, INF,   4,   3,   5],
            [INF,   2, INF,   4, INF, INF,   3],
            [INF, INF,   4,   3, INF, INF,   7],
            [INF, INF, INF,   5,   3,   7, INF]
            ]
def prim():
    for i in range(0,7):
        low_cost[i] = adjacent[0][i]
    for j in range(1,7):
        min = low_cost[1]
        k = 1
        for kp in range(2,7):
            if min > low_cost[kp]:
                min = low_cost[kp]
                k = kp
        low_cost[k] = MAX
        for r in range(1,7):
            if low_cost[r] < MAX and low_cost[r] > adjacent[k][r]:
                low_cost[r] = adjacent[k][r]
                print(low_cost)
prim()
