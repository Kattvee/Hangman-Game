# Hangman game

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, guessedWord, guess):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    p = 0
    for char in secretWord:
        if char == guess: 
            guessedWord[p] = guess
        p += 1
    return guessedWord 

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','']
    alpha1 = alpha[:]
    for char in lettersGuessed :
        alpha1.remove(char)
    return alpha1

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    c = 0
    lettersGuessed = []
    guessedWord = ['_']*len(secretWord)
    print('The word has', len(secretWord),'letters. You have',8-c,'guesses.') 
    guess = input('Enter your first guess: ')
    guess = guess.lower()
    if guess not in alpha: 
        print('Error. Input a valid letter.')
        guess = ''
    elif guess in secretWord: 
        print('Correct!') 
        guessedWord = getGuessedWord(secretWord, guessedWord, guess)
        checkerWord = ' '.join(guessedWord)
        print('Your word is now:', checkerWord)
    else: 
        print('Incorrect.')
        checkerWord = ' '.join(guessedWord)
        print( 'Your word so far is blank:', checkerWord)
        c += 1
    lettersGuessed.append(guess)
    checkerWord = ''.join(guessedWord)
    
    while checkerWord != secretWord :
        print(secretWord)
        print('Here are the remaining letters to choose from:', getAvailableLetters(lettersGuessed))
        print('You have', 8-c, 'guesses left.')
        guess = input('Guess another letter: ')
        guess = guess.lower()
        if guess not in alpha: 
            print('Error. Input a valid letter.')
        elif guess in lettersGuessed:
            print('Letter already used.')
            checkerWord = ' '.join(guessedWord)
            print('Your word is still:', checkerWord)
        elif guess in secretWord: 
            lettersGuessed.append(guess)
            print('Correct!') 
            guessedWord = getGuessedWord(secretWord, guessedWord, guess)
            checkerWord = ' '.join(guessedWord)
            print('Your word is now:', checkerWord)
        else: 
            lettersGuessed.append(guess)
            print('Incorrect.')
            checkerWord = ' '.join(guessedWord)
            c += 1
            if c >= 8 :
                print('You have run out of guesses. Your word was:',secretWord)
                return secretWord
            print('Your word is still:', checkerWord)
        checkerWord = ''.join(guessedWord)
    return print('You win! The word was:', secretWord)
    




secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
