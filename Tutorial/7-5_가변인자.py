def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {}|t 나이: {} |t".format(name,age),end=" ")
    print(lang1, lang2, lang3, lang4, lang5)
    #end=" "를 쓰게 되면 print문이 띄어쓰기로 끝나게 된다. 줄 바꿈이 아니라 
    # 따라서 다음 코드가 한칸 띄고 실행되게 된다

profile("유재석", 20, "python", "java", "C", "C++", "C# ")
profile("김태호", 25, "Kotilin", "swift", "","","" )
#언어를 두개 가능, 원하는대로 출력은 가능, 그러나 매번 빈값 넣어야 하는 불편함
#추가적으로 유재석이 공부해서 아는 언어가 하나 늘어나면 함수 자체를 재정의 해야하는 불편함 발생


def profile(name, age, *language):
    print("이름: {}\t 나이: {}\t".format(name,age),end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "python", "java", "C", "C++", "C#", "javaScript")
profile("김태호", 25, "Kotilin", "swift")