from google.cloud.firestore_v1 import FieldFilter

from app.firestore.firestoreInit import db, usersCollection


def uploadUser(name, password, hobbie):
    try:
        doc_ref = usersCollection.document("users")
        doc_ref.set({
            "name": name,
            "password": password,
            "hobbie": hobbie
        })
    except Exception as e:
        print(e)


# ir no banco -> pegar o objeto -> transformar em uma lista -> devolver essa lista
def get_all_users():
    try:
        users_ref = usersCollection
        docs = users_ref.stream()

        users = []

        for doc in docs:
            users.append(doc.to_dict())

        return users
    except Exception as e:
        print(e)


def get_specific_user(name, password):
    try:
        docs = ((usersCollection
                 .where(filter=FieldFilter("name", "==", name))
                 .where(filter=FieldFilter("password", "==", password)))
                .limit(1)
                .stream())

        for doc in docs:
            user = doc.to_dict()

        return user

    except Exception as e:
        print(e)


def update_hobbie(id, hobbie):
    try:
        user_ref = usersCollection.document(id)
        user_ref.update({
            "hobbie": hobbie
        })

    except Exception as e:
        print(e)
