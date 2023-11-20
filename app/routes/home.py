from app import app
from flask import render_template, request
from app.firestore.firestoreLib import get_all_users, get_specific_user, update_hobbie, uploadUser
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

    user = get_specific_user(name, password)

    if not user is None:
        update_hobbie(user["documentID"], hobbie)
        return render_template('index.html', users=get_all_users())

    uploadUser(name, password, hobbie)
    return render_template('index.html', users=get_all_users())
