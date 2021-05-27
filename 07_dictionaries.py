# Create a dictionary
my_dictionary1 = {}
my_dictionary2 = dict()

rock_paper_scissors_defeats = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"  
}
assert rock_paper_scissors_defeats.get("rock") == "scissors", "rock should defeat scissors"
assert rock_paper_scissors_defeats.get("scissors") == "paper", "scissors should defeat paper"
assert rock_paper_scissors_defeats.get("paper") == "rock", "paper should defeat rock"

# If the program gets here, the code works!
print("Your solution works!")

# Exercise: in the following code segment, print the grade of the student by accessing the value from the dictionary stored in the student variable.
student = {
    "name": "Ada Lovelace",
    "id": 12345,
    "age": 147,
    "grade": 11,
}
print(student["grade"])

#Exercise
my_cat = {
    "name": "Samson",
    "breed": "Alley-cat",
    "age": 8,
}

print(my_cat.get("name")) # "Samson"
print(my_cat["name"]) # "Samson"

print(my_cat.get("has_shots")) # None
#print(my_cat["has_shots"]) # Raises a KeyError

#We can iterate through the keys with a for loop.
my_cat = {
    "name": "Samson",
    "breed": "Alley-cat",
    "age": 8,
}

my_cat_keys = my_cat.keys()
for key in my_cat_keys:
  print(key)

#Or convert the keys into a list using list. But it will no longer be connected to the original dictionary.
my_cat = {
    "name": "Samson",
    "breed": "Alley-cat",
    "age": 8,
}

my_cat_keys = my_cat.keys()
list(my_cat_keys)[0]

#Looping Over a dictionary
my_cat = {
    "name": "Samson",
    "breed": "Alley-cat",
    "age": 8,
}

for key in my_cat:
    print(f"The key is {key} and the value is {my_cat[key]}")

#Excercise: Print out a dictionary
rock_paper_scissors_defeats = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}

for key in rock_paper_scissors_defeats:
    print(f"{key} defeats {rock_paper_scissors_defeats[key]}")
    