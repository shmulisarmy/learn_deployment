from flask import Flask, render_template


app = Flask(__name__)

@app.route('/<string:name>')
def ri(name):
    return render_template('index.html', name = name)

# @app.route('/')
# def nri():
#     return 'hello world'

if __name__ == '__main__':
    app.run(debug=True)