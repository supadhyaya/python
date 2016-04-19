

sentence = input("please enter a sentence \n")

print(sentence.split())

#split the input sentence based on the white space; by default, split() function breaks the letters with white space
for x in sentence.split():
    print(x+"gedaDhumma", end="")