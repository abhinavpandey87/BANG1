from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! Welcome to My Website."

    
    
@app.route('/index')
def loan():
    return render_template('index.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)