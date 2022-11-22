#comma separated value  
one,two,three
#tab seperated value 
one  two  three

#eamaple
#file  smith,john,20


"""
example using split
f = open("file.csv")
for line in f.readlines():
  line = line.strip()
  print(line.split(" , "))

#python has a built in csv module

"""
"""
import csv
reader = csv.reader(open("file.csv"))
for line reader:
print(line)
"""

#another example average age
"""
reader = csv.reader(open("file.csv"))
num_people = 0
sum = 0
for line in reader:
  num_people = num_people + 1
  sum = sum +int(line[2])
print(sum/num_people)
"""

"""
#using the csv.dictreader

reader = csv.DictReader(open("file.csv"))
data = []
for item in reder:
 data.append(item)

same thing in one lines of code using list comprihention

reader = csv.DictReader(open("movies.csv"))
data = [x for x in reader]
"""

