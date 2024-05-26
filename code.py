print("Hello World!")

#Variables and Data Types

x = 10
y = 20.5
# String
name = "Ritik"
# Boolean
is_active = True

print(x, y, name, is_active)

#Lists
numbers = [1, 2, 3, 4, 5]

# Accessing elements
print(numbers[0])  # First element
print(numbers[-1])  # Last element

# Adding elements
numbers.append(6)

# Removing elements
numbers.remove(3)

print(numbers)


# Dictionary 
student = {
    "name": "Yashvi",
    "age": 23,
    "courses": ["Math", "Science"]
}

# Accessing values
print(student["name"])
print(student["courses"])

# Adding a new key-value pair
student["grade"] = "A"

print(student)

# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
