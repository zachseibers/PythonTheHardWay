#Ex34 Accessing List Items

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale','platypus']

print(f"The animal at 1 is {animals[1]}")
print(f"The third animal in the list is a {animals[2]} and is at 2")
print(f"The first animal of the list is a {animals[0]}")
print("The animal at 3 is a", animals[3])
print("The fifth animal in the list is a", animals[4])
print(f"The animal at 2 is a {animals[2]}")
print(f"The sixth animal is a {animals[5]}")
print(f"The animal at 4 is a {animals[4]}")

for i in range(0,5):
    print(f"The animal at the {i} position is a {animals[i]} ")