#10/3 class (going over list)
# Stings are immutable. Can't be changed after created. But, we can change lits directly. 

s = "this is a string"
elist= []
l1= [11,33,15,20]
l2= ['one','two','three']
l3= ['one', 2,122,33,'something',23]
l4= ['one',23,['a','b','c'],5,[10,11,12]]
slice= l1[3:5]
longer_string = s + s
longer_list= l1 + l3

def change_in_place_and_return(l,index,new_value):
  l[index]= new_value
  return l

print(l1)
l1=change_in_place_and_return(l1,4,321)


#aliasing= "known as shallow copy"
#following function paradigm:
def change_value(l,index,value):
  result= []
  for item in l:
    result = result +[item]
  result[index]=value
  return result


#list2.py
def avg(l):
  #calculate the sum of the item 
  #then divide the sum of the item
  sum = 0
  for item in l:
    sum = sum + item 
#divide by the number of items
  average = sum / len()
  return average

Grades: [90,95,100,90]
print("grades:", grades)
average = avg(grade)