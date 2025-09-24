# 숫자가 적힌 N개의 풍선들이 나란히 서 있음.
# 손님에게 게임총과 N개의 총알들이 주어짐.
# 손님은 N번 쏴서 풍선을 터트리면 점수를 얻음.
# 풍선이 터지고 난 뒤 터지지 않은 풍선들은 일정한 간격을 가지도록 이동
# 최종적으로 획득한 점수에 따라 경품을 받음.
# 점수는 0점부터 시작
# 풍선이 터지면, 좌와 우로 이웃한 풍선에 적힌 두 숫자들의 곱으로 점수를 얻음.
# 좌와 우로 한쪽만 이웃하는 풍선이 있는 경우, 이웃한 풍선에 적힌 숫자 만큼 점수를 얻음.
# 좌와 우로 이웃하는 풍선이 없는 경우, 터진 풍선에 적힌 숫자 만큼 점수를 얻음.
# 어떤 풍선도 터트리지 못한 경우, 점수를 얻지 못함.
# 숫자가 적힌 N개 풍선이 주어질 때 사격 게임에서 얻을 수 있는 최대 점수 계산
# 풍선이 동시에 2개 이상 터지는 경우는 없음.

# 이거는 무조건 재귀 써야될 것 같은데...
# 일단 첫번째 경우의 점수를 획득하고
# 나머지는 그 점수보다 큰 거 업데이트

# 1 20
# 2 100
# 3 16057
# 4 561630
# 5 6455522

import sys
sys.stdin = open('sample_input (3).txt', 'r')


# i : 몇 번째 풍선인지
# cnt : 터트린 풍선의 개수
# N : 풍선 개수
def game(i, cnt, N):
    global score
    global max_score
    global total
    global game_setting
    global order

    if 0 <= i-1 and i+1 < N: # 좌우로 이웃한 풍선이 있는 경우
        score += game_setting[i-1] * game_setting[i+1]
    elif 0 > i-1 and i+1 < N: # 우에만 이웃한 풍선이 있는 경우
        score += game_setting[i+1]
    elif 0 <= i-1 and i+1 >= N: # 좌에만 이웃한 풍선이 있는 경우
        score += game_setting[i-1]
    elif 0 > i-1 and i+1 >= N: # 좌우에 이웃하는 풍선이 없는 경우
        score += game_setting[i]

    order.append(i)
    game_setting.remove(game_setting[i]) # 터트린 풍선 삭제
    N -= 1 # 전체 풍선 개수도 1 감소

    if N == 0:
        if max_score < score:
            max_score = score
            print(max_score)
        cnt = 0 # 다음 경우의 수도 살펴봐야 되니까 cnt 초기화
        game_setting = balloons[:]  # 게임할 때는 터트린 풍선들을 삭제할 거니까 풍선을 담은 리스트 하나 더 만듦.
        score = 0
        order = []
        return

    for j in range(N):
        game(j, cnt+1, N)



T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    N = int(input()) # 풍선의 개수
    balloons = list(map(int, input().split())) # 풍선에 적힌 숫자 N개

    total = N # 초기 상태의 풍선 개수
    max_score = 0 # 게임에서 얻을 수 있는 최대 점수
    cnt = 0  # 터트린 풍선 개수
    game_setting = balloons[:]  # 게임할 때는 터트린 풍선들을 삭제할 거니까 풍선을 담은 리스트 하나 더 만듦.
    score = 0 # 게임 한판동안의 점수
    order = []

    for i in range(N):
        game(i, 0, N)

    print(f'#{test_case} {max_score}')

