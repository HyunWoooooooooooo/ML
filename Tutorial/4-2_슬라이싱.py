jumin = "010721-1234567" #필요한 정보만을 잘라서 갖어오는것

print("성별:" + jumin[7]) #인덱스 count시 0부터 시작,-도 count함 
print("연:" +jumin[0: 2]) #내가 자르고 싶은 정보끝에서  +1 해야함
print("월:" + jumin[2: 4])#2자리 부터 3번째 까지
print("일:" + jumin[4: 6])
print("생년월일:" + jumin[0: 6] )
print("생년월일:" + jumin[:6]) #7번과 같은 의미임
print("뒤 7자리:" +jumin[7:]) #or jumpin[7: 14]
print("뒤 7자리(뒤에서부터): "+jumin[-7:]) 