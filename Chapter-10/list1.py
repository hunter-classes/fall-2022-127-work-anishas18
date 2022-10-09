#3. 
myList = [76, 92.3, 'hello', True, 4, 76]

#a)
addto_myList = 'apple'
myList.append(addto_myList)
addto_myList = 76
myList.append(addto_myList)

#b)
inserttolist = 'cat'
myList.insert(3,inserttolist)

#c)
inserttolist = 99
myList.insert(0,inserttolist)
print(myList)
#d)
findindex = myList.index('hello')
print(findindex)

#e)
myList = [76, 92.3, 'hello', True, 4, 76]
print(myList.count(76))

#f)
myList = [76, 92.3, 'hello', True, 4, 76]
myList.remove(76)

#g)
myList = [76, 92.3, 'hello', True, 4, 76]
item = myList.pop(3)
print(myList)