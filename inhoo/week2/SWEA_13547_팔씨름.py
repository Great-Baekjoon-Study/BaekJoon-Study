#15번 팔씨름, 8번이상 이기는 사람
#지금가지 k번의 팔씨름 진행함.
#길이가 k인 'o' 또는 'x'로 구성된 문자열 S[1...k]
#S[i] 가 'o'면 A가 i번째 경기에서 승리했다는 것
#A는 15번까지 진행했을 때 내가 승리할 수 있을까?

T = int(input())
for tc in range(1, T+1):
    S = list(input()) #길이가 1~15

    #A가 8번 이상 이겼다 = B가 8번이상 졌다.
    #S를 보고 YES or NO가 바로 판단가능하게 테스트케이스를 주지 않음.
    # A의 승리가 불가능한 것이 아니라면 YES 출력
    # A가 질 조건 => B가 8번 이상 이길 것. => x가 8번이상 출력
    cnt_lose = 0
    for i in S:
        if i == 'x':
            cnt_lose +=1
    if cnt_lose >= 8:
        print(f'#{tc} NO')
    else:
        print(f'#{tc} YES')

