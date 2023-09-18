import copy


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


#Python program to print negative numbers in a list
my_list = [1, 2, 3, -1, -5, -10]
for i in my_list:
    if i < 0:
        print("Is_Negative ",i)

Is_Nagetive = lambda x : x < 0  
for i in my_list:
    if Is_Nagetive(i):
        print("Is_Negative :", i)

Is_Nagetive = lambda x : x < 0  
if Is_Nagetive(-1):
    print("Is Negative")
else:
    print("Not Negative")


# Python program to print all positive numbers in a range
for i in range (-3,3):
    if i > 0:
        print("Is_Positive",i)
    else:
        print("Not Positive",i)

Is_positive = lambda x : x > 0
for i in range (-3,3):
    if Is_positive(i):
        print("Is_Positive",i)
    else:
        print("Not Positive",i)


# Python program to print all negative numbers in a range
for i in range (-3,3):
    if i < 0:
        print("Is Negative",i)
    else:
        print("Not Negative",i)

Is_positive = lambda x : x < 0
for i in range (-3,3):
    if Is_positive(i):
        print("Is Negative",i)
    else:
        print("Not Negative",i)


# Remove multiple elements from a list in Python
my_list = [1, 2, 3, 4, 5,"Apple","Orange"]
elements_to_remove = [1, 2, 3, 4, 5]
new_list = [i for i in my_list if i not in elements_to_remove]
print(new_list)


# Python – Remove empty List from List
my_list = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]
filtered_list = [i for i in my_list if i]
print(filtered_list)


# Python | Cloning or Copying a list
original_list = [1, 2, 3, 4, 5]
cloned_list = original_list[:]
print(cloned_list)

original_list = [1, 2, 3, 4, 5]
cloned_list = copy.copy(original_list)
print(cloned_list)

original_list = [[1, 2], [3, 4], [5, 6]]
deep_cloned_list = copy.deepcopy(original_list)
print(deep_cloned_list)


# Python | Count occurrences of an element in a list
my_list = [1, 2, 2, 3, 4, 2, 5]
count_mylist = my_list.count(2)
print(count_mylist)

my_list = [1, 2, 2, 3, 4, 2, 5]
element_to_count = 2
count = len([i for i in my_list if i == element_to_count])
print(count)  


# Python | Remove empty tuples from a list
my_list = [(1, 2), (), (3, 4), (), (), (5, 6)]
filtered_list = [i for i in my_list if i]
print(filtered_list)

# Python | Program to print duplicates from a list of integers
my_list = [1, 2, 3, 2, 4, 5, 4, 6]
count_dict = {}
for num in my_list:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1
print("Duplicate integers in the list:")
for num, count in count_dict.items():
    if count > 1:
        print(f"{num} appears {count} times")


# Python program to find Cumulative sum of a list
my_list = [1, 2, 3, 4, 5]
cumulative_sum = []
current_sum = 0
for num in my_list:
    current_sum += num
    cumulative_sum.append(current_sum)
print("Cumulative sum using loop:", cumulative_sum)

my_list = [1, 2, 3, 4, 5]
cumulative_sum = [sum(my_list[:i+1]) for i in range(len(my_list))]
print("Cumulative sum using list comprehension:", cumulative_sum)


# Function to calculate the sum of the digits of a number
def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10  
        number //= 10         
    return total
my_list = [123, 45, 789, 12]
sum_of_digits_list = [sum_of_digits(number) for number in my_list]
print("Sum of digits for each number in the list:", sum_of_digits_list)


# Break a list into chunks of size N in Python
def chunk_list(input_list, chunk_size):
    for i in range(0, len(input_list), chunk_size):
        yield input_list[i:i + chunk_size]
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3
result = list(chunk_list(my_list, chunk_size))
print(result)


# Python | Sort the values of first list using second list
list1 = [3, 1, 2, 4]
list2 = ["apple", "banana", "cherry", "date"]
pairs = list(zip(list2, list1))
sorted_pairs = sorted(pairs, key=lambda x: x[1])
sorted_list1 = [pair[1] for pair in sorted_pairs]
print(sorted_list1)