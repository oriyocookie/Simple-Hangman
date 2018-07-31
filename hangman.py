
import random #needed to randomize the word from the wordlist
class Hangman():
    def main(self):
        #ask the user if he wants to play
        print("Hi, this is a very basic hangman game. Enjoy")
        print("Press 1 to start the game. Other options to quit")
        difficulty=int(input('Choose now: ')) 
        if difficulty !=1: #exits the game if user picks anything other than 1
            exit()
            #was planning on making a difficulty but will add that later
            #while 0<difficulty<=3:
             #   print("Please enter the difficulty between 1(Easy),2(Medium),3(Hard)")
              #  difficulty=int(input('or press any other option to quit: '))
        else:
            self.startGame() #starts the game
    def startGame(self):
        #draw the beginning screen
        print("You approach the noose")
        print("ironically you can survive the execution if you win a game of hangman")
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
        attempts=0 #initialize the number of attempt
        usedLetters="" #creates the list for used letters
        wordList=open("word.txt", "r") #creates a list from a text file by reading the words from it
        word=random.choice(wordList.read().split(',')) #randomly picks a word from the list
        progress=[] #creates a progress bar
        progress.extend(word) #extends it depending on the number of characters in the word
        for i in range(0,len(progress)): #for loop that adds the underscores to the progress bar. 
            progress[i]="_"
        while attempts <6: #while loop that asks for input from the user until attempts are done
            guess=str(input("Guess a letter: ")) #asks for input
            if guess in word: #if the guess is found in the word
                if guess in usedLetters:
                    print ("you already tried that") #if the guess is in the used letters, it will not count it as a correct guess
                else:
                    print ("correct")
                    usedLetters += guess + "," #adds the guess to the used Letters
                    self.draw(attempts) #draws out the current progress
                    print ("Progress: " + self.progressUpdated(guess, word, progress))
                    print ("Letters used so far: " + usedLetters)
            elif guess not in word:
                if guess in usedLetters:
                    print ("you already tried that")
                else:
                    attempts+=1 #adds to the attempts if the guess was wrong and not used before
                    print ("uh oh, Wrong")
                    usedLetters +=guess + "," #adds the wrong attempt to the used letters list
                    self.draw(attempts) #draws out the current progress
                    print ("Progress: " + self.progressUpdated(guess, word, progress))
                    print ("Letters used so far: " + usedLetters)
    def draw(self,attempts): #function that basically draws out the man hanging
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
            option=input("Press 1 if you would like to give it another shot at surviving: ") #asks user if they want to try again
            if option=='1':
                self.startGame()
            else:
                exit()

    def progressUpdated(self,guess,word,progress):
        i=0
        while i<len(word):
            if guess ==word[i]:
                progress[i]= guess
                i+=1
            else:
                i+=1
        if guess==word: #if the user types out the guess, they win
            print("you won")
            print("do you want to play another round?")
            option=input('press 1 if you want to play another round ')
            if option=='1':
                self.startGame()
            else:
                exit()
        return "".join(progress)

game=Hangman() #an object game is created for the class Hangman
game.main() #starts the game

