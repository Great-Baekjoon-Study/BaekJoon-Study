N, S= map(int,input().split())
lst = list(map(int,input().split()))

cnt = 0  # 개수 세는 변수

def make_set(idx, selected, s):
    global cnt

    # if s > S:
    #     return -> 음수 때문에 가지치기 하면 오답됨

    # 1. 종료 조건
    if idx == N:
        if s == S:   # 합이 S인 경우만
            subset = []
            for i in range(N):
                if selected[i]:
                    subset.append(lst[i])
            if subset:   # 공집합이 아닐 때만
                cnt += 1
        return

    selected[idx] = 1
    make_set(idx + 1, selected, s + lst[idx])

    selected[idx] = 0
    make_set(idx + 1, selected, s)

make_set(0, [0] * N, 0)
print(cnt)
