# 두 전구 X, Y
#0~100초 사이에 두 전구가 언제 켜지는지
#X는 A~B초까지에만 켜져 있었따.
#Y는 C~D초까지에만 켜저 있었따.
#100초 중 두 전구가 켜져있던 시간은 몇 초?

T = int(input())
for tc in range(1, T + 1):
    result = 0
    A, B, C, D = map(int, input().split())

    s = max(A, C)
    e = min(B, D)

    if s <= e:
        result = e - s  # 몇 초인지: 시간 *간격*을 구하는 것이므로 +1하지 않는다.

    print(f'#{tc} {result}')

