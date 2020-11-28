import telebot
from config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)
controller = {}

INVALID_CHOICE = "Введите, пожалуйста, другой вариант - одно число из списка вариантов выше."

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
    #answer = 'none'
    if user_state == 'start':
        answer = start_handler(user_id, user_choice)
    if user_state == 'teacher':
        answer = teacher_handler(user_id, user_choice)
    if user_state[:5] == 'older':
        answer = older_handler(user_id, user_choice)
    bot.send_message(message.from_user.id, answer)


def start_handler(user_id, user_choice):
    if user_choice == "1":
        pass
    if user_choice == "2":
        controller[user_id] = 'older'
        return """
            Вы открываете глаза. Вы проснулись, но без звонка будильника. Также вы чувствуете бодрость, которую никогда не испытывали после пробуждения.
            [1] Встать с кровати немедленно
            [2] Немного полежать и подумать 
            [3] Попытаться заснуть
        """
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


def older_handler(user_id, user_choice):
    # на начальном этапе
    if controller[user_id] == 'older':
        if user_choice == "1":
            controller[user_id] = 'older_1'
            return """
                Вы встали с кровати. Вы осмотрелись. Вы находитесь в белой комнате без окон. Перед вами 2 двери
                [1] войти в первую дверь
                [2] войти во вторую дверь
                [3] осмотреться по-внимательнее
                
            """
        if user_choice == "2":
            controller[user_id] = 'older_2'
            return """
                Вы заметили, что совершенно не чувствуете кровать. Также у вас смутное чувство, что что-то не так
                [1] Встать с кровати
                [2] Продолжить размышлять
            """
        if user_choice == '3':
            # вечный цикл)
            controller[user_id] = 'older'
            return """
                Вы открываете глаза. Вы проснулись, но без звонка будильника. Также вы чувствуете бодрость, которую никогда не испытывали после пробуждения.
                [1] Встать с кровати немедленно
                [2] Немного полежать и подумать 
                [3] Попытаться заснуть
            """

    if controller[user_id] == 'older_1':
        if user_choice == '1':
            controller[user_id] = 'older_1_1'
            return """
                Вы попали коридор, такое же белый как и комната. 
                [1] дойти до конца коридора и открыть противоположную дверь
                [2] вернуться в комнату. 
            """
        if user_choice == '2':
            controller[user_id] = 'older_1_2'
            return """
                Вы попали в просторное помещение, напоминающее Вам лабораторию. На больших столах стоит оборудование, назначение которого вам неведомо, склянки, детали и т.п.
                На другом конце огромная установка, похожая на портал ,привлекла ваше внимание.
                [1] осмотреться
                [2] подойти к установке
                
            """
        if user_choice == '3':
            controller[user_id] = 'older_1_3'
            return """
                На одной из стен вы обнаружили едва-заметные часы с датой. Вас смутил год. 2040.
                [1] идти к правой двери
                [2] идти к левой двери
                [3] подойти к кровати
            """
        return INVALID_CHOICE


    return INVALID_CHOICE


bot.polling()
