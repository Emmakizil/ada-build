#  Conditionals Syntax
temp = 60

if temp == 0:
    print("It's ZERO DEGREES outstide!")
elif temp == 100:
    print("It's ONE HUNDRED DEGREES outstide!")
elif temp < 50:
    print("It's a bit chilly outside!")
elif temp < 100:
    print("It's warm outside.")

''' Exercise
In black jack, you "bust" if your cards total over 21. Print 
* `Bust!` if `score` is greater than 21.
* `Black Jack!` if `score` equals 21.
* `Great Hand!` if `score` is greater than or equal to 17, but less than 21.
* `Hit Me!` if `score` is less than 17
(_`Hit Me!` means give me another card_)
Currently, our `score` is `21` but the code block mistakenly outputs `Bust!`. Find and fix the error and then review the solution code below.
'''

score = 21
if score < 17:
    print("Hit Me!")
elif score < 21:
    print("Great Hand!")
elif score == 21:
    print("Black Jack!")
else:
    print("Bust!")

#Truthy or Falsy excercise

#x = "hi"
x = 0

if x:
    print(f'x = {x}, and therefore it\'s truthy.')
else:
    print(f'x = {x}, and therefore it\'s falsey.')

#boolean expressions excercise #2

coffee = True
good_sleep = True

#coffee = False
#good_sleep = True

if coffee and good_sleep:
    print("It's going to be a great day!")
else:
    print("Eh. Today's going to be a wash.")