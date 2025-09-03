# N개의 수로 이루어진 수열 A1, A2, ..., An이 주어짐.
# 수와 수 사이에 끼워넣을 수 있는 연산자(+, -, *, /)가 주어짐.
# 연산자의 개수는 N-1보다 많을 수도 있음.
# 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있음. 주어진 수의 순서를 바꾸면 안 됨.
# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행
# 나눗셈은 정수 나눗셈으로 몫만 취함.
# 음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같음.
# N개의 수와 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것 구하기

N = int(input()) # 수의 개수
arr = list(map(int, input().split())) # A1, A2, ..., An
plus, minus, mul, div = map(int, input().split()) # 덧셈, 뺄셈, 곱셈, 나눗셈의 개수

max_v = -1e9 # 만들 수 있는 식의 결과의 최댓값
min_v = 1e9 # 만들 수 있는 식의 결과의 최솟값

# idx : 현재 수열에서 사용할 숫자의 인덱스
# val : 지금까지 계산된 값
# plus, minus, mul, div : 남은 연산자 개수
def backtrack(idx, val, plus, minus, mul, div):
    global max_v, min_v

    # 모든 수를 다 사용했으면 결과 갱신 후 종료
    if idx == N:
        max_v = max(max_v, val)
        min_v = min(min_v, val)
        return

    # 덧셈 연산자 사용 가능하면
    if plus > 0:
        # 다음 숫자 idx를 더하고, 남은 + 연산자 1 감소
        backtrack(idx+1, val+arr[idx], plus-1, minus, mul, div)
    
    # 뺄셈 연산자 사용 가능하면
    if minus > 0:
        # 다음 숫자 idx를 빼고, 남은 - 연산자 1 감소
        backtrack(idx+1, val-arr[idx], plus, minus-1, mul, div)

    # 곱셈 연산자 사용 가능하면
    if mul > 0:
        # 다음 숫자 idx를 곱하고, 남은 * 연산자 1 감소
        backtrack(idx+1, val*arr[idx], plus, minus, mul-1, div)

    # 나눗셈 연산자 사용 가능하면
    if div > 0:
        # 문제 조건 : 음수를 양수로 나눌 때 처리
        if val < 0:
            backtrack(idx+1, -(-val//arr[idx]), plus, minus, mul, div-1)
        else:
            backtrack(idx+1, val//arr[idx], plus, minus, mul, div-1)

# 첫 번째 수는 그냥 val로 사용하고, idx = 1부터 시작
backtrack(1, arr[0], plus, minus, mul, div)

# 최댓값 출력
print(max_v)

# 최솟값 출력
print(min_v)
 