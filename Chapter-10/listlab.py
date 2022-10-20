# Write a function to find the smallest value in a list find smallest in a list of items
def smallestnumber(numbers):
    smallest_num = numbers[0]
    for num in numbers:
        if num < smallest_num:
           smallest_num = num
    
    return smallest_num

print(smallestnumber([657,233,567,999,1234,24,89,6,1,888,777,654]))

#Write a function that returns a new list that contains all the odd items in the original list
def onlyodd(lst):
  odd = []
  for i in list:
    if i % 2 == 1:
      odd.append(i)
    return odd

  print(onlyodd([2,3,4,5,6,7,8,9]))

#Write a function that takes a string and returns a new string where all the words are capitalized.
str1 = input("Type anything here ")
print(str1.upper())

#another solution but in function form:
def capitalizeall(sent):
  newStr= ""
  newStr = sent.upper()
  return newStr

#Write a function that takes a string and returns a new string with every word that's longer than 5 characters turned into upper case
def upperfive(sent):
  splitSent = sent.split()
  newest = []
  for i in splitsent:
      if len(i) <= 5:
       newSent.append(i)
      else:
        newSent.append(i.upper())
  jointSent = ' '.join(newSent)
  return jointSent
print(upperfive("hello world, how you doing?"))

#Write a function that takes a list of numbers and returns a new list with each item squared  
def squarelist(l):
  square = []
  for i in l:
    square.append(i ** 2)
  return square

print(squarelist([1,2,3,4,5,6,7,8,9]))
     
#Write a function that takes two lists of numbers and returns a new list where each item is the corresponding value of the original lists added together.
def sumoftwo(num1,num2):
  sumlist = []
  index = 0
  for i in num1 and num2:
      sumlist.append(num1[index] + num2[index])
      index += 1
    return sumlist

print(sumoftwo([1,2,3], [23,24,25])
  
#10)Count how many words in a list have length 5.

def countWords(lst):  
  count = 0 
   i = 0 
   for words in list: 
    if (len(list[i]) == 5):
        count = count + 1
    i = i + 1
   return count

print("the number of words with length = 5 are: ")
print(countWords("animal", "apple","how")))


#11) Sum all the elements in a list up to but not including the first even number.
def sum_of_initial_odds(lst):
    sum = 0
#test if element is odd number - if it's odd, add it to the previous integer
    for i in lst:
        if i % 2 != 0:
            sum = sum + i
#test if element is even number - if it's even, don't include it and break code
        else: 
            break
    return sum

print(sum_of_initial_odds([1,3,1,4,3,8]) == 5)
print(sum_of_initial_odds([6,1,3,5,7]) == 0)
print(sum_of_initial_odds([1, -7, 10, 23]) == -6)
print(sum_of_initial_odds(range(1,555,2)) == 76729)

#12) 