def main():
    print('Welcome to ConvertAll Calculator')
    print('Please select the operation to be used:')
    print(
        '''
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        ''')
    print('Input your selection here:')
    operationSelect = str(input())

    if operationSelect == '1' or operationSelect == 'one':
        addition()
    elif operationSelect == '2' or operationSelect == 'two':
        subtraction()
    elif operationSelect == '3' or operationSelect == 'three':
        multiplication()
    elif operationSelect == '4' or operationSelect == 'four':
        division()
    else:
        print('Under development')


def addition():
    print('Please Enter the 1st Number')
    firstNum = int(input())
    print('Please Enter the 2nd Number')
    secondNum = int(input())
    answer = firstNum + secondNum
    print('Solution')
    print(str(firstNum) + ' + ' + str(secondNum) +
          ' is equal to: ' + str(answer))


def subtraction():
    print('Please Enter the 1st Number')
    firstNum = int(input())
    print('Please Enter the 2nd Number')
    secondNum = int(input())
    answer = firstNum - secondNum
    print('Solution')
    print(str(firstNum) + ' - ' + str(secondNum) +
          ' is equal to: ' + str(answer))


def multiplication():
    print('Please Enter the 1st Number')
    firstNum = int(input())
    print('Please Enter the 2nd Number')
    secondNum = int(input())
    answer = firstNum * secondNum
    print('Solution')
    print(str(firstNum) + ' x ' + str(secondNum) +
          ' is equal to: ' + str(answer))


def division():
    print('Please Enter the 1st Number')
    firstNum = int(input())
    print('Please Enter the 2nd Number')
    secondNum = int(input())
    answer = firstNum / secondNum
    print('Solution')
    print(str(firstNum) + ' / ' + str(secondNum) +
          ' is equal to: ' + str(answer))
