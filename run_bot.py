import telebot
from config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)
controller = {}

INVALID_CHOICE = "Введите, пожалуйста, другой вариант - одно число из списка вариантов выше."

parts_pet = []

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id,
                     """               
                     Вы сладенько укрылись одеялом, закрыли глаза и провалились в сон. 
                     \U000023F9 Тут же перед вами возникла приборная панель с четырьмя кнопками.
                     \U000025B6 Каждая подписана. На какую вы нажмете? Введите одно число.
                     [1] Кнопка "Ваше домашнее животное" 
                     [2] Кнопка "Вы на 20 лет старше"
                     [3] Кнопка "Полная противоположность вас"
                     [4] Кнопка "Известная личность"
                     [5] Кнопка "Самый счастливый человек на Земле"
                     [6] Кнопка "Ваш преподаватель по проектному программированию"
                     """)
    user_id = message.from_user.id
    controller[user_id] = 'start'


@bot.message_handler(content_types=['text'])
def start(message):
    user_id = message.from_user.id
    user_choice = message.text
    user_state = controller.get(user_id, 'start') # Если вдруг такой user_id не сохранен, то считаем, что статус = start
    if user_state == 'start':
        answer = start_handler(user_id, user_choice)
    if user_state == 'teacher':
        answer = teacher_handler(user_id, user_choice)
    if user_state == 'head_pet':
        answer = pet_handler_head(user_id, user_choice)
    if user_state == 'body_pet':
        answer = pet_handler_body(user_id, user_choice)
    if user_state == 'wings_pet':
        answer = pet_handler_wings(user_id, user_choice)
    bot.send_message(message.from_user.id, answer)

def start_handler(user_id, user_choice):
    if user_choice == "1":
        controller[user_id] = 'head_pet'
        return """
            Вы открываете глаза. И слышите недовольное попискивание. Вы видите перед голову собой...
            [1] Змейки
            [2] Львёнка
            [3] Орлёнка
            """
    if user_choice == "2":
        pass
    if user_choice == "3":
        pass
    if user_choice == "4":
        pass    
    if user_choice == "5":
        pass
    if user_choice == "6":
        controller[user_id] = 'teacher'
        return """
            Вы открываете глаза. Звенит будильник. Перед вами ноутбук с Zoom. Что вы сделаете?
            [1] Выключите будильник и продолжите спать
            [2] Войдете в Zoom и начнете урок
            """
    return INVALID_CHOICE


def teacher_handler(user_id, user_choice):
    if user_choice == "1":
        controller[user_id] = 'start'
        return """
            Перед вами опять возникла приборная панель с четырьмя кнопками.
            На какую вы нажмете в этот раз? Введите одно число.
            [1] Кнопка "Ваше домашнее животное" 
            [2] Кнопка "Вы на 20 лет старше"
            [3] Кнопка "Полная противоположность вас"
            [4] Кнопка "Известная личность"
            [5] Кнопка "Самый счастливый человек на Земле"
            [6] Кнопка "Ваш преподаватель по проектному программированию"
            """
    if user_choice == "2":
        pass
    return INVALID_CHOICE

def pet_handler_head(user_id, user_choice):
    if user_choice == "1":
        parts_pet.append('змейки')
    if user_choice == "2":
        parts_pet.append('львёнка')
    if user_choice == "3":
        parts_pet.append('орлёнка')
    controller[user_id] = 'body_pet'
    return """
               Имел он 4 лапки, но тело малыша было половинами двух тел...
               [1] Дракона - Тигра
               [2] Медведя - Киборга(?с кем вообще можо срестить тело медведя?)
               [3] Волка - Орла
               """
def pet_handler_body(user_id, user_choice):
    if user_choice == "1":
        parts_pet.append('тигро - дракончика')
    if user_choice == "2":
        parts_pet.append('КИБЕР - медвежонка')
    if user_choice == "3":
        parts_pet.append('орлиного - волчёнка')
    controller[user_id] = 'wings_pet'

    return """
               Резко от тела отделяются гигантские крылья, рассмотрев их вы понимаете что они похожи на...
               [1] Крылья летучей мыши черного цвета с густой мягкой шерстью
               [2] Крылья попугая с красно-желто-сине-зеленым оперением
               [3] Огненные крылья
               """
def pet_handler_wings(user_id, user_choice):
    if user_choice == "1":
        parts_pet.append('крыльями летучей мыши')
    if user_choice == "2":
        parts_pet.append('крыльями попугая')
    if user_choice == "3":
        parts_pet.append('огненными крыльями')
    HISTORY_PET = ('Зверенок с головой {}, телом {} и прекрасными {} обнюхав вас радостно завизжал и начал бегать вокруг вас.\n'
                   '\n'
                   'Пока вы смотрели на этот "вихрь", у вас закружилась голова, вы упали наземь потеряв сознание.\n'
                   '\n'
                   'Когда вы пришли в себя то увидели свою комнату...\n'
                   '\n'
                   'Спустя время вы заснули и опять увидели 6 кнопок...(/start если не знаете порядок)'.format(parts_pet[0], parts_pet[1], parts_pet[2]))
    controller[user_id] = 'start'
    return HISTORY_PET
bot.polling()
