from flask import Flask
from flask_cors import CORS # Import CORS to allow cross-origin requests

app = Flask(__name__)
# Enable CORS for the entire app
CORS(app)

@app.route('/api/hello')
def hello_world():
    # This message will be sent to the front-end
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the server on port 5252 and make it accessible externally
    app.run(host='0.0.0.0', port=5252)
