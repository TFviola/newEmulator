from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    # Renders templates/index.html
    return render_template('index.html')

if __name__ == '__main__':
    # Run in debug mode for local dev. 
    # Access at http://127.0.0.1:5000
    app.run(debug=True)
