from flask import Flask, render_template, request
import random
#needed for obvious random number generation. I don't remember how to implement pseudo random number generation:/
#   (e) | (Good Luck)
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
reversed_ran = RAN[::-1] #reverses the string

app = Flask(__name__)

@app.route('/')
def index():        #Home page select track
    return render_template('index.html')
    

@app.route('/jebaited', methods=['POST', 'GET'],)
def jebaited():
    RAN = random.choice(TOBE_DECRYPTED) #gets random string from the list above
    reversed_ran = RAN[::-1] #reverses the string
    return render_template('jebaited.html', reversed_string=reversed_ran)
















if __name__ == '__main__':
    app.run(debug=True)
    