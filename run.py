from app import create_app
from flask import session

flask_app = create_app()

if __name__ == " __main__":
    flask_app.run(debug=True)
    session["customer_id"] = None