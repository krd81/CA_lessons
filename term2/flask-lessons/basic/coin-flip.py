from flask import Flask
import random
import json

app = Flask(__name__)

@app.route('/coinflip')
def coin_flip():
    number = random.randint(0,1) # 0 = Heads / 1 = Tails
    if(number == 1):
        result = {'Result': 'Tails'}        
    else:
        result = {'Result': 'Heads'}
    return json.dumps(result)
    
    

if __name__ == '__main__':
    app.run(debug=True)
    


