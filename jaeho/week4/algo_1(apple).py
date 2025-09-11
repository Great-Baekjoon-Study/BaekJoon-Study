import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    apple = 0
    # 사과 숫자
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                apple += 1

    P = []
    # 사과 위치
    for num in range(1, apple+1):
        for i in range(N):
            for j in range(N):
                if arr[i][j] == num:
                    P.append([i, j])


    apple_num = 0
    # 처음 먹어야 할 사과의 번호, 인덱스를 받아오기 위해 변수를 둔다
    spin = 0
    start = [0, 0]
    direction = 4
    # 하 좌 상 우
    # 어찌됏건 0,0에서 시작하고
    # 사과는 외곽에서는 나오지 않으니
    # 방향은 오른쪽으로 보면서 시작하면 됨
    for apple_idx_i, apple_idx_j in P:
        # p를 돌면서 사과의 좌표를 받아옴
        if direction == 1:
            # 진행방향이 아래쪽일 때
            if start[0] > apple_idx_i and start[1] < apple_idx_j:
            # 시작하는 i 인덱스보다 사과가 위에 있고 i인덱스 보다 오른쪽에 있으면 우, 상 즉 1사분면
            # 1사분면이면 왼쪽으로 3번 돌아야 함 3번 돌고 나면 방향은 오른쪽을 보고있음
            # 따라서 스핀카운트 3을 먹이고
            # 방향도 같이 3을 먹임
                spin += 3
                direction += 3
                start = P[apple_num]
                apple_num += 1
                if direction > 4:
                    # 방향이 4보다 커졋으면 4를 빼서 정상화 시켜줌
                    direction -= 4
            elif start[0] > apple_idx_i and start[1] > apple_idx_j:
                # 이걸 이제 방향별로 4사분면까지 모든 수를 걍 다 정의해주는것
                # 시작점보다 사과가 위에 있고, 왼쪽에 있으면 2사분면
                spin += 2
                direction += 2
                # 스핀과 방향이 늘어나는 것만 바꿔주면 된다.
                start = P[apple_num]
                apple_num += 1
                if direction > 4:
                    direction -= 4
            elif start[0] < apple_idx_i and start[1] > apple_idx_j:
                # 3사분면
                spin += 1
                direction += 1
                start = P[apple_num]
                apple_num += 1
                if direction > 4:
                    direction -= 4
            elif start[0] < apple_idx_i and start[1] < apple_idx_j:
                # 4사분면도 3바퀴면 갈 수 있음(바닥에 붙어있는 경우가 없기 때문)
                spin += 3
                direction += 3
                start = P[apple_num]
                apple_num += 1
                if direction > 4:
                    direction -= 4

        if direction == 2:
            # 진행방향이 왼쪽일 때
            if start[0] > apple_idx_i and start[1] < apple_idx_j:
            # 1사분면
                spin += 2
                direction += 2
                start = P[apple_num]
                apple_num += 1
                if direction > 4:
                    direction -= 4
            elif start[0] > apple_idx_i and start[1] > apple_idx_j:
                # 2사분면
                spin += 1
                direction += 1
                start = P[apple_num]
                apple_num += 1
                if direction > 4:
                    direction -= 4
            elif start[0] < apple_idx_i and start[1] > apple_idx_j:
                # 3사분면
                spin += 3
                direction += 3
                start = P[apple_num]
                apple_num += 1
                if direction > 4:
                    direction -= 4
            elif start[0] < apple_idx_i and start[1] < apple_idx_j:
                # 4사분면
                spin += 3
                direction += 3
                start = P[apple_num]
                apple_num += 1
                if direction > 4:
                    direction -= 4


        if direction == 3:
            # 진행방향이 위쪽일 때
            if start[0] > apple_idx_i and start[1] < apple_idx_j:
            # 1사분면
                spin += 1
                direction += 1
                start = P[apple_num]
                apple_num += 1
                if direction > 4:
                    direction -= 4
            elif start[0] > apple_idx_i and start[1] > apple_idx_j:
                # 2사분면
                spin += 3
                direction += 3
                start = P[apple_num]
                apple_num += 1
                if direction > 4:
                    direction -= 4
            elif start[0] < apple_idx_i and start[1] > apple_idx_j:
                # 3사분면
                spin += 3
                direction += 3
                start = P[apple_num]
                apple_num += 1
                if direction > 4:
                    direction -= 4
            elif start[0] < apple_idx_i and start[1] < apple_idx_j:
                # 4사분면
                spin += 2
                direction += 2
                start = P[apple_num]
                apple_num += 1
                if direction > 4:
                    direction -= 4

        if direction == 4:
            # 진행방향이 오른쪽일 때
            if start[0] > apple_idx_i and start[1] < apple_idx_j:
            # 1사분면
                spin += 3
                direction += 3
                start = P[apple_num]
                apple_num += 1
                if direction > 4:
                    direction -= 4
            elif start[0] > apple_idx_i and start[1] > apple_idx_j:
                # 2사분면
                spin += 3
                direction += 3
                start = P[apple_num]
                apple_num += 1
                if direction > 4:
                    direction -= 4
            elif start[0] < apple_idx_i and start[1] > apple_idx_j:
                # 3사분면
                spin += 2
                direction += 2
                start = P[apple_num]
                apple_num += 1
                if direction > 4:
                    direction -= 4
            elif start[0] < apple_idx_i and start[1] < apple_idx_j:
                # 4사분면
                spin += 1
                direction += 1
                start = P[apple_num]
                apple_num += 1
                if direction > 4:
                    direction -= 4

    print(f'#{tc} {spin}')

