from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')

def first_page():
      return render_template('index.html')

@app.route('/hobby')
def hobby():
    return render_template('hobby.html')

@app.route('/friend')
def friend():
    return render_template('friend.html')

@app.route('/speciality')
def speciality():
    return render_template('speciality.html')

if __name__=='__main__':
    app.run()