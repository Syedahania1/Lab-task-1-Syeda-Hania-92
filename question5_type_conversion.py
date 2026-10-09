age = 20
item = 5

print("Before type conversion:")
print("age:", age)
print("items:", item)

age = float(age)
item = float(item)

print("After type conversion:")
print("age:", age)
print("items:", item)

print("Explanation:")
print("Initially, age and item are integers (int).")
print("The float() function converts both values into floating-point numbers (float).")
print("Therefore, 20 becomes 20.0 and 5 becomes 5.0.")
