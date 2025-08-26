# 깃발은 N행 M열로 나뉘어 있고, 각 칸은 흰색, 파란색, 빨간색 중 하나로 칠해져 있음.
# 몇 개의 칸에 있는 색을 다시 칠해서 이 깃발을 러시아 국기처럼 만들려고 함.
# 위에서 몇 줄(한 줄 이상)은 모두 흰색으로 칠해져 있어야 함.
# 다음 몇 줄(한 줄 이상)은 모두 파란색으로 칠해져 있어야 함.
# 나머지 줄(한 줄 이상)은 모두 빨간색으로 칠해져 있어야 함.
# 러시아 국기 같은 깃발을 만들기 위해서 새로 칠해야 하는 칸의 개수의 최솟값 구하기
# W : 흰색, B : 파란색, R : 빨간색

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    N, M = map(int, input().split()) # N x M 크기의 깃발
    flag = [input() for _ in range(N)] # 깃발 데이터

    # 행 단위로 다시 칠해야 하는 칸 수
    count = []
    for f in flag:
        count.append({
            'W' : sum(1 for c in f if c != 'W'),
            'B' : sum(1 for c in f if c != 'B'),
            'R' : sum(1 for c in f if c != 'R')
        })

    min_c = float('inf') # 새로 칠해야 하는 칸의 개수의 최솟값

    # 무조건 첫 줄은 흰색, 마지막줄은 빨간색이어야 함.
    # 흰색 구간의 끝 지점 i, 파란색 구간의 끝 지점 j을 정하면 나머지 줄은 자동으로 빨간색 구간
    for i in range(0, N-2):
        for j in range(i+1, N-1):
            new = 0  # 새로 칠해야 하는 칸의 개수
            # 흰색 구간 : 0 ~ i
            for k in range(0, i+1):
                new += count[k]['W']
            # 파란색 구간 : i+1 ~ j
            for k in range(i+1, j+1):
                new += count[k]['B']
            for k in range(j+1, N):
                new += count[k]['R']

            if min_c > new:
                min_c = new

    print(f'#{test_case} {min_c}')