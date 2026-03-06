from flask import Flask
from flask_cors import CORS  # Import CORS to handle cross-origin requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes so front-end can communicate with back-end

# Define the /api/hello route that returns a simple string
@app.route('/api/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the server on all network interfaces on port 5252
    app.run(host='0.0.0.0', port=5252)
