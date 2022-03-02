import model
import codecs

def get_user(message):
    user_id = message.from_user.id
    user = model.get_user_byid(user_id)
    if user:
        return user
    else:
        add_user(message)


def add_user(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    user = {'user_id': user_id, 'first_name': first_name, 'last_name': last_name, 'username': username}
    model.add_new_user(user)


def add_user_city(message, city):
    user_id = message.from_user.id
    model.add_user_city(user_id, city)


def get_country_data(country_name):
    file_name = country_name + ".txt"
    data = codecs.open(file_name, 'r', 'utf-8')
    data_text = data.read()
    return data_text



