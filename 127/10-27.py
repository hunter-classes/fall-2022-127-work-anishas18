import datetime
import random

def findLargest(dataset):
    largeSoFar = dataset[0]
    for item in dataset[1:]:
        if item > largeSoFar:
            largeSoFar = item
    return largeSoFar


print(findLargest(1000,100))

def testMode(size,maxValue):
  dataset = buildRandomlist(size,maxValue)
  print(dataset)
  m = mode(dataset)
  print(m)

print(testmode(1000,25))