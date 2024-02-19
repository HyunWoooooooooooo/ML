

temp = input() #문자열 형태로 word로 입력 받고 다 소문자로 변환
word = temp.lower()
count_num = [0]*26
compare =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(len(word)):
    for j in range(len(compare)):
        if word[i] == compare[j]:
            count_num[j] = count_num[j] + 1
        

#최댓값 찾기
max_num = max(count_num)
#최댓값 등장 횟수
final_num = count_num.count(max_num)
#최종 출력할 알파벳




if final_num == 1:  #등장횟수가 1이면
    temp2 = count_num.index(max_num)
    print(compare[temp2].upper())
elif final_num > 1:
    print('?')






