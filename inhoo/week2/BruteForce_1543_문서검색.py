#영어 문서 검색
#단어가 총 몇 번 등장하는지
#중복되어 세는 것은 빼고 세야한다. 동시에 셀 수 없음
#그 단어가 최대 몇 번 중복되지 않게 등장하는지 구하기
#처음부터 찾다가, 찾은 후, 글자 수 만큼 점프해서 다시 찾기

#카운팅 3개하는 걸 어떻게 함?

arr = list(input())
search_word = list(input())


def brute_force(t,p): #t: 본문 문자열, p: 찾을 패턴
    i = 0
    j = 0
    cnt_word = 0
    while i < len(t) and j < len(p):
        if t[i] != p[j]: #글자가 다르다면
            i = i-j #i에서 시작해서 j번만큼 비교했는데 그만큼 빼기
            i+=1
            j=0

        else:   #같다면
            i+=1
            j+=1

        if j == len(p): #이미 j+1 했으므로 그냥 j = len(p)
            cnt_word +=1
            j=0


    return cnt_word

print(brute_force(arr,search_word))






