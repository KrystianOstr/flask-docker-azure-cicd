import os
from flask import Flask

app = Flask(__name__)


port =int(os.environ.get("PORT", 80))

@app.route('/')
def hello():
    return "Hello from Flask inside Docker!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)