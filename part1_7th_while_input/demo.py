# input
message = input('Please input your information:')
print(message)
prompt = 'Please input your name:'
name = input(prompt)
print(name)

number = input('Enter a number,this code will tell you if it\'s even or odd:')
number = int(number)
if number%2 == 0:
    print('It\'s even')
else:
    print('It\'s odd')

# while
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = '\nTell me something,and I will repeat it back to you'
prompt += '\nInput \'quit\' to quit this program'
message = ''
while message != 'quit':
    message = input(prompt)
    print(message)
# usr target
# active = True
# while active :
    # if input() == 'quit'
    # active = False
# usr break
# While True:
    # if input() == 'quit'
    # break
# continue


