from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/current-time')
def cuurent_time():
    date = datetime.now()
    time = f'{date.strftime("%H")}:{date.strftime("%M")}' 
    return f'<p>{time}</p>'

if __name__ == '__main__':
    app.run(debug=True)
