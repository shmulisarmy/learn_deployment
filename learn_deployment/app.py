from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def ri():
    return render_template('index.html')

# @app.route('/')
# def nri():
#     return 'hello world'

if __name__ == '__main__':
    app.run(debug=True)