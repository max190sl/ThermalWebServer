from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def root():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title' : 'Max''s web page',
        'time' : timeString
    }
    return render_template('index.html', **templateData)

@app.route('/time')
def dtime():
    now = datetime.datetime.now()
    timeString = now.strftime("%H")
    templateData = {
        'title' : 'Swedish Time',
        'time' : timeString
    }
    return render_template('time.html', **templateData)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
