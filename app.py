from flask import Flask
from resources.presence import presences

app = Flask(__name__)

app.register_blueprint(presences)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)