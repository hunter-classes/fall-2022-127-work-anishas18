"""
input: a string representing a word
returns: a new string with the word converted to piglatin

Rules:
if the first letter is a consonent, move it from the start to the end and add "ay"
so "hello" becomes "ellohay"

If the first letter is a vowel, just add "yay" to the end
try to also handle upper case words

"""

#going over hw
def piglatinify(word):
    
    first = word[0]
    if first in 'aeiou':
        result = word.tittle() + 'ay'
    else:
        # move first letter to end and add 'ay'
        result = word.tittle()+ word[1:] +first+'ay'
    
    return result


# Testing
test_word = "hello"
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "able"
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = 'Cable' + '.'
result = piglatinify(test_word)
print(test_word), " -> ",result 





