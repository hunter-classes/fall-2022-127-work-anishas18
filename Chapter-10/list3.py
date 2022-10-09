#5. Write a Python function named max that takes a parameter containing a nonempty list of integers and returns the maximum value. (Note: there is a built-in function named max but pretend you cannot use it.)
def max(lst):
    max = 0
    for e in lst:
        if e > max:
            max = e
    return max
print(max(lst))


#7. Write a function to count how many odd numbers are in a list.
import random

def countOdd(lst):
    odd = 0
    for e in lst:
        if e % 2 != 0:
            odd = odd + 1
    return odd

# make a random list to test the function
lst = []
for i in range(100):
    lst.append(random.randint(0, 1000))

print(countOdd(lst))

#8. Sum up all the even numbers in a list.

def sumEven(lst):
    for i in lst:
        if i%2==0:
            return i