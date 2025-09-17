"""
두 명의 손님에게 음식을 제공하려고 한다.
두 명의 손님은 식성이 비슷하기 때문에, 최대한 비슷한 맛의 음식을 만들어 내야 한다.

N개의 식재료가 있다.
식재료들을 각각 N / 2개씩 나누어 두 개의 요리를 하려고 한다. (N은 짝수이다.)

이때, 각각의 음식을 A음식, B음식이라고 하자.
비슷한 맛의 음식을 만들기 위해서는 A음식과 B음식의 맛의 차이가 최소가 되도록 재료를 배분해야 한다.

음식의 맛은 음식을 구성하는 식재료들의 조합에 따라 다르게 된다.

식재료 i는 식재료 j와 같이 요리하게 되면 궁합이 잘 맞아 시너지 Sij가 발생한다. 
(1 ≤ i ≤ N, 1 ≤ j ≤ N, i ≠ j)

각 음식의 맛은 음식을 구성하는 식재료들로부터 발생하는 시너지 Sij들의 합이다.
"""
# 식재료 i를 식재료 j와 같이 요리하게 되면 발생하는 시너지 Sij의 정보가 주어지고, 
# 가지고 있는 식재료를 이용해 A음식과 B음식을 만들 때, 
# 두 음식 간의 맛의 차이가 최소가 되는 경우를 찾고 그 최솟값을 정답으로 출력하는 프로그램을 작성하라.

# N개 중에 N // 2개를 선택해서 조합을 계산하는 재귀함수를 짜고, 
# 다 고르고 리턴할때 나머지를 다 계산해서 최솟값을 찾자
# 그럼 가지는 어떻게 치나요?
# 전체 맛 - 고른 식재료들로 요리한 음식의 맛 = 남은 식재료로 요리한 음식의 맛
# 고른 식재료들로 요리한 음식의 맛 - 남은 식재료로 요리한 음식의 맛 > 최솟값보다 크면 가지치면 될거같다.
# 그렇다면 누적으로 맛의 합계를 받아와 줘야겠네
# selec = 고른 재료의 수
# taste = 누적 맛
# 그럼 배열에서는 어떻게 가져올거야
# 두개 가져온걸 
# 가져온 식재료를 냄비에 넣고
# 조리를 하자
def cooking(start, select, idx, pot):
    if idx == 2:
        return arr[select[0]][select[1]] + arr[select[1]][select[0]]
    
    for i in range(start, len(pot)):
        select.append(pot[i])
        taste += cooking(start+1, select, idx +1, pot)
        select.pop()

def cooking_ready(selec, pot, start):
    global min_diff
    if selec == N//2:
        # 3개 다 고르면
        A_taste = 0
        A_taste += cooking(0,[],0,pot)
        B_taste = total_sum - A_taste 
        diff = A_taste - B_taste
        if diff < 0:
            diff *= -1

        if diff < min_diff:
            min_diff = diff
        return
    
    for i in range(start, N):
        # 0부터 n-1번까지의 식재료
        pot.append(i)
        cooking_ready(selec+1, pot, start+1)
        pot.pop()
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    min_diff = 99999999999
    arr = [list(map(int, input().split())) for _ in range(N)]
    total_sum = 0
    for i in range(N):
        for j in range(N):
            total_sum += arr[i][j]

    cooking_ready(0, [], 0)
    print(f'#{tc} {min_diff}')


# ------------------------------------------------------------------------

def calculate_taste(team):
    taste = 0
    # 팀에 속한 멤버가 2명 이상일 때만 시너지 계산
    if len(team) > 1:
        # 모든 멤버 쌍(i, j)에 대해 시너지를 더함
        for i in range(len(team)):
            for j in range(i + 1, len(team)):
                member1 = team[i]
                member2 = team[j]
                taste += arr[member1][member2] + arr[member2][member1]
    return taste

# N/2명의 팀원을 뽑아 맛의 차이를 계산하는 재귀 함수
def find_diff(member_count, start_index, team_A):
    global min_diff

    # 기저 조건: A팀 구성이 완료되었을 때
    if member_count == N // 2:
        # B팀 구성하기 (전체 재료에서 A팀 재료를 제외)
        team_B = []
        for i in range(N):
            if i not in team_A:
                team_B.append(i)
        
        # 각 팀의 맛 계산
        taste_A = calculate_taste(team_A)
        taste_B = calculate_taste(team_B)
        
        # 맛의 차이를 구하고 최솟값 갱신
        diff = abs(taste_A - taste_B)
        min_diff = min(min_diff, diff)
        return

    # 재귀 호출: 조합 생성
    for i in range(start_index, N):
        team_A.append(i)
        find_diff(member_count + 1, i + 1, team_A)
        team_A.pop() # 백트래킹: 다음 조합을 위해 마지막에 추가한 멤버 제외


# --- 메인 실행 부분 ---
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    min_diff = float('inf') # 최솟값을 매우 큰 수로 초기화

    find_diff(0, 0, [])
    
    print(f'#{tc} {min_diff}')

    