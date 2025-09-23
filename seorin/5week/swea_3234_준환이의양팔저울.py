def recur(idx, left, right):
    global cnt

    if left < right : 
        return 
    
    # 모든 추를 다 돌았을 때 
    if idx == N : 
        cnt += 1
        return
    
    for i in range(N):
        if not used[i]:
            used[i] = True
            # 왼쪽에 넣었을 떄 
            recur(idx+1, left + arr[i], right)
            # 오른쪽에 넣었을 때 
            recur(idx+1, left, right + arr[i])
            used[i] = False

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    used = [False] * N
    # N개의 서로 다른 무게를 가진 무게 추와 양팔 저울을 갖고 있음
    # 오른쪽에 있는 합이 왼쪽에 올라가 있는 무게의 총합보다 커져서는 안됨
    # 올리는 순서도 봄 => 순열 

    recur(0, 0, 0)
    # 총 경우의 수 구하기 
    print(f"#{tc} {cnt}")