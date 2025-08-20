# 소정이와 세정이는 15번 팔씨름을 하여 8번 이상 이기는 사람이 점심 값을 면제받기로 함.
# 둘은 지금까지 k번의 팔씨름 진행
# s[i]가 'o'면 소정이가 i번째 경기에서 승리했다는 것이고, 'x'면 패배했다는 것임.
# 소정이가 앞으로 팔씨름을 15번째 경기까지 진행했을 때 자신이 점심값을 면제받을 가능성이 있는지 알아내기
# 각 테스트 케이스마다, 소정이가 점심값을 면제받을 가능성이 있다면 'YES', 없다면 'NO' 출력

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    result = input()

    x_cnt = 0 # x의 개수 세기

    for r in result:
        if r == 'x':
            x_cnt += 1

    if x_cnt <= 7:
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')
