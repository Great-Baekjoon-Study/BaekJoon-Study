def get_score(order, balloons):
    balloons_copy = balloons[:]  # ***원본 보호하기 위해 복사본 쓰기
    score = 0
    for idx in order:
        i = balloons_copy.index(idx)
        if len(balloons_copy) == 1:  # 풍선 하나 남았을 때
            score += balloons_copy[i]
        elif i == 0:  # 맨 왼쪽 풍선
            score += balloons_copy[i+1]
        elif i == len(balloons_copy)-1:  # 맨 오른쪽 풍선
            score += balloons_copy[i-1]
        else:  # 가운데 풍선
            score += balloons_copy[i-1] * balloons_copy[i+1]
        balloons_copy.pop(i)
    return score

# 순열 직접 구현 (백트래킹)
def permute(arr, visited, path, result):
    if len(path) == len(arr):
        result.append(path[:])
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            path.append(arr[i])
            permute(arr, visited, path, result)
            path.pop()
            visited[i] = False

# 메인
T = int(input())
for t in range(1, T+1):
    N = int(input())
    balloons = list(map(int, input().split()))

    balloons_list = []
    visited = [False]*N
    permute(balloons, visited, [], balloons_list)  # 순열 생성

    max_score = 0
    for order in balloons_list:
        max_score = max(max_score, get_score(order, balloons))

    print(f"#{t} {max_score}")
