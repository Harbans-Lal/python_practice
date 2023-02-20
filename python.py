#introduction to python programming...........
print('Hello world')

#Arithmetic operator............
x = 10
y = 13

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)

z  = (x+y)* 7
print(z)


#if ,elif and else............................
favorite_color =input('enter your favorite color')

if favorite_color == 'Blue':
    print('This is also sam color too')
elif favorite_color == 'red':
    print('tasty')
else:
    print('this is also good color') 


#funcion.................
def add(num , another_num):
    return num + another_num


def three_time(parm):
    print(parm)
    print(parm)
    print(parm)

def howMany(what , how_many):
    if type(what) == str and type(how_many)== int:
        print(what * how_many)  
    else:
        print('first argument should be string and other shoudl be integer')      

if __name__ == '__main__':

    howMany(1, 5)

      

#Loop........................

count = 1
while count < 100:
    print(count)
    count+=1

for count in range(1 , 100):
    print(count)


def while_loop(start , stop):
    sum = 0
    while start <= stop:
        sum += start
        start += 1
    print(sum)    

def for_loop(start, stop):
    sum  = 0
    for count in range(start,stop):
        sum+= count
    print(sum)


if __name__ == '__main__':
    for_loop(1,11)  



while True:
    user_input = input('enter your favourite fruit.  press q to Quit  ')
    
    if user_input == 'q':
        break
    else:
        print('That is good fruit')



#String..............
str1 = 'Functions are important programming concepts.'

def print_fn():
    str1 = 'Variable scope is an important concept.'
    print(str1)


my_str = 'akghfjhdjnfdsnfhdsjfjkldjl;fieisiyoutyrtjfmzxcbnvnzm,.nkdjsflhflakdhljhdfhdjhfuyruithjadsfhkjadshjkfhbvcjdkahfbvncmnzx,.vbcvznneuhfuw'
lookup_char = 'abcd'

for char in lookup_char:
    print(char)
    print(my_str.count(char))

for char in lookup_char:
    result = char+ ':' + str(my_str.count(char))
    print(result)


for char in lookup_char:
    result = 'char{} count{} '.format(char , my_str.count(char))
    print(result)


#List...................
favourite_food = ['pizza','apple' , 'banana']
my_fav = ['abc' ,'xyz' , 'pizza']

for food in my_fav:
    if food in favourite_food:
        print('it is also my favorite food')
    else:
        print('it is not') 



numbers = []
sum = 0
while True:
    user_input = input('enter the number to get sum or pres q to Quit. ')

    if user_input == 'q':
        break
    else:
        user_in = int(user_input)
        numbers.append(user_in)

for number in numbers:
    sum = sum + number 
      
print('Your total number of sum is ' , sum   )   


#Dictionary...................         
first_dic = {'one':1,'two':2,'three':3}

for key, value in first_dic.items():
    print('key is {} and value is{}'.format(key, value))


logs = 'kjdfkldjkfhadshflkdsa;ahdfjha;skhdjklfahfhfhk;lskdj;lkjlkdlfhadhieirtyrhvbz.,cnzbvz.czcjhads;fz.mcvznc,zdafjakjfkuiotgyurqrpieqpwurpqureityqoirudkJC:Lb,zvm'
logs_count = {}
alpha = 'abcdefghijklmnopqrstuvwxyz'
for letter in alpha:
    for char in logs:
        if char == letter:
            if char in logs_count:
                logs_count[char] += 1
            else:
                logs_count[char] = 1

for key, value in logs_count.items():
    print('{} : {}'.format(key , value))


#Tuple.........................
def divmod(a,b):
    if type(a)==int and type(b)==int :
        division = a // b
        remainder = a % b 
        return (division , remainder)
    else:
        return None


f_num = 9
s_num = 4

dev , rem = divmod(f_num , s_num) #unpack through tuple
print(dev)
print(rem)

def tuple_div_mod(pair_tuple):
    if type(pair_tuple) == tuple:
        a , b = pair_tuple
        div = a /b
        rem = a%b

        return div,rem
    else:
        return False    


pairs = (9,4)
div,rem = tuple_div_mod(pairs)
print(div)
print(rem)

#after returing a fuction it will stop executing further...


#File manipulation..........................
f = open('data.txt' ,'r')
text = f.read()
print(text)
f.close()

with open('data.txt' , 'r') as f:
    text = f.read()
    
with open('some_file.txt' , 'w') as fw:
    fw.write(text)

with open('data.txt' , 'r') as f , open('extra_file.txt' , 'w') as ex:
    text  = f.read()
    for char in text:
        ex.write(char)