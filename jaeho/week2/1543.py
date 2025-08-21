"""
세준이는 영어로만 이루어진 어떤 문서를 검색하는 함수를 만들려고 한다.
이 함수는 어떤 단어가 총 몇 번 등장하는지 세려고 한다. 
그러나, 세준이의 함수는 중복되어 세는 것은 빼고 세야 한다.
예를 들어, 문서가 abababa이고, 그리고 찾으려는 단어가 ababa라면, 세준이의 이 함수는 이 단어를 0번부터 찾을 수 있고,
2번부터도 찾을 수 있다. 그러나 동시에 셀 수는 없다.

세준이는 문서와 검색하려는 단어가 주어졌을 때, 
그 단어가 최대 몇 번 중복되지 않게 등장하는지 구하는 프로그램을 작성하시오.
"""

string = input()
search_str = input()

# 전체 문장에서 필요한 단어만 골라서 검색, 중복을 피하려면 어떻게?
# 한글자씩 넣을 빈 리스트를 설정하고 넣다가 널다가 찾으려는 단어 있으면 카운트 1개, 그리고 리스트 초기화 
lst = []
count = 0
search_str_len = len(search_str)

for i in string:
    lst.append(i)
    # 하나씩 리스트에 넣고
    if len(lst) >= search_str_len:
        # 리스트의 길이가 찾고자하는 단어의 길이와 같거나 더 클때
        last_part_list = lst[-search_str_len:]
        # 뒤에서 그 만큼 슬라이싱
        if "".join(last_part_list) == search_str:
            # 그리고 붙여서 검색하고자 하는 단어 비교
            count += 1
            # 맞으면 카운트 +1
            lst = []
            # 리스트 초기화

print(count)


