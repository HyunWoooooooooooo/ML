# import pickle
# profile_file = open("profile.pickle","wb")
# profile = { "이름":"박명수", "나이": 30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)
# #profile에 있는 정보를 file에 저장함
# profile_file.close()
#파일을 저장하는 에제

#파일을 불러오는 예제
import pickle
profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file) 
#profile_file에 있는 데이터를 profile이라는 변수에 불러오기
print(profile)
#잘 불려왔는지 확인해보기
profile_file.close()