# 길이가 N인 수식
# 수식은 0보다 크거나 같고, 9보다 작거나 같은 정수와 연산자(+, -, x)로 이루어져 있음.
# 연산자 우선순위는 모두 동일
# 왼쪽에서부터 계산
# 괄호 안에 들어있는 식 먼저 계산
# 수식이 주어졌을 때, 괄호를 적절히 추가해 만들 수 있는 식의 결과의 최댓값 구하기
# 추가하는 괄호 개수의 제한은 없고, 추가하지 않아도 됨.
# 수식의 길이 1 <= N <= 19
# -2^31 < 정답 < 2^31

# 백트래킹
# 각 연산자마다 괄호를 칠지 말지 결정하면서 진행
# 직전에 괄호를 쳤으면 다음 연산자에는 괄호를 못 치도록 제약을 둠.
# 괄호를 안 치고 그냥 계산하거나, 괄호를 쳐서 먼저 계산한 값을 반영하거나 두 가지를 모두 재귀적으로 탐색

def calc(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

# idx : 현재 처리할 숫자의 인덱스
# value : 지금까지 계산된 누적값
def dfs(idx, value):
    global answer

    # 수식을 다 봤으면 결과 갱신
    if idx >= N:
        answer = max(answer, value)
        return

    # 1. 괄호 없이 현재 숫자와 누적값을 바로 계산하는 경우
    # 현재 숫자 앞에 있는 연산자는 expr[idx-1]에 위치
    if idx > 0:
        op = expression[idx - 1]
    else: # idx == 0 이면 연산자가 없이 때문에 '+'
        op = '+'

    # 현재 숫자를 바로 계산하고 다음 숫자로 이동
    dfs(idx + 2, calc(value, op, int(expression[idx])))

    # 2. 다음 연산자와 다음 숫자를 괄호로 묶어서 먼저 계산한 뒤 적용
    # 괄호를 만들려면 현재 숫자 뒤에 연산자와 숫자가 더 있어야 함
    if idx + 2 < N:
        # 괄호 안에서 먼저 계산될 값 : (현재 숫자 op 다음 숫자)
        temp = calc(int(expression[idx]), expression[idx + 1], int(expression[idx + 2]))
        # 괄호 결과를 지금가지의 누적값에 현재 위치의 앞 연산자로 적용
        if idx > 0:
            op = expression[idx - 1]
        else:
            op = '+'
        
        dfs(idx + 4, calc(value, op, temp))

N = int(input()) # 수식의 길이
expression = list(input()) # 길이가 N인 수식

answer = -2 ** 31 # 최댓값의 초기값을 가장 작은 값으로 설정

dfs(0, 0)
print(answer)
