import telebot
import controller


class Handler:
    data = []

    def __init__(self, bot):
        self.bot = bot

    def main_menu(self, message):
        user_id = message.from_user.id
        user = controller.get_user(message)
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        if user and user[5] is None:
            msg = self.bot.send_message(user_id, 'Укажите город или населеный пункт, где вы сейчас находитесь.')
            self.bot.register_next_step_handler(msg, self.set_city)
        if user and user[5] is not None:
            user_markup.row('Информация по пересечению границы')
            user_markup.row('Информация для тех кто потерялся или кого-то потерял')
            user_markup.row('Полезная информация от Международного Штаба помощи украинцам')
            user_markup.row('Полезная информация')
            user_markup.row('В главное меню')
            self.bot.send_message(user_id, 'Выберите какую информацию вы бы хотели получить', reply_markup=user_markup)

    def set_city(self, message):
        controller.add_user_city(message, message.text)
        self.main_menu(message)

    def border_crossing(self, message):
        user_id = message.from_user.id
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Молдова')
        user_markup.row('Польша')
        user_markup.row('Румыния')
        user_markup.row('Венгрия')
        user_markup.row('Словакия')
        user_markup.row('Испания')
        user_markup.row('Австрия')
        user_markup.row('Бельгия')
        user_markup.row('Швейцария')
        user_markup.row('Франция')
        user_markup.row('Германия')
        user_markup.row('Украина')
        user_markup.row('Швеция')
        user_markup.row('В главное меню')
        msg = self.bot.send_message(user_id,
                                    'Выберите в списке какую '
                                    'границу вы бы хотели пересечь',
                                    reply_markup=user_markup)
        self.bot.register_next_step_handler(msg, self.step1)

    def step1(self, message):
        user_id = message.from_user.id
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('В главное меню')
        if message.text == 'Молдова':
            reply_text = controller.get_country_data('moldova')
            self.bot.send_message(user_id, reply_text, reply_markup=user_markup)
        elif message.text == 'Польша':
            reply_text = controller.get_country_data('poland')
            self.bot.send_message(user_id, reply_text, reply_markup=user_markup)
        elif message.text == 'Румыния':
            reply_text = controller.get_country_data('moldova')
            self.bot.send_message(user_id, reply_text, reply_markup=user_markup)
        elif message.text == 'Венгрия':
            reply_text = controller.get_country_data('moldova')
            self.bot.send_message(user_id, reply_text, reply_markup=user_markup)
        elif message.text == 'Словакия':
            reply_text = controller.get_country_data('moldova')
            self.bot.send_message(user_id, reply_text, reply_markup=user_markup)
        elif message.text == 'Испания':
            reply_text = controller.get_country_data('spain')
            self.bot.send_message(user_id, reply_text, reply_markup=user_markup)
        elif message.text == 'Австрия':
            reply_text = controller.get_country_data('austria')
            self.bot.send_message(user_id, reply_text, reply_markup=user_markup)
        elif message.text == 'Швейцария':
            reply_text = controller.get_country_data('swiss')
            self.bot.send_message(user_id, reply_text, reply_markup=user_markup)
        elif message.text == 'Бельгия':
            reply_text = controller.get_country_data('belgium')
            self.bot.send_message(user_id, reply_text, reply_markup=user_markup)
        elif message.text == 'Франция':
            reply_text = controller.get_country_data('france')
            self.bot.send_message(user_id, reply_text, reply_markup=user_markup)
        elif message.text == 'Германия':
            reply_text = controller.get_country_data('german')
            self.bot.send_message(user_id, reply_text, reply_markup=user_markup)
        elif message.text == 'Украина':
            reply_text = controller.get_country_data('ukraine')
            self.bot.send_message(user_id, reply_text, reply_markup=user_markup)
        elif message.text == 'Швеция':
            reply_text = controller.get_country_data('sweden')
            self.bot.send_message(user_id, reply_text, reply_markup=user_markup)
        elif message.text == 'В главное меню':
            self.main_menu(message)
        else:
            reply_text = 'Неправльно указано название границы'
            self.bot.send_message(user_id, reply_text, reply_markup=user_markup)
            self.border_crossing(message)

    def lost(self, message):
        user_id = message.from_user.id
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('В главное меню')
        reply_text = controller.get_country_data('lost')
        self.bot.send_message(user_id, reply_text, reply_markup=user_markup)

    def usefull_info_ihhu(self, message):
        user_id = message.from_user.id
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('В главное меню')
        reply_text = controller.get_country_data('info')
        self.bot.send_message(user_id, reply_text, reply_markup=user_markup)

    def usefull_info(self, message):
        user_id = message.from_user.id
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('В главное меню')
        reply_text = controller.get_country_data('links')
        self.bot.send_message(user_id, reply_text, reply_markup=user_markup)
        pass
