
#yaditydo - Evan P. repo initialized python==3.10.10 -> run env/Scripts/activate to enter venv or source env/bin/activate on mac
import sys
import os
import random
#needed for obvious random number generation. I don't remember how to implement pseudo random number generation:/
#   (e) | (Good Luck)
#Question How will we store strings. Do we want it to be random? Perhaps use GPT's AI to give 5 or so sentences for at random for each function? or do we want to just list a bunch of strings? Im going to set a list of string to be passed to each individual function nemo
CSHIFT = 3
SCORE = 0
TOBE_DECRYPTED =[
    'this is thy sentence one',
    'how much wood does a chuck wood',
    'consumer on a daily basis',
    'i used to best firends with nemo',
    'shame those tasty snacks got em again',
    'i dont blame him',
    'i see absolutely no error in logical reasoning within that matter of events',
    'as a famous man once said',
    'on to the next one',
    "why did the tomato turn red because it saw the salad dressing",
    "what did the left eye say to the right eye between us something smells", 
    "why dont scientists trust atoms because they make up everything",
    "why did the math book look so sad because it had too many problems",
    "why do seagulls fly over the sea because if they flew over the bay theyd be bagels",
    "why did the coffee file a police report it got mugged",
    "why did the bicycle fall over because it was two-tired",
    "what do you call a boomerang that doesnt come back a stick",
    "why dont skeletons fight each other they dont have the guts",
    "why dont oysters give to charity because theyre shellfish"]
RAN = random.choice(TOBE_DECRYPTED) #gets random string from the list above
RANSTR_INDEX_VAUE = len(RAN) #retrieves the Index Value string stored in RAN
print(RANSTR_INDEX_VAUE) #PRINTS INTEGER INDEX VALUE
print(RAN) #PRINT RANDOM STRING FROM LIST

def main(): #MAIN GAME LOOP FUNCTION
    print("""Please Enter selected path then press enter:
            a | (easy)
            b | (less-easy)
            c | (more-easy)
            d | (Questionable)""")
    x = input('Enter: ')
    if x == 'a':
        easy(RAN)
    elif x == 'b':
        less_easy()
    elif x == 'c':
        more_easy()
    elif x == 'd':
        questionable()
    elif x == 'e':
        good_luck()
    else:
        print("Invalid Input")
        plyagain = input("Play again? (y/n): ").lower()
        if plyagain == 'y':
            main()
        else:
            sys.exit()
            
    
            
            
def easy(RAN):
    GUESSES = 10
    COUNTER = 0
    reversed_cipher = RAN[::-1]
    print('\n\nLEVEL 1\nDecrypt the following below:\n' + reversed_cipher) 
    while True:
        f = input('Decrypted Sentence: ').lower()

        if f == RAN:
            print("correct! +1 score.\n On to the Next Level!")
            less_easy()
        else:
            COUNTER += 1
            print("incorrect!, Try Again!\n" + reversed_cipher)
            
            if COUNTER == GUESSES:
                print("10 Attempts Used too bad so sad")
                again = input("Play again?\n 'm' to return to main menu. (y/n/m): ").lower()
                if again == 'y':
                    easy(RAN)
                elif again =='m':
                    main()
                else:
                    sys.exit()



def less_easy():
    GUESSES = 10
    COUNTER = 0
    CRAN = random.choice(TOBE_DECRYPTED) #NEW RANDOM STRING FROM LIST FOR THIS CIPHER
    encrypted_string = caesar_cipher(CRAN, 3)
    print('Decrypt the following below: \n', encrypted_string,"\n") 
    while True:
        f = input('Decrypted Sentence: ').lower()
        if f == CRAN:
            print("correct! +2 Score:\tOn to the Next Level!")
        else:
            COUNTER += 1
            print("incorrect!, Try Again!\n", encrypted_string,"\n")

            if COUNTER == GUESSES:
                print("10 Attempts Used too bad so sad")
                again = input("Play again?\n 'm' to return to main menu. (y/n/m): ").lower()
                if again == 'y':
                    less_easy()
                elif again == 'm':
                    main()
                else:
                    sys.exit()

def caesar_cipher(rand, shift):
    
    #Encrypts the given message using Caesar cipher and returns the encrypted string.
    
    # The Caesar cipher only works with uppercase letters
    rand = rand.upper()

    # The encrypted string starts as an empty string
    encrypted_string = ""

    # Loop through each character in the message
    for character in rand:
        # If the character is a letter, encrypt it
        if character.isalpha():
            # Calculate the index of the shifted character
            shifted_index = (ord(character) - 65 + shift) % 26

            # Convert the shifted index back to an uppercase letter and append it to the encrypted string
            encrypted_string += chr(shifted_index + 65)
        else:
            # If the character is not a letter, simply append it to the encrypted string
            encrypted_string += character

    # Return the encrypted string
    return encrypted_string
                
                
def more_easy():
    GUESSES = 10
    COUNTER = 0
    RORAN = random.choice(TOBE_DECRYPTED) #NEW RANDOM STRING FROM LIST FOR THIS CIPHER
    print(RORAN) #test
    cipher13 = rot13(RORAN) #plain text -> rot13
    print("Decrypt the following:\n\n" + cipher13, "\n")
    x = input('\nEnter Decrypted Phrase: ')
    while True:
        f = input('Decrypted Sentence: ').lower()
        if f == cipher13:
            print("correct! +2 Score:\tOn to the Next Level!")
        else:
            COUNTER += 1
            print("incorrect!, Try Again!\n", cipher13,"\n")

            if COUNTER == GUESSES:
                print("10 Attempts Used too bad so sad")
                again = input("Play again?\n 'm' to return to main menu. (y/n/m): ").lower()
                if again == 'y':
                    less_easy()
                elif again == 'm':
                    main()
                else:
                    sys.exit
    
    

    
def rot13(string): #ROT13 Cipher   
    output = ''
    for char in string:
        if char.isalpha():
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            rotated = (ord(char) - base + 13) % 26 + base
            output += chr(rotated)
        else:
            output += char
    return output


def questionable():
    GUESSES = 10
    COUNTER = 0
    COLRAN = random.choice(TOBE_DECRYPTED) #NEW RANDOM STRING FROM LIST FOR
    print("""Ready for a bit of a challenge? This one operates a bit differently than others
          please chease your desired KEY length. Then use the key tp decrypt the message.""")
    usrkey = (input("Please enter a a single word, the longer the harder to decrypt: "))
    key = (len(usrkey))
    grid = [''] * key
    for column in range(key):
        currentIndex = column
        while currentIndex < len(COLRAN):
            grid[column] += COLRAN[currentIndex]

            currentIndex += key
    x = ''.join(grid)
    print('\n')
    print("Decrypt the following:\n" +  x, "\n")
    finale = input('\nEnter Decrypted Phrase: ').lower()
    while True:
        f = input('')
        if f == finale:
            print("correct! +1 Score:\tOn to the Next Level!")
        else:
            COUNTER += 1
            print("incorrect!, Try Again!\n", x,"\n")

            if COUNTER == GUESSES:
                print("This was a tough one! The correct answer was: " + COLRAN)

                again = input("Play again?\n 'm' to return to main menu. (y/n/m): ").lower()
                if again == 'y':
                    less_easy()
                elif again == 'm':
                    main()
                else:
                    sys.exit
    
    

    
    
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':    
    main()