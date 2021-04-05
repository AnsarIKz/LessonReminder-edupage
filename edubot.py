from datetime import datetime
from edupage_api import Edupage, EduDate, EduTimetable, EduTime, EduLength
import telebot
import time


allLinks = {
    'Рауан  Жаукенов': 'https://us02web.zoom.us/j/6167704361?pwd=Z2tOUUJLSUFPSTk1QTEvWkVXR2htdz09',
    'Макпал Абдиева': 'https://us04web.zoom.us/j/4209084564?pwd=WURnMW53Q21IcVFqWEhBY2c3bXpUZz09',
    'Ремзия Пелтек': 'https://us04web.zoom.us/j/3191675202?pwd=aytkWkU5N3l1bXd6VU9aNHFNaGtBZz09',
    'Мерует Бекжасарова': 'https://us04web.zoom.us/j/8690240204?pwd=dkdXQ0lzejRaVDlPVHQ1U2pBWHNCQT09',
    'Досжан Алдаберген': 'https://us04web.zoom.us/j/5806683078?pwd=YU1tc3pGNkNnSkNMN3JmVmRQTkhqdz09',
    'Нури Гасанов': 'https://us04web.zoom.us/j/7043389639?pwd=TndhdFprb0NqY0ZqczNwaDRSZ0VIdz09'
}

edupage = Edupage("sdc", "nansarik@mail.ru", "Ansar2003")
edupage.login()
bot = telebot.TeleBot('1724837486:AAHSCeHaZeyxW03Qd5TzEK7XCwgCGNDe53k')

lessonTime = datetime.strptime('0:0', '%H:%M')
lessonDuration = 1800
groupId = -1001163700495


def detectLesson():
    global lessonTime
    if str(timetable.get_lesson_at_time(EduTime(current.hour, current.minute))) == 'None':
        if str(timetable.get_next_lesson_at_time(EduTime(current.hour, current.minute))) == 'None':
            lessonTime = datetime.strptime('0:0', '%H:%M')
            print('Уроков нет')
            time.sleep(7200)
        else:
            lessonTime = datetime.strptime(str(timetable.get_next_lesson_at_time(EduTime(current.hour, current.minute)).length.start), "%H:%M")
    else: 
        print('Урок уже идет!')


def sendReminder():  
    try:
        bot.send_message(groupId, 'Начался урок \n' + timetable.get_lesson_at_time(EduTime.now()).name + '\n' + timetable.get_lesson_at_time(EduTime.now()).teacher + ' \nСсылка - ' + allLinks[timetable.get_lesson_at_time(EduTime.now()).teacher])
    except:
        bot.send_message(groupId, 'Не удалось получить данные об уроке.')
        time.sleep(60)
    detectLesson()
    time.sleep(60)


for hw in edupage.get_homework():
    print(hw)   


while True:
    try:
        timetable = edupage.get_timetable(EduDate.today()) 
        current = datetime.strptime(datetime.now().strftime('%H:%M'),'%H:%M')

        detectLesson()

        if lessonTime == current:
                sendReminder()
                # bot.send_message(-1001163700495, 'Уроков нет, пошел нахуй мразота ебанная')
        time.sleep(20)
    except:
        print('Бисмиллях!')
        print(current)
        print(lessonTime)