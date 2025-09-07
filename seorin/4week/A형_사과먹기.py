import sys
sys.stdin = open("input.txt", "r")

def turn(a, b):
    return (b - a) % 4   # a에서 b로 가려면 시계방향으로 몇 번 도는지

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    graph = [list(map(int, input().split())) for _ in range(N)]

    # 사과 위치 구하기 
    # key = 사과 번호, value = 사과 좌표
    apples = {}
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0:
                apples[graph[i][j]] = (i, j)
                cnt += 1

    x, y = 0, 0
    d = 1   # 현재 방향
    turns = 0

    for i in range(1, cnt+1):
        ax, ay = apples[i]

        # 0 = 위 / 1 = 오른쪽 / 2 = 아래 / 3 = 왼쪽 (시계방향)
        # 상하좌우 중에 다음 사과가 현재 사과 기준 어디에 있는지 확인 
        row = 2 if ax > x else 0   # 아래 / 위
        col = 1 if ay > y else 3   # 오른쪽 / 왼쪽

        # 두 가지 순서(가로→세로 / 세로→가로) 중 회전 수가 작은 걸 선택
        t1 = turn(d, col) + turn(col, row)
        t2 = turn(d, row) + turn(row, col)

        if t1 <= t2:
            turns += t1
            d = row  
        else:
            turns += t2
            d = col

        x, y = ax, ay

    print(turns)
