from app import app
from flask import render_template, request
from app.firestore.firestoreLib import get_all_users, get_specific_user, update_hobbie, uploadUser, verify_username 
from app.utils.utilities import check_fields


@app.route("/")
def home():
    data = {
        "Users": get_all_users(),
        "message": ""
    }
    return render_template('index.html', data=data)


@app.route("/", methods=["POST"])
def handle_form():
    name = request.form.get('name')
    password = request.form.get('password')
    hobbie = request.form.get('hobbie')

    if not check_fields(name, password, hobbie):
        data = {
            "Users": get_all_users(),
            "message": "Campos em branco, por favor, preencha todos."
        }

        return render_template('index.html', data=data)

    user = get_specific_user(name, password)

    if not user is None:
        update_hobbie(user["documentID"], hobbie)
        data = {
            "Users": get_all_users(),
            "message": "Usuário atualizado com sucesso!"
        }
        return render_template('index.html', data=data)

    username_exists = verify_username(name)

    if username_exists:
        data = {
            "Users": get_all_users(),
            "message": "nome de usuário existe!"
        }
        
        return render_template('index.html', data=data)

    uploadUser(name, password, hobbie)
    data = {
        "Users": get_all_users(),
        "message": "Usuário criado com sucesso!"
    }

    return render_template('index.html', data=data)
