from flask import Flask
from views import views


#creates the app

app = Flask(__name__)

#connects to the blueprints/routes made in views.py
app.register_blueprint(views, url_prefix= '/')

#creating a route

# @app.route('/')
# def home():
#         return "this is the home page"

# ^ can also just be HTML


if __name__ == '__main__':
    app.run(debug=True, port = 8000)

#debug refreshes the page when you make changes
#default port is 5000

#python -m pip install pyodbc
#pip install Flask
#https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16#download-for-windows