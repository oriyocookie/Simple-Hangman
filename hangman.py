
import random
class Hangman():
    def choice(self):
        print("Hi, this is a very basic hangman game. Enjoy")
        print("Press 1 to start the game. Other options to quit")
        difficulty=int(input('Choose now: '))
        if difficulty !=1:
            exit()
            #while 0<difficulty<=3:
             #   print("Please enter the difficulty between 1(Easy),2(Medium),3(Hard)")
              #  difficulty=int(input('or press any other option to quit: '))
        else:
            self.startGame()
    def startGame(self):

        print("The criminal approaches the noose")
        print("ironically he awaits his trial by a game of Hangman")
        print("______________")
        print("|            |")
        print("|            |")
        print("|            |")
        print("|            |")
        print("|            |")
        print("|____________|")
        print("YOU HAVE 6 TRIES BEFORE THE FINAL DECISION IS MADE")
        print("__________________________________________________")
        print("TYPE OUT THE WHOLE WORD, ONCE YOU SOLVE IT")
        attempts=0
        usedLetters=""
        wordList=open("word.txt", "r")
        word=random.choice(wordList.read().split(','))
        progress=[]
        progress.extend(word)
        for i in range(0,len(progress)):
            progress[i]="_"
        while attempts <6:
            guess=str(input("Guess a letter: "))
            if guess in word:
                if guess in usedLetters:
                    print ("you already tried that")
                else:
                    print ("correct")
                    usedLetters += guess + ","
                    self.draw(attempts)
                    print ("Progress: " + self.progressUpdated(guess, word, progress))
                    print ("Letters used so far: " + usedLetters)
            elif guess not in word:
                if guess in usedLetters:
                    print ("you already tried that")
                else:
                    attempts+=1
                    print ("uh oh, Wrong")
                    usedLetters +=guess + ","
                    self.draw(attempts)
                    print ("Progress: " + self.progressUpdated(guess, word, progress))
                    print ("Letters used so far: " + usedLetters)
    def draw(self,attempts):
        if attempts == 0:
	        print("______________")
	        print("|      |     |")
	        print("|            |")
	        print("|            |")
	        print("|            |")
	        print("|____________|")
	        print("Remember to type out the whole word once you're finished")
        elif attempts ==1:
            print("______________")
            print("|      |     |")
            print("|      0     |")
            print("|            |")
            print("|            |")
            print("|____________|")
            print("Remember to type out the word once you're finished")
        elif attempts==2:
            print("______________")
            print("|      |     |")
            print("|      0     |")
            print("|     /      |")
            print("|            |")
            print("|____________|")
            print("Remember to type out the word once you're finished")
        elif attempts ==3:
            print("______________")
            print("|      |     |")
            print("|      0     |")
            print("|     /|     |")
            print("|            |")
            print("|____________|")
            print("Remember to type out the word once you're finished")
        elif attempts ==4:
            print("______________")
            print("|      |     |")
            print("|      0     |")
            print("|     /|\    |")
            print("|            |")
            print("|____________|")
            print("Remember to type out the word once you're finished")
        elif attempts ==5:
            print("______________")
            print("|      |     |")
            print("|      0     |")
            print("|     /|\    |")
            print("|     /      |")
            print("|____________|")
            print("Remember to type out the word once you're finished")
        else:
            print("______________")
            print("|      |     |")
            print("|      0     |")
            print("|     /|\    |")
            print("|     / \    |")
            print("|____________|")
            print("YOU DIED")
            print("few days later Logan Paul found your dead body and filmed it")
            self.choice()

    def progressUpdated(self,guess,word,progress):
        i=0
        while i<len(word):
            if guess ==word[i]:
                progress[i]= guess
                i+=1
            else:
                i+=1
        if guess==word:
            print("you won")
            print("do you want to play another round?")
            option=input('press 1 if you want to play another round ')
            if option=='1':
                self.startGame()
            else:
                exit()
        return "".join(progress)

game=Hangman()
game.choice()

