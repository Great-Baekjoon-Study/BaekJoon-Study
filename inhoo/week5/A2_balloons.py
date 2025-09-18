
# 풍선 터뜨리기 순서에 대해서 총점 계싼
def get_score(order, balloons):
    balloons_copy = balloons[:]  # ***ballons 리스트를 훼손하지 않도록 복사본 쓰기
    
    
    score = 0
    for idx in order: # order: 풍선들의 순서가 담긴 order 리스트를 반복, idx: 현재 터뜨릴 풍선
        i = balloons_copy.index(idx)
        if len(balloons_copy) == 1:  # 풍선 하나 남았을 때
            score += balloons_copy[i] # 이 풍선의 숫자를 점수에 더하고
        elif i == 0:  # 맨 왼쪽 풍선
            score += balloons_copy[i+1] # 오른쪽 이웃한 풍선의 숫자를 점수에 더하기
        elif i == len(balloons_copy)-1:  # 맨 오른쪽 풍선
            score += balloons_copy[i-1] # 왼쪽 이웃 풍선의 숫자를 점수에 더합니다.
        else:  # 가운데 풍선
            score += balloons_copy[i-1] * balloons_copy[i+1] # 좌우 이웃한 풍선들의 숫자의 곱
        balloons_copy.pop(i) # 점수를 계산한 후, 풍선을 리스트에서 제거 
    return score

# 순열 직접 구현 (백트래킹)
def permute(arr, visited, path, result):
    if len(path) == len(arr): # 순열이 완성됨.
        result.append(path[:])
        return
    for i in range(len(arr)): # 첫번째 풍선부터 탐색 시작
        if not visited[i]:
            visited[i] = True
            path.append(arr[i]) #현재 순열에 이 풍선 추가
            permute(arr, visited, path, result) #다음풍선 선택
            path.pop()
            visited[i] = False


# 메인
T = int(input())
for t in range(1, T+1):
    N = int(input())
    balloons = list(map(int, input().split())) # 풍선들의 번호를 리스트로ㅗ 받고

    balloons_list = [] # 모든 순열을 저장할 빈 리스트
    visited = [False]*N  # permute 함수에서 각 풍선이 현재 순열에 이미 사용되었는지 여부 추적
    permute(balloons, visited, [], balloons_list)  # 순열 생성

    max_score = 0
    for order in balloons_list:
        max_score = max(max_score, get_score(order, balloons))

    print(f"#{t} {max_score}")
