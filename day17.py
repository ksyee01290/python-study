try:
    num1 = int(input("첫번쨰:"))
    num2 = int(input("두번째:"))

    print(num1/num2)

# except ValueError:
#     print("숫자만 입력해주시죠")

# except ZeroDivisionError:
#     print("0으로 나눌수 없음")

except Exception as e:
    print("에러발생:", e)
    

finally:
    print("프로그램 종료")
    
