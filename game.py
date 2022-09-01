import math
import random
import graphic

#Create an array of words
words = [
      "inexhaustible",
      "dauntless",
      "ceaselessly",
      "magniloquent"
    ]

#Pick a random word
word = words[math.floor(random.random() * len(words))]
answerArray = []
for i in range(0, len(word)) :
    answerArray.append("_")

print(' '.join(answerArray))

wrongGuess = 0
correctGuess = 0
graphic.draw(wrongGuess)

while (wrongGuess < 6 and correctGuess < len(word)) :
    guess = input("Guess a letter:")
    #Update the game state with the guess
    hasCorrectGuess = False
    for j in range(0, len(word)) :
        if (answerArray[j] == '_' and word[j:j+1] == guess) :
            answerArray[j] = guess
            correctGuess = correctGuess + 1
            hasCorrectGuess = True
    if (not hasCorrectGuess) :
        wrongGuess = wrongGuess + 1
        graphic.draw(wrongGuess)
    print(' '.join(answerArray))
    print('Correct guess = ' + str(correctGuess))
    print('Wrong guess = ' + str(wrongGuess))

if (correctGuess == len(word)) :
    print ('You win!')
else :
    print ('You lose! The correct answer is ' + word)
