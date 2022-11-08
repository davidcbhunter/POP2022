word = "antifragile"

base = "  -----\n \
 |\n \
 |\n \
 |\n \
 |\n \
/ \u29F5 "

one_mistake = "  -----\n \
 |  |\n \
 |\n \
 |\n \
 |\n \
/ \u29F5 "

two_mistakes = "  -----\n \
 |  |\n \
 |  O\n \
 |\n \
 |\n \
/ \u29F5 "

three_mistakes = "  -----\n \
 |  |\n \
 |  O\n \
 |  |\n \
 |\n \
/ \u29F5 "

four_mistakes = "  -----\n \
 |  |\n \
 |  O\n \
 | /|\n \
 |\n \
/ \u29F5 "

five_mistakes = "  -----\n \
 |  |\n \
 |  O\n \
 | /|\u29F5\n \
 |\n \
/ \u29F5 "

six_mistakes = "  -----\n \
 |  |\n \
 |  O\n \
 | /|\u29F5\n \
 | /\n \
/ \u29F5 "

seven_mistakes = "  -----\n \
 |  |\n \
 |  O\n \
 | /|\u29F5\n \
 | / \u29F5\n \
/ \u29F5 "

mistakes = [base,one_mistake,two_mistakes,\
            three_mistakes, four_mistakes, \
            five_mistakes, six_mistakes,
            seven_mistakes]
mis_guessed_letters = []
correct_letters = []

blank_word = ""

for x in word:
    blank_word += "_"

#print(blank_word)

while len(mis_guessed_letters) < 7 and blank_word != word:
    print(mistakes[len(mis_guessed_letters)])
    print("\n" + "word: " + blank_word)
    print("incorrect letters: " + str(mis_guessed_letters))
    letter = input("Please guess a letter \n")
    if not letter.isalpha():
        print("You need to guess a letter")
    if len(letter) > 1:
        print("You can only guess one letter at a time")
    if letter.lower() in word:
        if not letter.lower() in correct_letters:
            correct_letters.append(letter.lower())
            for x in range(len(word)):
                if word[x] == letter:
                    blank_word = blank_word[:x] + letter + blank_word[x+1:]
        else:
            print("You already guessed this letter")
    else:
        mis_guessed_letters.append(letter.lower())
    print("\n\n")

if blank_word == word:
    print(blank_word)
    print("Nice job! You did it!")
elif blank_word != word:
    print(mistakes[len(mis_guessed_letters)])
    print("\n Oh no! You killed him!")
