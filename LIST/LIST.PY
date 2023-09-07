# Python program to interchange first and last elements in a list
my_list = [1, 2, 3, 4]
if len(my_list) >= 2:
    my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)


# Swapping two elements in a list
my_list = [1, 2, 3, 4, 5]
index1 = 1
index2 = 3
my_list[1],my_list[3]=my_list[3],my_list[1]
print(my_list)


# Finding the length of a list
my_list = [1, 2, 3, 4]
list_length = 0
for _ in my_list:
    list_length += 1
print(list_length)

# Alternatively:
print(len(my_list))



# Checking if an element exists in a list
my_list = [1, 2, 3, 4]
element_to_check = 1
if my_list.count(element_to_check):
    print(True)

# Alternatively:
if element_to_check in my_list:
    print(True)


# Different ways to clear a list in Python
my_list=["Apple",1,2,3,"Bus"]
my_list.clear()
del my_list[:]
print(my_list)


# Python | Reversing a List
my_list=["Apple",1,2,3,"Bus"]
print(my_list[::-1])


# Python program to find sum of elements in list
my_list=[1,2,3,4,5]
total = sum(my_list)
print(total)

# Alternatively:
result = 0
for i in my_list:
    result+=i
print(result)


# Python | Multiply all numbers in the list
my_list=[1,2,3,4,5]
multiply = lambda x,y:x*y
result =1
for number in my_list:
    result = multiply(result, number)
print(result)

result = 1
for i in my_list:
    result*=i
print(result)

multiply  = lambda x,y:x*y
result = multiply(5,8)
print(result)

# Python program to find smallest number in a list
my_list = [555,5,44,6,9,9,8,6,1]
my_list.sort()
print("smallest number:",my_list[0])

smallest = my_list[0]
for i in my_list:
    if i < smallest:
        smallest = i
print("The smallest number in the list is:", smallest)


#Python program to find largest number in a list
my_list = [1,5,9,7,8,88]
my_list.sort()
print("Largest number:",my_list[-1])


#Python program to find second largest number in a list
my_list = [1,5,9,7,8,88]
my_list.sort()
print("Second largest number:",my_list[-2])


#Python program to find N largest elements from a list
my_list = [1,5,9,7,8,88]
N = int(input("Enter N:"))
my_list.sort()
print("N largest number:",my_list[-N])


#Python program to print even numbers in a list
even = lambda x:x%2
x = int(input("enter a number:"))
if even(x) == 0:
    print("Is even:",x)
else:
    print("Not Even:",x)

my_list = [1,5,9,7,8,12]
even = lambda x:x%2
for i in my_list:
    x=i
    if even(x) == 0:
        print("Is Even:",x)


# Python program to print odd numbers in a List
odd = lambda x:x%2
x=int(input("Enter a number:"))
if odd(x) != 0:
    print("Is odd:",x)
else:
    print("Not odd:",x)

my_list = [1,5,9,7,8,12]
odd = lambda x:x%2
for i in my_list:
    x = i
    if odd(x) != 0:
        print("Is odd:",x)
    else:
        print("Not odd:",x)


#Python program to print all even numbers in a range
Even_range = lambda x:x%2
for i in range(10):
    x = i
    if Even_range(x) == 0:
        print("Is even:",x)
    else:
        print("Not Even:",x)   


#Python program to print all odd numbers in a range
Odd_range = lambda x:x%2
for i in range(10):
    x = i
    if Odd_range(x) != 0:
        print("Is odd:",x)
    else:
        print("Not odd:",x) 


# Python program to print positive numbers in a list
my_list = [1,2,3,-1,-5,-10]
for i in my_list:
    while 0 < i:
        print(f"Is positive {i}")
        break

my_list = [1, 2, 3, -1, -5, -10]
is_positive = lambda x: x > 0
positive_numbers = [i for i in my_list if is_positive(i)]
for i in positive_numbers:
    print(f"Is positive {i}")