
#yaditydo - Evan P. repo initialized python==3.10.10 -> run env/Scripts/activate to enter venv or source env/bin/activate on mac

import sys
import os
import random
#needed for obvious random number generation. I don't remember how to implement pseudo random number generation:/
#Question How will we store strings. Do we want it to be random? Perhaps use GPT's AI to give 5 or so sentences for at random for each function? or do we want to just list a bunch of strings? Im going to set a list of string to be passed to each individual function nemo

TOBE_DECRYPTED =[
    'this is thy sentence one',
    'how much wood does a chuck wood',
    'consumer on a daily basis',
    'i used to best firends with nemo',
    'shame those tasty snacks got em again',
    'i dont blame him',
    'i see absolutely no error in logical reasoning within that matter of events',
    'as a famous man once said',
    'on to the next one mother fuckas',
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
RANSTR_INDEX_VAUE = len(RAN) #retrieves the Index Value string stored in RAM
print(RANSTR_INDEX_VAUE, RAN)

def main():
    x = input(f"""Please Enter selected path then press enter:
            (a) | easy):
            (b) | less-easy):
            (c) | more-easy):
            (d) | Questionable):
            (e) | Good Luck)
            """).lower()
    if x == 'a':
        easy(RAN)
    elif x == 'b':
        less_easy()
    elif x == 'c':
        more_easy()
    elif x == 'd':
        questionable()
    elif x == 'e':
        goodluck()
    else:
        print("Invalid Input")
        plyagain = input("Play again? (y/n): ").lower()
        if plyagain == 'y':
            main()
        else:
            sys.exit()
            
            
def easy(RAN):
    reversed_cipher = RAN[::-1]
    print("Decrypt the following:\n", reversed_cipher)
    
    
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':    
    main()