from app import app
from flask import render_template, request
from app.firestore.firestoreLib import get_all_users, get_specific_user
from app.utils.utilities import check_fields

@app.route("/")
def home():
    return render_template('index.html', users=get_all_users())

@app.route("/", methods=["POST"])
def handle_form():
    name = request.form.get('name')
    password = request.form.get('password')
    hobbie = request.form.get('hobbie')

    if not check_fields(name, password, hobbie):
        return render_template('indexEmpty.html')

    if not get_specific_user(name, password) is None:


        return render_template('index.html', users=get_all_users())

    return "usuário não existe no banco."
