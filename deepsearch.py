adjacentlist = [[1,2],#A
                [0,2,3],#B
                [0,1,4],#C
                [1,4,5],#D
                [2,3,6],#E
                [3],#F
                [4]]#G

def search(goal,now_here):
    if goal==now_here:
        start.append(now_here)
        print(start)
    if now_here not in start:
        start.append(now_here)
        for i in adjacentlist[now_here]:
            if i not in start:
                search(goal,i)
                start.pop()



start = []
search(6,0)
