'''
N개의 서로 다른 무게를 가진 무게 추와 양팔 저울

N!가지

2^N N!가지


right <= left


N: 1~9


1. 부분집합을 만들고

2. 거기에서 포함: left, 포함 아닌 거는 right에.

4. 더하다가, left < right인 경우가 생기면 바로 리턴(가지치기)

5. left >= right인 거 찾기

'''
#오른쪽 저울 위에 올라가있는 무게의 총합<= 왼쪽에 올라가 있는 무게의 총합
# result = solve(0, 0, 0, arr, [False] * N)
def solve(idx, left_sum, right_sum, weights, selected):
    # 
    #idx: 현재 추의 순서
    #left_sum: 현재 왼쪽 저울의 무게 합
    #weights: 주어진 추의 무게 리스트
    # selected: 추의 사용 여부 추적(o: True)


    global N, total_sum, count
    
    # 가지치기: 오른쪽 무게>  왼쪽 무게보다 커지면 더 이상 진행할 필요x
    if left_sum < right_sum:
        return 0
    
    # 1. 가지치기 2 (Pruning): 남은 추를 모두 오른쪽에 올려도
    # 이미 왼쪽 무게가 오른쪽 무게보다 크거나 같은 경우
    remaining_sum = total_sum - (left_sum + right_sum)
    if left_sum >= right_sum + remaining_sum:
        # 남은 추들은 어떤 순서로든 왼쪽에 올리든 오른쪽에 올리든
        # 항상 left_sum >= right_sum을 만족
        # [100,1,2,3,4,5,6,7,8,9]
        # N개의 추 중 이미 idx개의 추를 이미 사용함
        # 따라서 남은 (N - idx)개의 추를 배치하는 경우의 수만 계산하면 됩니다.
        
        
        #모든 무게 추를 양팔저울의 왼,오에 올릴 경우의 수 : (2^N)*N!
        # 1-1. 남은 추의 순열 수 (N-idx)!
        permutations_of_remaining = 1
        for i in range(N - idx, 0, -1):
            permutations_of_remaining *= i
        
        # 1.2 각 추를 왼쪽/오른쪽에 놓는 경우의 수: 2^(N - idx)
        power_of_two = 2 ** (N - idx)
        
        return permutations_of_remaining * power_of_two





    # 2. 종료 조건 : 모든 추를 사용한 경우
    if idx == N: # 현재 결정할 추의 순서
        # 이 시점에서 left_sum >= right_sum임
        return 1

    count = 0
    # 3. 재귀 호출: N개의 추 중 하나를 선택하여 저울에 올립니다.
    for i in range(N):
        if not selected[i]:  # 아직 사용되지 않은 추라면
            selected[i] = True
            
            # 1: weights[i]를 왼쪽에
            count += solve(idx + 1, left_sum + weights[i], right_sum, weights, selected)
            
            # weights[i]를 오른쪽에
            if left_sum >= right_sum + weights[i]:#가지치기
                count += solve(idx + 1, left_sum, right_sum + weights[i], weights, selected)
            
            #재귀호출이 끝났을 때, 사용하지 않은 상태로
            selected[i] = False
            
    return count



T = int(input())

for tc in range(1, T + 1):
    N = int(input()) # 추의 개수
    arr = list(map(int, input().split()))
    
    # 남은 추의 무게 합을 계산하기 위해 전체 합을 미리 구해둡니다.
    total_sum = sum(arr)
    
    # solve 함수를 호출하여 유효한 경우의 수를 계산합니다.
    result = solve(0, 0, 0, arr, [False] * N)
    
    print(f"#{tc} {result}")