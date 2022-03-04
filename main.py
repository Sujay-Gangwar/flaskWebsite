from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
     return render_template('contact.html')

@app.route("/post")
def post():
    return render_template('post.html')

@app.route("/post1")
def post1():
    return render_template('post1.html')
@app.route("/post2")
def post2():
    return render_template('post2.html')

app.run(debug=True)