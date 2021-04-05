from datetime import datetime
from edupage_api import Edupage, EduDate, EduTimetable, EduTime, EduLength
import telebot
import time

groupId = -1001163700495
edupage = Edupage("sdc", "nansarik@mail.ru", "Ansar2003")
edupage.login()
bot = telebot.TeleBot('1724837486:AAHSCeHaZeyxW03Qd5TzEK7XCwgCGNDe53k')


@bot.message_handler(commands=['hw'])
def hw(message):
    try:
        for hw in edupage.get_homework():
            bot.send_message(groupId, hw)
    except:
        bot.send_message(groupId, 'Не удалось получить данные.')


lessonTime = EduTime(0, 0)

@bot.message_handler(commands=['lesson'])
def nextLesson(message):
    try:
        if str(edupage.get_timetable(EduDate.today()).get_next_lesson_at_time(EduTime.now())) != 'None':
            bot.send_message(groupId, 'Следующий урок \n' + edupage.get_timetable(EduDate.today()).get_next_lesson_at_time(EduTime.now()).name + '\n' + edupage.get_timetable(EduDate.today()).get_next_lesson_at_time(EduTime.now()).teacher)
        else:
            bot.send_message(groupId, 'Следующий урок - ' + edupage.get_timetable(EduDate.tommorrow_this_time()).get_next_lesson_at_time(lessonTime).name + '\nУчитель - ' + edupage.get_timetable(EduDate.tommorrow_this_time()).get_next_lesson_at_time(lessonTime).teacher + '\nДлительность урока ' + str(edupage.get_timetable(EduDate.tommorrow_this_time()).get_next_lesson_at_time(lessonTime).length.start) + ' - ' + str(edupage.get_timetable(EduDate.tommorrow_this_time()).get_next_lesson_at_time(lessonTime).length.end))
    except:
        bot.send_message(groupId, 'Не удалось получить данные.')

        
bot.polling()