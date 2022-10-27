verbs = []
for i in range(2):
  verb='ate','walked','slept'
  verbs.append(verb)

nouns = []
for i in range(2):
  noun='dog','hammer','cat','car','frog'
  nouns.append(noun)
  

print(f"Sam {verb[0]} the {noun[0]} and then {verb[1]} the {noun[1]} later.")



#####
import random 

verbs = ['ate','walked','slept']
value = random.choice(verbs)
for i in range(2):
  verb='ate','walked','slept'
  verbs.append(verb)
value = random.choice(verbs)

nouns = ['dog','hammer','cat','car','frog']
value2 = random.choice(nouns)
for i in range(2):
  noun='dog','hammer','cat','car','frog'
  nouns.append(noun)
value2 = random.choice(nouns)



print(f" Sam " + value + " " "the " + value2 +  " " "and then" " " + value +  " " "the " + value2 + " " "later.")