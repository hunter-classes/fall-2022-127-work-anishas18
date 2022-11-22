#dictionary in python

d = {}
d[2] = 12345
d[5] = "hello"
d['hello'] = 'world'
d['list'] = [2,3,4,5,6]
d[(1,2)] = 55
print(d)
d['list'] = 55.3
print(d)


person = {'first' : "John",
          'last' : "Smith",
          'age' : 50}
person['age'] = person['age'] + 1

print(person

k = person.keys()
print(k)
for item in k:
    print('person[' ,item,'] = ' ,person[item])

#convert the dict_keys thing into a list;
Klist = [x in x in person.keys()]
print(dict_value(klist)
print(person.items())

#trupole - it can't change, ex of truepole = (3,5)

for k,v in person.items():
    print (k,v)

for k in person.keys():
  print(k,person[k])