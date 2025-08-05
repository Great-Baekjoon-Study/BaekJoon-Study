# K번째 교환되는 두 개의 수를 작은 수부터 한 줄에 출력
# 교환 횟수가 K보다 작으면 -1 출력

N, K = map(int, input().split()) # N : 배열 A의 크기, K : 교환 횟수
A = list(map(int, input().split())) # 배열 A

sort_cnt = 0 # 교환 횟수 초기 설정값
for i in range(N-1, 0, -1): # 버블 정렬 시작
    for j in range(i):
        if A[j] > A[j+1]: # j번째 원소가 (j+1)번째 원소보다 클 경우
            A[j], A[j+1] = A[j+1], A[j] # 두 원소 교환
            sort_cnt += 1 # 교환 횟수 1 증가
            if sort_cnt == K: # 교환 횟수가 K와 같으면
                # K번째 교환되는 두 개의 수 출력
                # 이미 위에서 교환을 했기 때문에 j번째 원소가 (j+1)번째 원소보다 무조건 작음.
                print(f'{A[j]} {A[j+1]}') 
                exit() # K번째 교환을 찾았기 때문에 바로 프로그램 종료

if sort_cnt < K: # 총 교환 횟수가 K보다 작으면
    print(-1) # -1 출력