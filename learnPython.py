favorite_phrase = 'i like cheese'

#loops.....................
for letter in favorite_phrase:
    print(letter)

index = 0
while index < len(favorite_phrase):
    letter = favorite_phrase[index]
    print(letter)
    index = index + 1

running =  True
while running:
    favorite_number = 7
    guess = int(input("what is vana's favorite number?"))
    if favorite_number == guess:
        print('yayyyyy! You won')
        running = False
    else:
        print('try again !!')  


number  = [1,2,3,4]
letter = 'abcd'

for number,letter in zip(number , letter):
    print(number , ':' , letter)

for num in number:
    for lett in letter:
        print(num , lett)

sale  = [
    list(range(2)),
    list(range(3)),
    list(range(4))
]

print(sale)

total =0
for sal in sale:
    for day in sal:
        total += day
print(total)

numbers = range(1,21)

sum = 0
for number in numbers:
    sum = sum + number;

print(sum)




#Reading and writing and copying file......................
with open('/home/user/Desktop/python/data.txt','r') as file:
    for line in file:
        print(line)

    file.seek(0)
    for line in file:
        print(line)    




output_file = '/home/user/Desktop/python/copyData.txt'

with open('/home/user/Desktop/python/data.txt' , 'r') as input_file , open(output_file ,'w') as file:
    for line in input_file:
        if line != "\n":
            file.write(line)



with open('/home/user/Desktop/python/winner.txt', 'r') as winner_list , open('/home/user/Desktop/python/message.txt' , 'r') as message_list:
    message = message_list.read()
    winners = winner_list.readlines()
    for winner in winners:
        file_name = winner.strip('\n') + '.txt'
        with open(file_name ,'w') as f:
            print('Dear ' + winner.strip('\n') + ',\n')
            print(message)









#Reading console input and formating outputs....................................

food_prompt = """
Which food are you purchasing ? (choose in letter)
A) Banana
B)Apple
C)Cheese
D)Pickles
Q)To Quit
"""

while True:
    print(food_prompt)
    food = input('enter a food to purchase ')
    if food == 'Q':
        print('Goodbye! Come again')
        break

    qunt_food = int(input('How many food do you want '))


    if food not in ['A' , 'B' , 'C' ,'D']:
        print('oppps!!! invalid option . Try again')
    else:
        if food == 'A':
            cost = 0.99 
            food_label = 'Banana'
        elif food == 'B':
            cost = 2.99
            food_label ='Apple'
        elif food == 'c':
            cost = 3.99
            food_label = 'Cheese'
        else:
            cost = 2.67
            food_label ='pickles'

        total = qunt_food * cost
        result = "You are buying {} {} for ${}".format(qunt_food , food_label , total)
        print(result)       







#defining funciton ....................

def eat(food):
    print('You jus had eat {}'.format(food))

def main():
    eat('apple')
    eat('graps')
    eat('milk')

main()



def eat(food , happy=False):
    if happy:
        print('nam nam!!!')
    
    print('i have some {}'.format(food))


eat('apple', True)


def game(*, starting_point = 15.0 , player_name = 'player 1'):
    print('game point is:' , starting_point)
    print('player name is:' , player_name)


game()


def example(*agrs , **kwargs):
    print(agrs)
    print(kwargs)

example(fName = 'Harbans' , lName = 'lal' , age='25')
example(lName = 'ram' , fName = 'Jai' , age='25')


def address(first_name = 'justin' , last_name = 'Doe' , age = 25):
    print(first_name , last_name ,age)

address()
address(last_name='world' , first_name='hello', age='28')




#infinite adding number calculator...

def add(*args):   
    numbers = list(args)
    total = 0
    for number in numbers:
        total = total + number

    print(total)

add(25,25,50,500)   


#excepiton handling ....................
tol = 4
num = 0
try:
    average  = tol / num
    print('average is :', average)

except Exception as e:
    print('you cannnot divide by zero' , e)

finally:
    print('savig progtresss.............')    


#math and random module........................
import math
import random
result  = math.fsum([4.3,2,6,8.2])
colors = ['red','blue','purple']
random_color = random.choice(colors)
secret_number  = random.randint(1,100)
sec_num  = random.randrange(0,102,2)
print(sec_num)


#os module............................
import os

current_directory = os.getcwd()
current_files = os.listdir()
file_path = os.path.join(current_directory , 'learnPython.py')
learn_python = os.stat(file_path)
print(learn_python)



#datetime and timedelta module....................
from datetime import datetime , timedelta

today = datetime.now()
first_of_day = datetime(2023,1,1)
total_days = today - first_of_day
tommorow = timedelta(days=1)
print(today + tommorow)