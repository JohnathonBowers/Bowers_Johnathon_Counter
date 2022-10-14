# I reached out to a TA for help with this assignment. Specifically, I needed help with how to use "session"

from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "74e81622e11216907d126e458f61a8b7"

@app.route('/')
def home_page():
    if 'num' not in session:
        print("key 'num' does NOT exist")
        session['num'] = 1
    else: print("key exists!")
    if session['num'] == 1:
        text = "time"
    else: text = "times"
    return render_template('index.html', text = text)

@app.route('/visits')
def visits():
    session['num'] += 1
    return redirect('/')

@app.route('/visits2')
def visits2():
    session['num'] += 2
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)