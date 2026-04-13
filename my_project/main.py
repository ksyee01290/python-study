import calculator
import utils

while True:
    utils.manu()
    name = int(input("메뉴를 골라라"))
    if name == 1:
        num = utils.inputs()
        print(calculator.add(num))
    
    elif name == 2:
        num = utils.inputs()
        print(calculator.sub(num))

    elif name == 3:
        num = utils.inputs()
        print(calculator.div(num))

    elif name == 4:
        num = utils.inputs()
        print(calculator.mul(num))
    else:
        break