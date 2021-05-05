import json
import random
import string

def add_new_user(email, password):
    try:
        with open('app/data/users.json') as json_file:
            users_dict = json.load(json_file)
            file_exists = True
    except:
        users_dict = {}
        file_exists = False

    if file_exists:
        for e in users_dict.items():
            if email == e[1]['email']:
                return None

    wallet_address = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    users_dict[wallet_address] = {}
    users_dict[wallet_address]['email'] = email
    users_dict[wallet_address]['password'] = password

    with open('app/data/users.json', 'w') as f:
        json.dump(users_dict, f, indent=2)
    return wallet_address
