import re
import collections

text = open('book.txt').read().lower()
words = re.findall('\w+', text) # This fondall method is to pass a string and find words. It ensures that all occurences of the pattern are found. The pattern we are using is the \w+. The w denotes anythong that is now whitespace. The plus denote one or more. So that means that the occurrence of one or more words which are not a space are counted as words. 
print(collections.Counter(words).most_common(10)) #The counter method counts how many ocurrences there are. And the most common metod limits the result to 10 words. 
# The tuples that appear in the printed words are each words how many times does it appear. 