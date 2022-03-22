import calculator

print('Welcome to ConvertALL')
print('Please select from the following:')
print(
    '''
1. Calculator
2. Measurement Converter
3. Currency Converter
4. Medical Converter
''')
print('Input your selection here:')

mainSelection = str(input())

if mainSelection == '1' or mainSelection == 'one':
    calculator.debug()
else:
    print('Under development')
