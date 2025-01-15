from flask import Flask
from routes import register_routes
from database import init_db

app = Flask(__name__)

# Initialize the database
init_db(app)

# Register routes
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)

