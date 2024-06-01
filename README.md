# Flask Backend Template

This is a basic template for starting a Flask backend project with SQLAlchemy and Flask-Migrate.

## Project Structure

## Setup

1. **Clone the Repository:**

   git clone https://github.com/Skomorac/flask_sqlalchemy_project new_project
   cd new_project

## Create a Virtual Environment

python3 -m venv venv
source venv/bin/activate

## Install Dependencies:

pip install -r requirements.txt

## Update Environment Variables

Update the .env file with your database URI and secret key.

## Initialize the Database

flask db upgrade

## Run the Application:

python app.py

## For production deployment, use Gunicorn

gunicorn -w 4 -b 0.0.0.0:8000 app:app
