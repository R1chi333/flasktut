from flask import render_template, request, redirect, url_for, Blueprint
from sql import getData, insertData

#defining the blueprint
views = Blueprint(__name__, "views")

#using render template to connect the html
@views.route('/')
def home():
    return render_template("index.html", name="tracy")


#dynamic url
@views.route('/profile/<username>')
def profile(username):
    return render_template("index.html", name=username)

#query parameter 
@views.route('/searchProfile')
def searchProfile():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)

@views.route('/allProfile')
def allProfile():
        data = getData()
        return data


@views.route('/ListProfile', methods=['GET', 'POST'])
def ListProfile():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        age = request.form.get('age')
        email = request.form.get('email')
        insertData(first_name, last_name, age, email)
        return redirect(url_for('views.ListProfile'))  # Redirect to the same page to refresh
    data = getData()  # Make sure this function returns the list of profiles
    return render_template('listProfile.html', profiles=data)



