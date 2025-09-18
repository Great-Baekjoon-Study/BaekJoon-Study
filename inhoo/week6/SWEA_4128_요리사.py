# 다시 풀어보기

def synergy(lst):
    total = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            total += matrix[lst[i]][lst[j]] + matrix[lst[j]][lst[i]]
    return total

def dfs(n, k):
    global ans
    if n == N//2:
        A = []
        B = []
        for i in range(N):
            if visited[i]:
                A.append(i)
            else:
                B.append(i)
        total_A = synergy(A)
        total_B = synergy(B)
        ans = min(ans, abs(total_A - total_B))
        return

    for i in range(k, N):
        if not visited[i]:
            visited[i] = 1
            dfs(n+1, i+1)
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    ans = 999999
    dfs(0, 0)
    print('#{} {}'.format(tc, ans))