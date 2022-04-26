import random
from termcolor import colored

listofwords = []
with open ("wordle_5_letters.txt") as file: # Dictionary of 500 5-letter words
# C:\\Users\charl\OneDrive - Edge Hill University\Documents\Documents\ATOM\Projects\
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        listofwords.append(line)

a = random.randint(0, len(listofwords)-1) # Random word out of listofwords
p = listofwords[a]

print("Welcome To Wordle!")
print("Please enter your five letter guesses in lowercase!")

def isinside(letter, word):
    for i in word:
        if letter == i:
            return True
    return False
def secondly(letter, word):
    done = False
    new = ""
    for i in word:
        if done == False:
            if letter != i:
                new = new + i
        else:
            new = new + i
    return new

guess = ""
correct = False
for i in range(6):
    q = p
    if guess != p:
        co = ["", "", "", "", ""]
        i = i + 1
        print("")
        print("Round "+str(i)+". Please enter your guess:")
        guess = input()

        if guess == p: # Correct Answer
            correct = True
            print(colored(guess, "green"))
            print("Congratulations! You guessed the correct answer!")

        else:
            answer = ""
            again = []
            for i in range(len(guess)):
                if guess[i] == p[i]: # Correct Letter Correct Place
                    co[i] = "green"
                    q = secondly(guess[i], q)
                else:
                    again.append(i)

            for i in (again):
                if isinside(guess[i], q) == True: # Correct Letter Wrong Place
                    co[i] = "yellow"
                    q = secondly(guess[i], q)

                else:
                    co[i] = "white" # Wrong Letter Wrong Place

            print(colored(guess[0],co[0]), colored(guess[1],co[1]), colored(guess[2],co[2]), colored(guess[3],co[3]), colored(guess[4], co[4]))

if correct == False:
    print("Bad luck! The correct answer was "+p+". Better luck next time")
