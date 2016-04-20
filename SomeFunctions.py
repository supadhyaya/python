""" we are trying to create a function just to play around the built in function of the python a bit"""

#get the first letter of the word
def first_letter(word):
    letter = []
    for x in word:
        letter.append(x)
    print(letter.pop(0))


#get the last letter of the word
def last_letter(word):
    letter = []
    for x in word:
        letter.append(x)
    print(letter.pop(-1))

#take the middle letter of the word
def mid_letter(word):
    letter = []
    length = int(len(word)/2) #get the index of the middle letter in the word
    for x in word:
        letter.append(x)
    print(letter.pop(length))

#sort the letters of the word using alphabets from Aa- zZ
def sort_letters(word):
    letter = []
    for x in word:
        letter.append(x)
    print(sorted(letter))


