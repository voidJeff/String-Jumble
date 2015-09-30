"""
stringjumble.py
Author: Jeff
Credit: Me!

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
text = input("Please enter a string of text (the bigger the better): ")
print('You entered "{0}". Now jumble it:'.format(text))
text_l = list(text)
tlen = len(text)

n1 = tlen
while n1 > 0:
    print(text_l[n1-1], end="")
    n1 -= 1
print("")
i = 0
a = 0
b = 0
word_num = text.count(" ") + 1
print(word_num)
while i < tlen:
    
    if text_l[i] != " ":
        a += 1
        i += 1
    else:
        while b <= a:
            print(text_l[b], end="")
            b += 1
    a = 0
    i += 1
    
    
