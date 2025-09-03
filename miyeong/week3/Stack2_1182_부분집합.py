# N개의 정수로 이루어진 수열이 있을 때, 
# 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수

N, S = map(int, input().split())
arr = list(map(int, input().split()))

def f(i, N, s):
    global cnt
    if i == N:   # 모든 원소를 다 확인했을 때
        if s == S:
            cnt += 1
        return
    else:
        f(i+1, N, s+arr[i])  # arr[i] 포함
        f(i+1, N, s)         # arr[i] 미포함

cnt = 0
f(0, N, 0)

# 문제 조건: "크기가 양수인 부분수열"
# 공집합도 합이 0이 되므로, S==0인 경우는 공집합을 빼야 함.
if S == 0:
    cnt -= 1

print(cnt)
