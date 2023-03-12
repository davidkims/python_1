# 문제와 정답을 딕셔너리로 정의
question = {
    "범죄가 일어난 방은 어디일까요?": "침실",
    "범인은 누구일까요?": "A씨",
    "범인이 범죄를 저지른 시간은 언제일까요?": "오후 3시"
}

# 문제 출제 및 답 입력 받기
for q, a in question.items():
    print(q)
    answer = input("Answer: ")

    # 입력받은 답과 정답 비교 후 결과 출력
    if answer == a:
        print("정답입니다!")
    else:
        print("오답입니다!")
