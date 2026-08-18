'''
There is a sequence of words in CamelCase as a string of letters, , having the following properties:

It is a concatenation of one or more words consisting of English letters.
All letters in the first word are lowercase.
For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
Given , determine the number of words in .

Example

There are  words in the string: 'one', 'Two', 'Three'.
'''

# through def
def camelCaseCount(s):
    count = 1
    for char in s:
        if char.isupper():
            count += 1

    return count


# normal
s1 = 'oneTwoThreeFour'
count = 1

for char in s1:
    if char.isupper():
        count += 1

print(count)
print(camelCaseCount(s1))