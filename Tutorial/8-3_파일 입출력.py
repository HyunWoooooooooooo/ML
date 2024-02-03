score_file = open("score.txt","w",encoding = "utf8")
#score_file이라는 변수 생성하고 score.txt를 열고 write하는 파일이다.

print("수학: 0", file = score_file)
print("영어: 0", file = score_file)
score_file.close()
#file은 열었으면 꼭 닫아줘야 한다,print는 자동으로 줄바꿈 해준다. 


score_file = open("score.txt", "a", encoding = "utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
#하지만 .write는 자동으로 줄바꿈을 하지 않는다.
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.read())
score_file.close()


score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.readline(), end = "") #줄 별로 읽기 + 커서 다음줄로 이동
print(score_file.readline(), end = "") #줄 별로 읽기 + 커서 다음줄로 이동
print(score_file.readline(), end = "") #줄 별로 읽기 + 커서 다음줄로 이동
print(score_file.readline(), end = "") #줄 별로 읽기 + 커서 다음줄로 이동
score_file.close()

score_file = open("score.txt","r", encoding = "utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end = "")
score_file.close()

score_file = open("score.txt","r", encoding = "utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end = "")
score_file.close()
