# Last Letter Word
# Program created by : The Sachin Patel
# Date created on by: 12/11/21


def asker(phrase, name):
    while not name.isalpha():
        print(phrase)
        name = str(input())
    return name


def liner():
    print("-------------------------------------------")


#Introducing the Game and asking for first player's name
print('Hello! lets play lastLetterWord game')
liner()
print('Please enter your name')
x = str(input())
x = asker("Please enter your name. Only alphabets.", x)
liner()
print("Hello " + x)
liner()
print("What is your friend's name?")
liner()

#Asking for second player's name
friendName = str(input("Enter your friend's Name "))
friendName = asker("Please enter the name of your friend. Only alphabets.",
                   friendName)
liner()
if friendName != "hello":
    if friendName.lower() == x.lower():
        friendName = friendName + " Number 2"
        print("Hello " + friendName + "! Hope you are ready for the game...")
        x = x + " Number 1"
    else:
        print("Hello " + friendName.lower() +
              "! Hope you are ready for the game...")

liner()

# Explaining the rules of the game
print("So we are going to be playing the Last Letter Word Game!")
liner()
print("Let me tell you the rules:")
print(
    "Basically one of us start out with a word, and then whatever the last letter is of that word, the opponent player has to say a word that starts with that letter."
)

# Asking if they understood
while True:
    try:
        answer = str(input("Understood? say yes or no ").lower())
        # print("num:", num)
        if answer == "yes" or answer == "y":
            print("Ok, good! Let's start")
            break
        if answer == "no" or answer == "n":
            liner()
            print("let me explain again!")
            print("If I started with the word Apple")
            print("The last letter of the Apple is 'E' ")
            print("So you have to say the next word starting with 'E'")
            print("For example a word like 'eagle' ")
            answer = str(input("Understood?"))
            if answer == "yes" or answer == "y":
                liner()
                print("Ok, good! Let's start")

            if answer == "no":
                print(
                    "Sorry I can't explain any better. Maybe go ask someone to explain better than me, and then we can play!"
                )
                exit()

            break
        if answer != "yes" or answer != "no":
            liner()
            print(
                "Please press either yes or no to express if you understood or not"
            )
            liner()

    except ValueError:
        liner()
        print(
            "Please write either yes or no to express if you understood or not"
        )
        liner()

liner()
liner()

# Starting the game
word_list = []
players = [x, friendName]
whoPlayedJustNow = []
print("Ok " + x + " start the game!")
print("Say a word")
liner()
player1word = str(input())
player1word = asker("Please enter a word. Only alphabets.", player1word)
# while not player1word.isalpha():
#   print("Please enter a word. Only alphabets.")
#   player1word = str(input())

whoPlayedJustNow.append(x)
last_letter = player1word[-1]

word_list.append(player1word)
while True:
    for i in players:
        if (whoPlayedJustNow[-1] == players[0]):
            liner()
            print("Ok " + players[1] +
                  " your turn! start the next word with '" + last_letter + "'")
            newWord = str(input())
            newWord = asker("Please enter a word. Only alphabets.", newWord)
            # while not newWord.isalpha():
            #   print("Please enter a word. Only alphabets.")
            #   newWord = str(input())
            while not newWord[0] == last_letter:
                print("Please enter a word that starts with '" + last_letter +
                      "'")
                newWord = str(input())
            if newWord in word_list:
                liner()
                print("Sorry you said " + newWord +
                      ", which has already been said! Sorry you lost ;(  " +
                      players[0] + " won!!!")
                print("The trophy goes to " + players[0])
                exit()
            word_list.append(newWord)
            last_letter = newWord[-1]
            whoPlayedJustNow.append(players[1])
            liner()

        # The second player's turn
        else:
            print("Ok " + players[0] +
                  " your turn! start the next word with '" + last_letter + "'")
            newWord = str(input())
            while not newWord.isalpha():
                print("Please enter a word. Only alphabets.")
                newWord = str(input())
            newWord = asker("Please enter a word. Only alphabets.", newWord)
            # while not newWord[0] == last_letter:
            #   print("Please enter a word that starts with '" + last_letter + "'")
            #   newWord = str(input())
            if newWord in word_list:
                liner()
                print("Sorry you said '" + newWord +
                      "', which has already been said! Sorry you lost ;(  " +
                      players[1] + " won!!!")
                print(word_list)
                liner()
                print("The trophy goes to " + players[1])
                exit()
            word_list.append(newWord)
            last_letter = newWord[-1]
            whoPlayedJustNow.append(players[0])
            liner()
            # print(word_list)
