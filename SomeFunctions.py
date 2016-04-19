

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



