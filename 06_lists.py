
#empty list in two methods
my_list1 = [] #or
my_list2 = list()

numbers = [1, 2, 3, 4]
#print(numbers)

nums = list(range(1,6))
#print(nums)

my_list = list("banana")
#print(my_list)

my_list[-1] = "apple"
#print(my_list)

list1 = [5, 6, 7, 8, 9, 10]
list2 = list([5, 6, 7, 8, 9, 10])
#print(list2)

# exercise 2
numbers = [10, 20, 30, 40]
#print(numbers[2])
#print(numbers[1:3])
#print(numbers[-1])
#print(numbers[0:3:2])

# exercise 4
zeros = [100] * 5
#print(zeros)

animals = ["bird", "horse", "cat", "monkey"]
animals[0] = "parrot"
animals.append('dog')
#print(animals)

#loop 
# veggies = ["carrot", "yam", "zucchini", "spinach"]
# veggies_count = len(veggies)

# for i in range(veggies_count):
#     print(f"Vegetable {i+1}: {veggies[i]}")

# names = ["Usagi", "Rei", "Ami", "Makoto", "Minako"]
# for i in range(len(names)):
#     print(f"Hello {names[i]}!")

veggies = ["carrot", "yam", "zucchini", "spinach"]

for i in range(len(veggies)):
    if len(veggies[i])>5:
        print(f"I love {veggies[i]}")

# problem 1.1
# random_data = ["b", "a", 1, 3, 99, "c"]
# print(random_data[4])
# print(random_data[2] + 10)
# print(random_data[1] + random_data[0])

# problem 1.2
# numeric_data = []
# numeric_data.append(2)
# numeric_data.append(4)
# numeric_data.append(6)
# numeric_data.append(8)
 
# print(len(numeric_data))
# print(numeric_data[1])

# problem 1.3
# my_list = ["dog", 5, "cat", 2, "horse", 1]
# print(my_list[6]) #out of range error
# print(my_list[-1])
