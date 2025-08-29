#gpt 도움 받은 거
#나중에 다시 보기

N = int(input())
numbers = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_val = -1e9
min_val = 1e9

def dfs(idx, current, p, m, mu, d):
    global max_val, min_val
    if idx == N:  # 모든 숫자 사용 완료
        max_val = max(max_val, current)
        min_val = min(min_val, current)
        return
    
    num = numbers[idx]
    if plus > 0:
        dfs(idx+1, current + num, p-1, m, mu, d)
    if minus > 0:
        dfs(idx+1, current - num, p, m-1, mu, d)
    if mul > 0:
        dfs(idx+1, current * num, p, m, mu-1, d)
    if div > 0:
        if current < 0:
            dfs(idx+1, -(-current // num), p, m, mu, d-1)
        else:
            dfs(idx+1, current // num, p, m, mu, d-1)

dfs(1, numbers[0], plus, minus, mul, div)

print(max_val)
print(min_val)
