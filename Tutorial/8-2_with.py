# import pickle

# with open("profile.pickle","rb") as profile_file:
#     #profile.pickle이라는 파일을 rb모드로 열고, profile_file이라는 변수에 할당한다.

#     print(pickle.load(profile_file))
#     #파일의 내용을 pickle.load로 불러와서 print를 했다.


# with open("study.txt","w", encoding = "utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt","r",encoding = "utf8") as study_file:
    print(study_file.read())


