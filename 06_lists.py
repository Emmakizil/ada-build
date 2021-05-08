#empty list in two methods
my_list1 = [] #or
my_list2 = list()

numbers = [1, 2, 3, 4]
print(numbers)

nums = list(range(1,6))
print(nums)

my_list = list("banana")
print(my_list)

my_list[-1] = "apple"
print(my_list)

list1 = [5, 6, 7, 8, 9, 10]
list2 = list([5, 6, 7, 8, 9, 10])
print(list2)

# exercise 2
numbers = [10, 20, 30, 40]
print(numbers[2])
print(numbers[1:3])
print(numbers[-1])
print(numbers[0:3:2])

# exercise 4
zeros = [100] * 5
print(zeros)