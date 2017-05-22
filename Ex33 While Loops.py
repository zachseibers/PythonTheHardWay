#Ex33 While Loops

i = 0
numbers = [] #define empty list

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    
    i += 1 #changed from i = i + 1
    print("Numbers now: ", numbers) # prints the contents of numbers
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers: #looping through the list  titled "numbers", note that num is a new 'counter' variable
    print(num)
