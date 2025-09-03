T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    
    # 틀린 문제 수
    false_problem = N - M

    # 틀린 문제를 K의 배수 위치에서 뒤쪽부터 채움
    false_number = []
    for i in range(N//K, 0, -1):
        if len(false_number) < false_problem:
            false_number.append(i*K)
        else:
            break

    true_cnt = 0  # 맞춘 문제 수
    i = 1         # 문제 번호
    score = [0] * (N+1)  # 점수 배열

    while i <= N:
        if true_cnt == M:  # 이미 M개 맞췄으면 나머지는 점수 그대로
            score[i] = score[i-1]
            i += 1
            continue

        if i % K != 0:  # K의 배수가 아니면 그냥 맞춘 문제
            score[i] = score[i-1] + 1
            true_cnt += 1
            i += 1
        else:  # K의 배수인 경우
            if false_number and i == false_number[-1]:  # 틀린 문제라면
                score[i] = score[i-1]
                false_number.pop()
                i += 1
            else:  # 맞춘 문제라면 점수가 2배
                score[i] = (score[i-1] + 1) * 2
                true_cnt += 1
                i += 1

    print(f'#{test_case} {score[N]}')
