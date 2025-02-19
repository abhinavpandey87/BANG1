from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def HOMEPAGE():
    return render_template('HOMEPAGE.html')

    
    
@app.route('/index')
def home():
    return render_template('index.html')
    
@app.route('/about')
def about():
    return render_template('about.html')
    
    

if __name__ == '__main__':
    app.run(debug=True)