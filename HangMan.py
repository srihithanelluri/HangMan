import random
WORDS = ("swift", "secret", "abolish", "caring","science",  "contrast","evolve","derive", "habitat", "fantasy", "glimpse", "horizon", "impulse")
word = random.choice(WORDS)

name = input("What is your name? ")

print ("Hello, " + name, "Time to play hangman!")

print ("Start guessing...")
guesses = ''

turns = 10

while turns > 0:         
    failed = 0             

    for char in word:      

        if char in guesses:    

            print (char,end=""),

        else:
            print ("_",end=""),
            failed += 1 


    if failed == 0:        
        print (" Great job! You won")

        break            

    guess = input(" guess a character:") 
    if len(guess) > 1:
      raise ValueError("Only one character at a time please:)")

    guesses += guess                    


    if guess not in word:  


        turns -= 1        


        print ("This letter is not in the word. Try Again. ")  

        print ("You have", + turns, 'more guesses' )

        if turns == 0:           
            print ("So close! You Lose. Your word was " + word)
