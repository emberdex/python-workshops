from flask import Flask, render_template

app = Flask(__name__)

my_hobbies = ["Programming", "Programming", "More programming"]

@app.route('/')
def hello_world():
  return render_template("hello.html")

@app.route('/login')
def loginPage():
    return render_template("login.html")

if __name__ == "__main__":
  app.run()
