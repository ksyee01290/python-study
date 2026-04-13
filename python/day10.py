students = {}

while True:
    print("-"*30)
    print("1. 학생 추가")
    print("2. 성적 입력")
    print("3. 평균 계산")
    print("4. 검색")
    print("5. 전체 조회")
    print("6. 종료")
    num = int(input("메뉴를 고르시오:"))
    print("-"*30)
    
    if num == 1:
        name = input("이름 입력(key입력) :")
        sid = int(input("학번 입력:"))
        students[name] = {'성적':0,'학번':sid}

    if num == 2:
        target_name = input("성적을 입력할 학생 이름:")
        if target_name in students:
            score = int(input(f"{target_name}성적 입력:"))
            students[target_name]['성적'] = score
            print(f"{target_name} 학생의 성적 업데이트")
        else:
            print("학생을 찾을수 없습니다.")
        
    if num == 3:
        total_score = 0

        for info in students.values():
            total_score += info['성적']
        val = total_score/len(info)
        print(val)

    if num == 4:
        print(students.keys())
        target_name = input("검색할 학생 이름:")

        print(students.get(target_name))
    if num == 5:
        for name, info in students.items():
            score = info['성적']
            sid = info['학번']

            print(f"이름: {name} | 학번: {sid} | 성적: {score}")
    if num == 6:
        break

    else:
        break
    