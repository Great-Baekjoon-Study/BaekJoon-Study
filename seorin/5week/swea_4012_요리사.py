import sys
sys.stdin = open('input.txt', 'r')


def recur(idx, cnt):
    global min_taste
    
    if cnt == N // 2 :
        # 그럼 A에 없는 게 B에 있으면 됨
        B = [i for i in range(N) if i not in A]
        A_taste = cal_synergy(A) 
        B_taste = cal_synergy(B)
        min_taste = min(min_taste, abs(A_taste - B_taste))
        return
    
    if idx >= N:
        return
    
    A.append(idx)
    recur(idx+1, cnt+1)
    A.pop()

    recur(idx+1, cnt)

def cal_synergy(food):
    total = 0
    
    for i in range(len(food)):
        for j in range(i+1, len(food)):
            total += synergy[food[i]][food[j]] + synergy[food[j]][food[i]]

    return total 


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    A = []
    min_taste = float('inf')

    recur(0, 0)
    print(f"#{tc} {min_taste}")


    

