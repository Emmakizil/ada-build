#Loops are programming constructs that help us repeat a code action a certain number of times based on algorithmic logic, without needing to copy and paste the code.
for i in range(3):
    print('hi')

i = 0
while i < 5:
    print('hello!')
    i += 1

word = "apple"
for letter in word:
    print(letter)


import random
def play_again():
    r = random.randit(0, 1)
    return r == 0

again = False
while again:
    print("Let's play a game!")
    print("...")
    again = play_again()

print("Game Over!")   

#blocks - a block is a section of code which is grouped together and intended to be executed if a certain condition is satisfied.

i = 0
while i < 5:
    multiple = i * 10
    print(f"{i} times 10 is {multiple}")
    i += 1

#infinit loop - runs forever
num = 0
while num <= 10:
    print(num)
    num += 2

#debugging loops - The following loop is intended to sum up all the numbers from 1 to 5
sum = 0
i = 1

while i <= 5: 
    sum = sum + i
    i = i + 1 
print(f"The Sum is {sum}") 

# write a function to take a string as a parameter and return the reverse of the string.
def reverse_string(input_str):
    answer = ""
    for i in input_str:
        answer = f"{i}{answer}"
    return answer

assert reverse_string("hello") == "olleh", "Cannot reverse 'hello'"
assert reverse_string("") == "", "When given an empty string it returns an empty string, but doesn't"
assert reverse_string("racecar") == "racecar", "Cannot reverse 'racecar'"
assert reverse_string("12345") == "54321", "Cannot reverse 12345"

#write a function, which takes an argument num and returns the sum of all the even numbers from 0 to num, inclusive
def total_even_numbers(number):
    sum = 0
    for num in range(number + 1):
        if num % 2 == 0:
            sum = sum + num
    return sum

test = total_even_numbers
print(test(10))