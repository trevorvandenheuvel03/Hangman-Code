import random
import pygame
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
     ===''', '''
  +---+
  /   |
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
  /\  |
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 _/\  |
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 _/\_ |
  O   |
 /|\  |
 / \  |
  ===''']

#the variable "animalWords", "periodicElements" and "food" will act as a wordbanks for the game. 
#the split method is being implicitly called to split the entire string into a list of strings.
animalWords = 'ant;baboon;badger;bat;bear;beaver;camel;cat;clam;cobra;cougar;coyote;crow;deer;dog;donkey;duck;eagle;ferret;fox;frog;goat;goose;hawk;lion;lizard;llama;mole;monkey;moose;mouse;mule;newt;otter;owl;panda;parrot;pigeon;python;rabbit;ram;rat;raven;rhino;salmon;seal;shark;sheep;skunk;sloth;snake;spider;stork;swan;tiger;toad;trout;turkey;turtle;weasel;whale;wolf;wombat;zebra'.split(";")
periodicElements = "hydrogen;helium;lithium;beryllium;boron;carbon;nitrogen;oxygen;fluorine;neon;sodium;magnesium;aluminum;silicon;phosphorus;sulfur;chlorine;argon;potassium;calcium;scandium;titanium;vanadium;chromium;manganese;iron;cobalt;nickel;copper;zinc;gallium;germanium;arsenic;selenium;bromine;krypton;rubidium;strontium;yttrium;cadmium;silver;tin;antimony;tellurium;iodine;xenon;cesium;barium;europium;osmium;platinum;gold;mercury;lead;bismuth;radon;francium;radium;actinium;uranium;neptunium;plutonium;americium;curium;berkelium;californium;einsteinium;mendelevium;nobelium".split(";")
food = "pizza;burger;pasta;chocolate;cake;salad;poutine;sushi;ramen;fries;popcorn;soup;cupcake;spaghetti;brownie;dumplings;muffin,pie;pudding;scone;sundae;pancakes;waffles;tacos;nachos;sandwich;noodles;rice;donut".split(";")
jobs = "accountant;actor;actress;actuary;advisor;aide;ambassador;animator;archer;artist;astronaut;astronomer;athlete;attorney;auctioneer;author;babysitter;baker;ballerina;banker;barber;bellhop;biologist;blacksmith;bookkeeper;bowler;builder;butcher;butler;cabdriver;calligrapher;captain;cardiologist;caregiver;carpenter;cartographer;cartoonist;cashier;catcher;caterer;cellist;chaplain;chauffeu;rchef;chemist;clergyman;clergywoman;clerk;coach;cobbler;composer;concierge;consul;contractor;cook;cop;coroner;courier;cryptographer;custodian;dancer;dentist;deputy;dermatologist;designer;detective;dictator;director;diver;doctor;doorman;driver;drummer;dry cleaner;ecologist;economist;editor;educator;electrician;emperor;empress;engineer;entertainer;entomologist;entrepreneur;executive;explorer;exporter;exterminator;falconer;farmer;financier;firefighter;fisherman;flutist;foreman;gardener;gatherer;gemcutter;general;geneticist;geographer;geologist;golfer;governor;grocer;guide;hairdresser;handyman;harpist;hobo;hunter;illustrator;importer;instructor;intern;internist;interpreter;inventor;investigator;jailer;janitor;jester;jeweler;jockey;journalist;judge;laborer;landlord;landscaper;laundress;lawyer;lecturer;librarian;librettist;lifeguard;linguis;tlobbyist;locksmith;lyricist;magician;maid;manager;manufacturer;marine;marketer;mason;mathematician;mayor;mechanic;messenger;midwife;miner;model;monk;muralist;musician;navigator;negotiator;notary;novelist;nun;nurse;oboist;operator;ophthalmologist;optician;oracle;orderly;ornithologist;painter;paleontologist;paralegal;pathologist;pawnbroker;peddler;pediatrician;percussionist;performer;pharmacist;philanthropist;philosopher;photographer;physician;physicist;pianist;pilot;pitcher;plumber;poet;police;policeman;policewoman;politician;president;prince;princess;principal;private;producer;professor;programmer;psychiatrist;psychologist;publisher;quarterback;quilter;radiologist;rancher;ranger;receptionist;referee;registrar;reporter;representative;researcher;restaurateur;retailer;retiree;sailor;salesperson;samurai;saxophonist;scholar;scientist;scout;seamstress;senator;sheriff;singer;smith;socialite;soldier;spy;starstatistician;stockbroker;student;surgeon;surveyor;swimmer;taxidermist;teacher;technician;tiler;toolmaker;trader;trainer;translator;tutor;typist;umpire;undertaker;usher;valet;veteran;veterinarian;vicar;violinist;waiter;waitress;warden;warrior;watchmaker;weaver;welder;woodcarver;workman;wrangler;writer;xylophonist;yodeler;zookeeper;zoologist".split(";")
metals = "alloy;aluminum;antimony;brass;bronze;chrome;chromium;copper;cupronickel;gold;gunmetal;iridium;iron;lead;magnesium;mercury;metal;pewter;platinum;silver;steel;tin;titanium;tungsten;uranium;zinc".split(";")
herbs = "allspice;angelica;anise;annatto;basil;bay;berbere;borage;capers;caraway;cardamom;carob;cayenne;chervil;chicory;chives;cicely;cilantro;cinnamon;clove;coriander;curry;dill;epazotelfennel;fenugreek;galangal;;garlic;ginger;harissa;horseradish;hyssop;lavender;licorice;lovage;mace;marjoram;mint;nasturtium;nutmeg;onion;oregano;paprika;parsley;pepper;peppermint;rosemary;rue;saffron;sage;sassafras;spearmint;sumac;tarragon;thyme;turmeric;vanilla;wasabi;watercress;wintergreen;woodruff".split(";")
virtues = "accountability;affection;agreeableness;amiability;benevolence;bravery;care;caring;charity;cleanliness;compassion;concern;confidence;consideration;contentment;cooperation;courage;courtesy;creativity;curiosity;determination;devotion;dignity;diligence;discipline;discretion;duty;earnest;enthusiasm;ethical;excellence;faithfulness;flexibility;focus;forgiveness;fortitude;friendliness;frugality;generosity;gentleness;good;goodwill;grace;graciousness;gratitude;helpfulnes;honesty;honor;honorable;hope;hopefulness;humanity;humility;humor;idealism;impartiality;industry;innocence;integrity;intelligence;joy;joyfulness;justice;kindness;leniency;love;loyalty;magnanimity;mercy;moderation;modesty;moral;morality;nice;nobility;noble;obedience;openness;orderliness;patience;peacefulness;perseverance;persistence;probity;propriety;prudence;purity;purposefulness;questioning;quietreliability;reputable;resilience;resourcefulness;respect;respectfulness;responsibility;restraint;reverence;righteousness;selfdiscipline;selflessness;sensitivity;simplicity;sincerity;spontaneity;steadfastness;strength;sympathy;tact;tenderness;thrift;tolerance;toughness;tranquility;trust;trustworthiness;truthfulness;understanding;unity;upstanding;virtuous;vitality;wholesome;wisdom;wonder;worthiness;worthy;zeal".split(";")

pygame.mixer.init()    
s = "sound"  

def getRandomWord(wordList):                                      # This function returns a random string from the passed list of strings. 
    wordIndex = random.randint(0, len(wordList) - 1)              # The function "randint" is part of the "random" module, and its purpose is to return a random integer between a given range (a,b).  
                                                                  # The varibale "wordIndex" is being randomly assigned to an integer that is in the range of 0 and the the last index of our words list. In this case, the integer that will be assigned to wordIndex will be inbetween 0 and 64. 
    return wordList[wordIndex]                                    # When the getRandomWord function is called, it will return the string in our words list that corresponds to the integer that was assigned to wordIndex. For example, if the integer assigned to wordIndex happened to be 2, the function will return "baboon" 


def getRandomTheme():
    listOfThemes = "animalWords;periodicElements;food;jobs;metals;herbs;virtues".split(";")
    randomThemeNum = random.randint(0, len(listOfThemes)-1)
    theme = listOfThemes[randomThemeNum]
    
    
    if theme == "animalWords":
        return animalWords
    elif theme == "periodicElements":
        return periodicElements
    elif theme == "food":
        return food
    elif theme == "jobs":
        return jobs
    elif theme == "metals":
        return metals
    elif theme == "herbs":
        return herbs
    elif theme == "virtues":
        return virtues
    
def getTheme(secretWord):
    if secretWord in animalWords:
        return "Animals"
    
    elif secretWord in periodicElements:
        return "Periodic Elements"
    
    elif secretWord in food:
        return "Food"
    
    elif secretWord in jobs:
        return "Jobs & Occupations"
    
    elif secretWord in herbs:
        return "Herbs & Spices"
    
    elif secretWord in virtues:
        return "Virtues"
    
    elif secretWord in metals:
        return "Metals & Alloys"
    else:
        return None

def giveHint(secretWord, correctLetters):
    
    for i in range (len(secretWord)):
        if secretWord[i] not in correctLetters:
            guess = secretWord[i]
            return guess
    
def displayBoard(missedLetters, correctLetters, secretWord, level):
    
    print("Level: " + level)
    print("Hints Left: " + str(numHints))############################
   
    print(HANGMAN_PICS[len(missedLetters)])                       # Prints the corresponding hangman picture to the number of missed letters by using the length of missed letters as the index for which HANGMAN_PIC to print 
    print()                                                       # Prints a new line  
    
    if numPlayer == "1":
        print("Theme: " + getTheme(secretWord) )
        print()
    
    elif numPlayer== "2":
        print("MULTIPLAYER")
        print()

    print('Missed letters:', end=' ')                             # Prints the missed letters and ends the string with a space 
    for letter in missedLetters:                                  # Create a For Loop to iterate the following conditions on each letter in the missedLetters list 
        print(letter, end=' ')                                    # Prints each letter and end the string with a space. 
    print()                                                       # Prints a empty line. This is for formatting. 


    blanks = '_' * len(secretWord)                                # Creating a varable, "blanks", and assigning its value to a certain amount of underscores. This amount of underscores is equal to length of the word that must be guessed(secretWord). For example, if secretWord was "cat", blanks would be "_ _ _". 

    for i in range(len(secretWord)):                              # Replace blanks with correctly guessed letters (already in file)
        if secretWord[i] in correctLetters:                       # Checking if the current letter is in the list of correct letters 
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]    # If user guesses the correct letter, the loop will go through each blank and change the underscore to the correct letter. If the user guesses an incorrect letter, the loop will go through each blank and leave it blank. 

    for letter in blanks:                                         # Create a For Loop to iterate the following conditions on each blank letter. 
        print(letter, end=' ')                                    # Print the letter and end the string with a space. 
    print()                                                       # Print an empty line. This is for formatting. 

def getGuess(alreadyGuessed,secretWord, correctLetters):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
     while True:                                                                # Iterate until the user inputs a valid input.                                                   
       
        print('\nGuess a letter.')                                                # Prints a statement that queries the user to input a letter. 
        guess = input()                                                         # Creates the variable "guess" and uses the input function to assign whatever the user inputs as its value. 
        guess = guess.lower()                                                   # Converts the originally inputted guess into a string that is all lowercase. 
        if guess == "hint":
            if useHint() >= 0:
                
                return giveHint(secretWord, correctLetters)+ " "
            else:
                print("You are out of hints")
        elif len(guess) != 1:                                                     # Checks if the length of the inputted guess is not equal to one. 
            print('Please enter a single letter.')                              # If the length of the input is not equal to one, the game prints a statement telling the user to enter asingle letter instead. 
        elif guess in alreadyGuessed:                                           # Checks if the input has already been previously guessed. 
            print('You have already guessed that letter. Choose again.')        # If the input has already been previously guessed, the game prints a statement telling the user to guess a different letter. 
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':                         # Checks if the input is not a lowercase letter. 
        
            print('Please enter a LETTER.')                                     # If the input is not a letter, the game prints a statement telling the user to print a letter. 
        else:                                                                   # If none of these conditions are, the user has inputted a valid guess 
            return guess                                                        # The guess is returned and can be used for the game.   

def getDifficultyLevel():
    
    while True:
        
        print ("\nEnter the number that corresponds to desired difficulty level.")
        print("1 - EASY | 2 - MODERATE | 3 - HARD ")
        level = input()
        
        if len(level) != 1:
            print ("Please enter a single character")
        
        elif level not in '123':
            print ("Please enter 1, 2 or 3")
        
        else:    
            if level == "1":
                level = "Easy"
            
            elif level == "2":
                level = "Moderate"
            
            elif level == "3":
                level = "Hard"
            return level

def getNumHints(level):                                                        #This function determines how many hints the user is given based on the difficulty of the game they select.                                                   
    if level == "Easy":                                                        #If the level selected is "Easy" then the program will return 2 hints for the user. 
        return 2;
    if level == "Moderate":                                                    #If the level selected is "Moderate" then the program will return 1 hint for the user. 
        return 1;
    if level == "Hard":                                                        #If the level selected is "Hard" then the program will return 0 hints for the user, making it exetremely challenging for the user as they are not given any hints. 
        return 0;


def useHint():                                                                 #This function subtracts hints when the user uses a hint to get help to solve the given word. 
    if hintsLeft > 0:                                                          #If the hints the user has left are greater than zero then when the user uses a hint it will subtract one of their hints. 
        return (numHints-1)
    
    else:
        return -1

def getNumPlayer():
    print ("\nEnter the number that corresponds to desired difficulty level.")
    print ("1 - Single Player | 2 - Two Player")
    numPlayer = input()
        
    if len(numPlayer) != 1:
        print ("Please enter a single character")
        
    elif numPlayer not in '12':
        print ("Please enter 1 or 2")
    
    else:
        return numPlayer

def getWord():
    
    while True:
        print ("Player 1: Enter the secret word")
        secretWord = input()
        
        if " " in secretWord:
            print("You can only enter one word")
        
        for i in range(len(secretWord) -1):
            if secretWord[i] not in "abcdefghijklmnopqrstuvwxyz":
                print("You can only enter alphabetical characters")
                
        else:
            return secretWord
    


# =============================================================================
# playAgain() function - MR
# PURPOSE: Determines whether or not the user would like to play again
# IN: Takes a user's input "y" or "no"
# OUT: Prompt statement that asks user if they would like to play again
#      If the player inputs "y" returns True otherwise returns False
# =============================================================================
def playAgain():

    print('Do you want to play again? (yes or no)')     # Prompts user with a print statement  
    return input().lower().startswith('y')              # If the user inputs a lowercase or uppercase "y" function will return true 

# =============================================================================
# SETUP CODE

missedLetters = ''                  # Initializes "missedLetters" as an empty char list. It holds all incorrect letters that the user guesses 
correctLetters = ''                 # Initializes "correctLetters" as an empty char list. It holds all the correct letters that the user guesses
theme= getRandomTheme()
secretWord = getRandomWord(theme)   # Initializes str "secretWord" by calling the getRandomWord() function and passing the str words variable. It holds the word that the user must guess 
gameIsDone = False                  # Initializes "gameIsDone" variable as false. This boolean variable keeps track of whether or not the game is done. When this variable has a value of "True" the game ends. 
level = getDifficultyLevel()
numHints = getNumHints(level)       #############################################
hintsLeft = numHints
numPlayer = getNumPlayer()


if numPlayer == "2":
    secretWord = getWord()
    print("\n"*50)

print('\nH A N G M A N')              # Prints the name of the game upon setup 

if numPlayer == "2":
    print("\nPlayer 2's Turn!\n")

# Iterates until the user specifies that they do not want to play again 
while True:
    
    # Upon every turn, the hangman game board is displayed in the console. 
    # Calls the displayBoard(char list, char list, str) function and passes game information such as the curresnt missed letters, correct letters and the secret word to generate "playing space" 
    displayBoard(missedLetters, correctLetters, secretWord,level)    

    # Calls the getGuess(char list) fuction to prompt the user for their guess 
    # Passes a cnatenated list of the missed letters and correct letters to ensure that the user's current guess hasn't been guessed before 
    guess = getGuess(missedLetters + correctLetters, secretWord, correctLetters)
    
    # Checks if the user's guess is in the secret word 
    if len(guess) > 1:
        numHints = numHints - 1
    
    guess = guess.strip()
    if guess in secretWord:
        correctLetters = correctLetters + guess     # If the user's guess is correct. It is added to the correctLetters char array 
        correctGuess = pygame.mixer.Sound("correctGuess.wav")
        pygame.mixer.Sound.play(correctGuess)
        
        foundAllLetters = True                      # Initializes Boolean variable foundAllLeters to True. This variable keeps track of wheteher or not the player guesses all the correct letters 
        
        # Checks if user guessed all the correct letters. 
        # Uses a for loop to check each index of the secretWord str. 
        for i in range(len(secretWord)):
            
            # If one or more letters in the secretWord str are not in the correctLetters char list, foundAllLetters evaluates to false 
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            
        # If the player finds all the letters the end game code is ran 
        # Outputs a congradulatory statment and sets gameIsDone value to true.  
        if foundAllLetters:
            winGame = pygame.mixer.Sound("WINNERSoundEffect.wav")
            pygame.mixer.Sound.play(winGame)
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    
    #If the guessed letter is not correct it is added to the missedLetters char list. This allows the user to keep track of the letters that they guessed 
    else:
        wrongGuess = pygame.mixer.Sound("wrongGuess.wav")
        pygame.mixer.Sound.play(wrongGuess)
        missedLetters = missedLetters + guess

        # Checks if the player ran out of guesses and lost (full hangman image is achieved) 
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            
            # Calls the displayBoard(char list, char list, str) function to output final game board with the full hangman image 
            displayBoard(missedLetters, correctLetters, secretWord, level)
            # Outputs a "lost game" message to the user. This messages lets the user know the number of incorrect and correct guesses by concatenating the length of the missedLetters char array and correctLetters char array into the message. 
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameOver = pygame.mixer.Sound("gameOver.wav")
            pygame.mixer.Sound.play(gameOver)
            gameIsDone = True                       # Sets gameIsDone boolean variable to true to end the game 

    # If the game is done asks the user if they would like to play again 
    if gameIsDone:
        if playAgain():                             # Calls play again fuction which asks the user if they would like to play again. 
        
            # If the user does want to play again, the missedLetters and correctLetters charList are reset to empty lists 
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False                      # Resets the gameIsDone boolean variable to False so that the user can play again 
            
            theme= getRandomTheme()
            secretWord = getRandomWord(theme)       # Generates new secretWord so that the user can play again 
            numPlayer = getNumPlayer()
            hintsLeft = numHints
            level = getDifficultyLevel()
            numHints = getNumHints(level)       #############################################
            hintsLeft = numHints


            if numPlayer == "2":
                secretWord = getWord()
        else:
            break                                   # Exits while loop and program ends 
