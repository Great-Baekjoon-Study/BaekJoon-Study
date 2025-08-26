"""
N개의 정수로 이루어진 수열이 있을 때,
크기가 양수인 부분수열 중에서
그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000)
둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다.
주어지는 정수의 절댓값은 100,000을 넘지 않는다.

"""

"""
N, M = map(int, input().split())
# N 은 수열의 개수
# M 은 구해야하는 합계

arr = list(map(int, input().split()))
count = 0
for i in range(1, 21):
    # 수열의 개수만큼 반복
    # 12 23 34 45
    # 123 234 345
    for j in range(0, N-i+1):
        if sum(arr[j:j+i]) == M:
            count +=1

print(count)
"""

# ----------------------------------
# 틀린 이유: **'부분수열'**을 구해야 하는데, **'연속된 부분 배열'**을 구하셨습니다.
# 해결책: 재귀나 itertools.combinations를 사용하여 모든 경우의 부분수열을 탐색해야 합니다.

N, M = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

def find(index, current_sum):
    global count

# 종료 조건: 모든 선수를 다 고려했을 때 (마지막 선수 index는 N-1)
    if index == N:
        # 최종 합계가 목표 S와 일치하는지 확인
        if current_sum == M:
            count += 1
        return # 탐색 종료

    # 재귀 파트: 현재 'index'번 값에 대한 결정
    # 1. 이 값을 포함시키는 경우
    find(index + 1, current_sum + arr[index])

    # 2. 이 값을 포함시키지 않는 경우
    find(index + 1, current_sum)


# 맨 처음 시작
find(0, 0)

# ※ S가 0일 때의 예외 처리
# 만약 S=0 이라면, 모든 값를 포함하지 않은 경우도 count가 1 올라감
# (find(0,0) -> find(1,0) -> ... -> find(N,0) 이 경로)
# 문제에서는 "크기가 양수인 부분수열"을 원했으므로,
# 아무것도 선택하지 않은 '공집합' 경우는 제외
if M == 0:
    count -= 1

print(count)

