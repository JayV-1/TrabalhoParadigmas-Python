from app import app
from flask import render_template, request

from app.firestore.firestoreInit import db
from app.utils.utilities import check_fields

# rota home - primeiro carregamento do app
@app.route("/")
def home():
    user = [
        {
            "name": "",
            "hobbie": ""
        },
    ]

    doc_ref = db.collection("users").document("alovelace")
    doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})

    return render_template('index.html', user=user)


@app.route("/", methods=["POST"])
def handle_form():
    # pegando as informacoes do input name
    name = request.form.get('name')
    password = request.form.get('password')
    hobbie = request.form.get('hobbie')

    if not check_fields(name, password, hobbie):
        return render_template('indexEmpty.html')

    user = [
        {
            "name": "jao",
            "hobbie": "jogar"
        },
        {
            "name": name,
            "hobbie": hobbie
        }
    ]

    return render_template('index.html', users=user)
