import sys
sys.stdin = open("input.txt", "r")

def dfs(balloons):
    # 풍선이 하나 남았으면 자기 자신 점수
    if len(balloons) == 1:
        return balloons[0]

    max_score = 0
    for i in range(len(balloons)):
        # 점수 계산
        if i == 0:  # 맨 왼쪽 풍선
            score = balloons[i+1]
        elif i == len(balloons) - 1:  # 맨 오른쪽 풍선
            score = balloons[i-1]
        else:  # 양옆 다 있는 경우
            score = balloons[i-1] * balloons[i+1]

        # 풍선 하나 제거
        new_balloons = balloons[:i] + balloons[i+1:]

        # 지금 점수 + 이후 점수
        max_score = max(max_score, score + dfs(new_balloons))

    return max_score


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    balloons = list(map(int, input().split()))
    print(f"#{tc} {dfs(balloons)}")