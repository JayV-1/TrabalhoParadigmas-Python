def check_fields(name, password, hobbie):
    # print(len(name))
    # print(password)
    # print(hobbie)

    if len(name) < 3:
        return "O campo Nome está com menos de 3 caracteres."

    if len(password) < 3:
        return "O campo Senha está com menos de 3 caracteres."

    if len(hobbie) < 3:
        return "O campo Hobbie está com menos de 3 caracteres."

    return True
