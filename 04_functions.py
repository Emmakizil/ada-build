# input is a example of built in functions. Note: use \n for seperating line
print ('What do you choose? A, B, C, or D\n')
#user_input = input()
#print(f'\nYou chose {user_input}. Great choice!')

#Modules or libraries
import math
square = math.sqrt(16)
print(square)

import random
random_num = random.randint(1, 10)
print(random_num)

rand_num = random.random() #returns a random floating point number in the range (0, 1)
print(rand_num)

#functions
def say_hello(name):
    print(f'welcome {name}! hello world!')
say_hello('fereshteh')


def add(num1, num2):
    return num1 + num2
    
the_sum = add(1, 2)
print(f'1 + 2 = {the_sum}')

#Practice Problems
#Write the function triple(x), which takes in a numeric input and outputs three times that input.
def triple(num):
    '''
    input: integer or float number
    output: three time the input
    '''
    return 3 * num
#assertion example   
assert triple(3) == 9, f"Reported {triple(3)} for triple(3) instead of 9"
assert triple(-3) == -9, f"Reported {triple(-3)} for triple(-3) instead of -9"
assert triple(1.5) == 4.5, f"Reported {triple(1.5)} for triple(1.5) instead of 4.5"

times_three = triple(4)
print(times_three)

# square
def square(n):
    """
    this is a docsctring:
    input: an integer or float value n
    output: the square of n (n*n)
    """
    
    return n * n

assert square(3) == 9, f"Reported {square(3)} for square(3) instead of 9"
assert square(-3) == 9, f"Reported {square(-3)} for square(-3) instead of 9"

square_num = square(3)
print(square_num)

#checkends
def checkends(s):
    if s[0] == s[-1]:
        return True
    else:
        return False

assert checkends('no match') == False, f"Reported {checkends('no match')} for checkends('no match') instead of False"
assert checkends('!ada!') == True, f"Reported {checkends('!ada!')} for checkends('!ada!') instead of True"
check_string = checkends("!ada!")
print(check_string)

#flipside
def flipside(s):
    '''
    input; string
    output: switch first and second half
    '''
    string_lenght = len(s)
    string_half = len(s) // 2
    new_string = s[string_half:string_lenght] + s[0:string_half]
    return new_string
assert flipside('carpets') == 'petscar', f"Reported {flipside('carpets')} for flipside('carpets') instead of petscar"
assert flipside('homework') == 'workhome', f"Reported {flipside('homework')} for flipside('homework') instead of workhome"
assert flipside('ada') == 'daa', f"Reported {flipside('daa')} for flipside('ada') instead of daa"

