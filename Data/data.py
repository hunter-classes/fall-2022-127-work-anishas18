import csv

with open('countries.csv','r') as csv_file:
  csv_reader = csv.reader(csv_file)
  
  for line in csv_reader:
    print(line)
    

print("_______________________________________________")
    
#overall average population
populations = []
with open('countries.csv','r', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  
  for row in reader:
    populations.append(float(row['population']))

print("overall average population: ", sum(populations) / len(populations))

