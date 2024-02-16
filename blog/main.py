from flask import Flask, render_template
app = Flask(__name__)

# Define the home page
@app.route('/')
def home():
    return 'Welcome to My Blog!'

# Define other routes as needed
# ...

if __name__ == '__main__':
    app.run(debug=True)