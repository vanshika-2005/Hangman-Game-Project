import random

HANGMAN_PICS = ['''
    +---+
         |
         |
         |
        ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

word_themes = {
    'cars': ['audi', 'bmw', 'mercedes', 'toyota', 'honda', 'ford', 'chevrolet', 'volkswagen', 'nissan', 'volvo', 'tesla', 'subaru', 'mazda', 'lexus', 'jaguar', 'porsche', 'fiat', 'jeep', 'dodge', 'kia', 'hyundai', 'maserati', 'ferrari', 'aston martin', 'rolls royce', 'bentley', 'land rover', 'lamborghini', 'mini', 'lotus', 'maserati', 'cadillac', 'chrysler', 'lincoln', 'infiniti', 'acura'],
    'food': ['pizza', 'burger', 'sushi', 'pasta', 'steak', 'taco', 'sandwich', 'soup', 'salad', 'curry', 'noodles', 'rice', 'kebab', 'lasagna', 'pie', 'pancake', 'waffle', 'ice cream', 'cake', 'cookie', 'donut', 'muffin', 'croissant', 'bagel', 'chocolate', 'cheese', 'bread', 'biscuit', 'sausage', 'bacon', 'omelette', 'fries', 'popcorn', 'pretzel', 'chips', 'cereal', 'pita', 'tortilla', 'hummus', 'guacamole', 'salsa'],
    'colors': ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'white', 'gray'],
    'cartoons': ['mickey mouse', 'spongebob', 'tom and jerry', 'pokemon', 'simpsons', 'powerpuff girls', 'scooby doo', 'bugs bunny', 'dora the explorer', 'peppa pig', 'pokemon', 'naruto', 'dragon ball', 'frozen', 'moana', 'shrek', 'finding nemo', 'minions', 'toy story']
}

def getRandomWord(theme):
    """
    Returns a random word based on the selected theme.
    """
    if theme == 'mixed':
        mixed_words = word_themes['cars'] + word_themes['food'] + word_themes['colors'] + word_themes['cartoons']
        return random.choice(mixed_words)
    else:
        return random.choice(word_themes[theme])

def displayBoard(missedLetters, correctLetters, secretWord):
    """
    Display hangman ASCII art, missed letters, and current progress.
    """
    print()
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', ' '.join(missedLetters))
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    print(' '.join(blanks))

def getGuess(alreadyGuessed):
    """
    Get a valid letter guess from the player.
    """
    while True:
        guess = input('Please guess a letter: ').lower()
        if len(guess) != 1:
            print('Please enter only a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter from the alphabet.')
        else:
            return guess

def playAgain():
    """
    Ask the player if they want to play again.
    """
    return input('Would you like to play again? (y)es or (n)o: ').lower().startswith('y')

def getDifficulty():
    """
    Get the difficulty level from the player.
    """
    while True:
        difficulty = input('Choose difficulty (easy, medium, hard): ').lower()
        if difficulty in ['easy', 'medium', 'hard']:
            return difficulty
        else:
            print('Please choose a valid difficulty.')

def getHint(secretWord, correctLetters):
    """
    Provide a hint for the player.
    """
    hint = random.choice([letter for letter in secretWord if letter not in correctLetters])
    return hint

def getTheme():
    """
    Get the theme from the player.
    """
    while True:
        theme = input('Choose theme (cars, food, colors, cartoons, mixed): ').lower()
        if theme == 'mixed':
            return theme
        elif theme in ['cars', 'food', 'colors', 'cartoons']:
            return theme
        else:
            print('Please choose a valid theme.')

def getGameMode():
    """
    Get the game mode from the player.
    """
    while True:
        mode = input('Choose game mode (single player, multiplayer): ').lower()
        if mode in ['single player', 'multiplayer']:
            return mode
        else:
            print('Please choose a valid game mode.')

def hangman():
    """
    Main game function.
    """
    mode = getGameMode()
    if mode == 'multiplayer':
        print("Welcome to Hangman - Multiplayer Mode!")
    else:
        print("Welcome to Hangman - Single Player Mode!")
        
    theme = getTheme()
    player1_turn = True
    missedLetters = ''
    correctLetters = ''
    secretWord = getRandomWord(theme)
    gameIsDone = False
    difficulty = getDifficulty()
    hint_given = False
    score = 0

    print('| H A N G M A N |')

    while True:
        displayBoard(missedLetters, correctLetters, secretWord)

        if mode == 'multiplayer':
            if player1_turn:
                print("Player 1's turn.")
            else:
                print("Player 2's turn.")

        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters += guess

            if all(letter in correctLetters for letter in secretWord):
             
                print('You guessed it!')
                print('The secret word is "{}"!'.format(secretWord))
                if player1_turn:
                  if mode == 'multiplayer':
                    print('Player 1 wins!')
                else:
                    print('Player 2 wins!')
                gameIsDone = True
        else:
            missedLetters += guess

            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                displayBoard(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!')
                print('The word was "{}".'.format(secretWord))
                if player1_turn:
                  if mode == 'multiplayer':
                    print('Player 2 wins!')
                else:
                    print('Player 1 wins!')
                gameIsDone = True

            # Switch turns when an incorrect guess is made in multiplayer mode
            if mode == 'multiplayer' and not player1_turn:
                player1_turn = not player1_turn

        if not gameIsDone:

            if difficulty == 'hard' and not hint_given:
                hint = getHint(secretWord, correctLetters)
                print(f'Hint: The word contains the letter "{hint}".')
                hint_given = True

        if gameIsDone:
            if playAgain():
                player1_turn = not player1_turn
                missedLetters = ''
                correctLetters = ''
                secretWord = getRandomWord(theme)
                gameIsDone = False
                hint_given = False
                difficulty = getDifficulty()
            else:
                break
            if mode == 'single player':
                break

if __name__ == "__main__":
    hangman()
