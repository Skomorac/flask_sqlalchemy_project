from flask import Flask
from dotenv import load_dotenv
import os
from extensions import db
from models import *
from routes import *
from flask_migrate import Migrate

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
