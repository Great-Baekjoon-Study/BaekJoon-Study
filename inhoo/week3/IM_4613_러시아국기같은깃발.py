T = int(input())

def count_color(start, end, color): # 행,  알파벳
    cnt_work = 0
    for p in range(start, end+1): #자신 포함 위까지
        for q in range(M):
            if arr[p][q] != color:
                cnt_work += 1
    return cnt_work

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]



    total_cnt_list = []

    for i in range(0,N-2):   #i의 범위는 0~N-3 :i는 1이상이어야 됨. 0무조건 포함
        for j in range(i+1,N-1):   #j의 범위는 N-2
            total_cnt = 0
            total_cnt += count_color(0, i, 'W')
            total_cnt += count_color(i+1, j, 'B')
            total_cnt += count_color(j+1, N-1,  'R')
            total_cnt_list.append(total_cnt)



    print(f'#{tc} {min(total_cnt_list)}')


