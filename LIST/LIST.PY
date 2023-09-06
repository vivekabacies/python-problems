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


#Python | Multiply all numbers in the list
my_list=[1,2,3,4,5]
result = 1
for i in my_list:
    result*=i
print(result)


# Python program to find smallest number in a list
my_list = [10,2,9]
smallest = my_list[0]
for i in my_list:
    if i < smallest:
        smallest = i
print("The smallest number in the list is:", smallest)
