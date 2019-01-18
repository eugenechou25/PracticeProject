from random import randint

alpha = 'abcdefghijklmnopqrstuvwxyz'
capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
total_list = []

for i in range(0, 200):
    activate_code = ''
    for j in range(10):
        rand_of_three = randint(0, 10000)
        if rand_of_three % 3 == 0:
            activate_code = activate_code+alpha[randint(0, 25)]
        elif rand_of_three % 3 == 1:
            activate_code = activate_code + capital[randint(0, 25)]
        else:
            activate_code = activate_code + number[randint(0, 9)]
    print(activate_code)
    total_list.append(activate_code)
    
with open('E:/Eics/atcode.txt', 'w') as f:
    for each in total_list:
        f.write(each)
        f.write('\n')
