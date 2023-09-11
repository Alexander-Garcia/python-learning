from flask import Flask
app = Flask(__name__)

def make_bold(func):
    def bold():
        return f"<b>{func()}</b>"
    return bold

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello hello</h1>' \
            '<p>This is a paragraph</p>'

@app.route("/bye")
@make_bold
def bye():
    return "adios"

@app.route("/user/<name>/<int:number>")
def greet(name, number):
    return f"hello, {name}. Here is a number: {number}"

if __name__ == "__main__":
    app.run(debug=True)
