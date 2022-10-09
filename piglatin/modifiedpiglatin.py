#punction and captitalized

def piglatinify(word):
    
    first = word[0]
    if first in 'aeiouAEIOU':
        result = word + 'ay'
    else:
    
      if first == first.upper():
        # move first letter to end and add 'ay'
        result = word[1:].capitalize() +first.lower() +'ay'

      else:
         result = word[1:] + first + 'ay'
      
    return result


# Testing
test_word = "Hello" + '.'
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "Able" + '.'
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = 'Cable'+ '.'
result = piglatinify(test_word)
print(test_word," -> ",result)


#word[-1] = last letter