import vk_api
import requests
from tokenVk import token
from time import sleep
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
############################ переменные ############################################
day = 'БАГБАГБАГБАГБАГБАГБАГБАГ'
botid = ''
bot = ''
bot_ids = []
botid_list = []

sch = '1. \n' \
      '2. \n' \
      '3. \n' \
      '4. \n' \
      '5. \n' \
      '6. \n' \
      '7. \n' \
      '8. \n' \
      '9. '

status_sch = ['clear']


############################ функции ############################################
def fill_sch(peer_id, sch_list, status_sch, user_id, text):
    print(peer_id, sch_list, status_sch, user_id, text)
    vk.messages.send(
        peer_id=peer_id,
        random_id=get_random_id(),
        message=f'❗️ Смена расписания дня {day} ❗️\n\n'
                'Следуйте шагам из следующих сообщений')

    vk.messages.send(
        peer_id=peer_id,
        random_id=get_random_id(),
        message='♦️ 1 шаг ♦️\n'
                'Введите кол-во уроков (1-9)')
    if user_id > 0:
        if text.isdigit:
            for _ in range(len(sch_list) - int(text)):
                sch_list.remove(sch_list[-1])
        elif text[0] != '!':
            vk.messages.send(
                peer_id=peer_id,
                random_id=get_random_id(),
                message='‼️‼️ Введите верную цифру ‼️‼️')

    vk.messages.send(
        peer_id=peer_id,
        random_id=get_random_id(),
        message='♦️ 2 шаг ♦️\n'
                'Введите расписание по образцу:\n'
                '1. Русский язык - \n'
                '3. Алгебра - \n'
                '\n‼️ Введенный вами текст будет вставлен в расписание с точностью до символа, поэтому прошу соблюдать образец'
                '\n‼️ В образце после дефиса стоит пробел')

    while True:
        if user_id > 0:
            if text[0].isdigit:
                user_sch = text.split('\n')
                for i in user_sch:
                    print(i[0])
                    sch_list[int(i[0]) - 1] = i
            break

    user_sch = '\n'.join(sch_list)

    vk.messages.send(
        peer_id=peer_id,
        random_id=get_random_id(),
        message='♦️ 3 шаг ♦️\n'
                'Проверьте введенное вами расписание:\n'
                f'{user_sch}\n'
                '\nЕсли вы хотите подтвердить ваш ввод, то напишите "готово"\n'
                'Если вы хотите изменить ваш ввод, то напишите "изменить"')

    while True:
        if user_id > 0:
            if text.lower() == 'изменить':
                if text[0].isdigit:
                    user_sch = text.split('\n')
                    for i in user_sch:
                        print(i[0])
                        sch_list[int(i[0]) - 1] = i
                break
            elif text.lower() == 'готово':
                break
            else:
                vk.messages.send(
                    peer_id=peer_id,
                    random_id=get_random_id(),
                    message='‼️‼️ Введите "готово" или "изменить" ‼️‼️')

    vk.messages.send(
        peer_id=peer_id,
        random_id=get_random_id(),
        message='Вы успешно изменили расписание ✅')
    status_sch[0] = 'filled'


######################### вывод расписания #########################################
def sch_output(peer_id, user_sch, user_id, text, sch_list):
    vk.messages.send(
        peer_id=peer_id,
        random_id=get_random_id(),
        message=f'{user_sch}'
                '\nВы можете изменить расписание, введя "изменить"')
    if user_id > 0:
        if text.lower() == 'изменить':
            vk.messages.send(
                peer_id=peer_id,
                random_id=get_random_id(),
                message='♦️ 2 шаг ♦️\n'
                        'Введите расписание по образцу:\n'
                        '1. Русский язык - \n'
                        '3. Алгебра - \n'
                        '\n‼️ Введенный вами текст будет вставлен в расписание с точностью до символа, поэтому прошу соблюдать образец'
                        '\n‼️ В образце после дефиса стоит пробел')

            while True:
                messages = vk.messages.getConversations(offset=0, count=20, filter='important')
                text = messages['items'][0]['last_message']['text']
                user_id = messages['items'][0]['last_message']['from_id']
                if user_id > 0:
                    if text[0].isdigit:
                        user_sch = text.split('\n')
                        for i in user_sch:
                            print(i[0])
                            sch_list[int(i[0]) - 1] = i


##################################################################################################################
def main():
    global day, botid, bot, bot_ids, botid_list, status_sch
    longpoll = VkBotLongPoll(vk_session, '209862435')
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                text = event.message.text
                user_id = event.message.from_id
                peer_id = event.message.peer_id
                if len(bot_ids) > 0:
                    botid = bot + str(bot_ids[-1]) + '\n'
                    botid_list = botid.split('\n')

                if not (peer_id in bot_ids):
                    bot_ids.append(peer_id)
                    if not (botid in botid_list):
                        vk.messages.send(peer_id=peer_id,
                                         random_id=get_random_id(),
                                         message='👉👌 БОТ ОПУЩЕН 🔞\n'
                                                 '================\n'
                                                 '▶ введите !команды')

                if text.lower() == '!команды' or text.lower() == '! команды':
                    vk.messages.send(peer_id=peer_id,
                                     random_id=get_random_id(),
                                     message='🔩 Список команд:\n'
                                             '▶ !команды\n вызов данного списка\n\n'
                                             '▶ !дз [#]\n вызов дз на [определенный день]\n# - [пн, вт, ср, чт, пт]')

                if text.lower() == '!тест' or text.lower() == '!т':
                    vk.messages.send(peer_id=peer_id,
                                     random_id=get_random_id(),
                                     message='🤠 @allllllllllllk (ЭЙ ТЫ) 🤠')

                if text.lower() in ['!дз пн', '!дз вт', '!дз ср', '!дз чт', '!дз пт',
                                    '!дз 1', '!дз 2', '!дз 3', '!дз 4', '!дз 5']:
                    if text.lower()[0] + text.lower()[1] + text.lower()[2] == '!дз' or text.lower()[0] + \
                            text.lower()[1] + text.lower()[2] + text.lower()[3] == '! дз':
                        sch_list = sch.split('\n')
                        if ((text.lower()[-2] + text.lower()[-1]) == 'пн') or text.lower()[-1] == '1':
                            day = 'Понедельник'
                            status_sch.append('mon')
                            if status_sch[0] == 'clear':
                                fill_sch(peer_id, sch_list, status_sch, user_id, text)
                            if status_sch[0] == 'filled':
                                sch_output(peer_id, user_sch, user_id, text, sch_list)

                        elif ((text.lower()[-2] + text.lower()[-1]) == 'вт') or text.lower()[-1] == '2':
                            day = 'Вторник'

                        elif ((text.lower()[-2] + text.lower()[-1]) == 'ср') or text.lower()[-1] == '3':
                            day = 'Среда'

                        elif ((text.lower()[-2] + text.lower()[-1]) == 'чт') or text.lower()[-1] == '4':
                            day = 'Четверг'

                        elif ((text.lower()[-2] + text.lower()[-1]) == 'пт') or text.lower()[-1] == '5':
                            day = 'Пятница'

    except requests.exceptions.ReadTimeout:
        print("--------------- [ СЕТЕВАЯ ОШИБКА ] ---------------")
        print("Переподключение к серверам...")
        time.sleep(3)


if __name__ == '__main__':
    main()
