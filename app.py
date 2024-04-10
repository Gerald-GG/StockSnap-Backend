# app.py

from flask import Flask
from routes import auth, stocks

app = Flask(__name__)
app.config.from_pyfile('config.py')

app.register_blueprint(auth.bp)
app.register_blueprint(stocks.bp)

if __name__ == '__main__':
    app.run()
