T = int(input())
group_word_count = 0

for _ in range(T):
    word = input()
    is_group_word = True
    visited = set()  # 이전에 등장한 문자를 기록하기 위한 집합 visted를 초기화

    for i in range(len(word)):
        if i > 0 and word[i] == word[i-1]:
            continue  # 이전 문자와 동일하면 다음 반복으로 넘어간다.
        if word[i] in visited: #방금 입력받은 문자가 visted에 있는 문자라면
            is_group_word = False  
            break
        visited.add(word[i])  # 문자 방문 기록
        # 0번째 i는 두가지 조건에 모두 거짓이니까 visted에 추가된다.
        # 그 다음으로 들어온 애들은 i=1, a라면 같으니까 continue만나서 다음 반복으
        # 로 넘어가고 b라면 다르니까 또다시 두가지 조건에 위배
        # visted를 만난다

    if is_group_word:
        group_word_count += 1  # 그룹 단어 카운트 증가

print(group_word_count)
