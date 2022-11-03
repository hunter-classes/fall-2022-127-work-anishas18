#1. find largest(l) which takes in a list of numbers and returns the value of the smallest number


def find_smallest(s):
    list.sort()
    return list[0]


list = [2, 4, 80, 1000, 98, 20]
print(find_smallest(list))

#going over it in class


#def findLargest(dataset):
    #largeSoFar = dataset[0]
    #for item in dataset[1:]:
       # if item > largeSoFar:
           # largeSoFar = item
  #return largeSoFar


#another way to do it
#result = []
#for x in range(size):
  #result.append(random.randrange(maxvalue))
  #return result 
#result = [random.ranrange(maxvalue)for x in range(size)]
#return result 


#2. freq(l,v) which takes a list of numbers (l) and a value (v). The function will return the frequency of v, that is, the number of times that v appears in l.

def freq(l, v):
    frequency = list.count(v)
    return frequency
  
list = [2, 4, 98, 80, 1000, 98, 20, 98]
print("frequency ", freq(list, 98))


#going over it in class
#def freq(l, v):
  #count = 0 
  #for item in dataset:
    #if item == v:
     # count = count + 1
      #return count 
#return len([x for x in dataset if x == v])

print(freq(dataset,98))
print(dataset)



#makes a copy of dataset [x for x in dataset]


#running mode faster

