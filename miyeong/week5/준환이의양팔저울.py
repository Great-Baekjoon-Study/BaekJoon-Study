# n! 계산
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# cnt : 지금까지 올린 추의 개수
# left : 현재 왼쪽 저울에 올라간 총 무게
# right : 현재 오른쪽 저울에 올라간 총 무게
# remain : 아직 올리지 않은 추들의 무게 합
def recur(cnt, left, right, remain):
    global answer
    
    # 가지치기 1 : 오른쪽이 더 무거워지면 불가능
    if left < right:
        return 
    
    # 가지치기 2 : 왼쪽이 남은 무게 다 합쳐도 항상 무거운 경우
    # 이후 배치 방법은 모두 유효하므로 경우의 수를 한 번에 더함
    if left >= right + remain:
        k = N - cnt # 아직 놓지 않은 추의 개수
        # 남은 추들을 놓는 방법 = (순서 경우의 수 k!) x (양쪽 선택 2^k)
        answer += factorial(k) * (2 ** k)
        return
    
    # 아직 남은 추가 있으면 하나씩 선택해서 배치 시도
    for i in range(N):
        if not used[i]:
            used[i] = 1

            # i번 추를 왼쪽에 놓기
            recur(cnt + 1, left + weights[i], right, remain - weights[i])

            # i번 추를 오른쪽에 놓기
            recur(cnt + 1, left, right + weights[i], remain - weights[i])

            used[i] = 0

T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 무게 추와 양팔저울의 개수
    weights = list(map(int, input().split())) # 각 무게추의 무게

    used = [0] * N
    answer = 0 # 양팔 저울에 모든 무게추를 올리는 방법 수
    total_weight = sum(weights)

    recur(0, 0, 0, total_weight)

    print(f'#{test_case} {answer}')
