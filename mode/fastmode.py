#how to find mode faster

dataset = [2,3,4,2,4,56,75,78,8]
def fastmode(dataset):

  largest = max(dataset)
  tallies = [0 for x in range(largest+1)]
    
  for item in dataset:
   tallies[item] = tallies[item] + 1
  return tallies

print(fastmode(dataset))
