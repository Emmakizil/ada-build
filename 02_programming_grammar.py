# 1, 2, and 3 are instances of the class int, and the operations we can do are math operations.
# "hello", "good bye", and "see ya" are instances of the class str, and the operations we can do include capitalization and concatenation.

print(type(1))
print(type("ada"))

# Assignment Statements
dog_name = "Rosa"
cat_name = "Raquel"
dog_age = 7
cat_age = 11

print("The dog named", dog_name, "is", dog_age, "yeard old.")
print("The cat named", cat_name, "is", cat_age, "years old.")

# Compound assignment statements
x = 2
y = 5
x += 3 
x += y + 3
x -= 2
x -= y - 5
x /= 3
x //= 3
x *= y
x %= y

print("x =", x)
print("y =", y)

# Details about string: https://docs.python.org/3/tutorial/introduction.html#strings

# problem 3.11
my_string = "I love Python"
print(my_string[2:6] , my_string[7:13] , my_string[2:6])
print(my_string[2:6] + my_string[7:13] + my_string[2:6])
print('Two strings without a comma or "+" ' 'are concatenated automatically.')