from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    drinks = ['Coffee','Tea','Milkshake']
    returm render_templete('index.html',drink=drinks)

@app.route('/drink/<dr>')

def drink(dr):
    return "Here is your drink " + str(dr)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)

