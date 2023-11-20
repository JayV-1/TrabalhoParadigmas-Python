def check_fields(name, password, hobbie):
    print(len(name))
    print(password)
    print(hobbie)

    if len(name) < 3:
        return False

    if len(password) < 3:
        return False

    if len(hobbie) < 3:
        return False

    return True
