doc = input()
find = input()

a = len(doc)
b = len(find)

i = 0
cnt = 0

while i <= a - b:
    # i에서 시작하는 b글자가 find와 같다면
    if doc[i:i+b] == find:
        # 개수 +1
        cnt += 1
        # 단어 길이만큼 점프
        i += b
    # 아니면 한 글자 이동
    else:
        i += 1
