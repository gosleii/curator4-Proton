import telebot

bot = telebot.TeleBot('6550841388:AAEPGy7PsRqPQAwwI7cR5ZQ7bHGAvZRGa14')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Хей-Хей!')


@bot.message_handler(commands=['joke3'])
def main(message):
    bot.send_message(message.chat.id,
                     'Бывает, разговариваешь с человеком, а у него такой взгляд: свет горит, а дома никого нет...')


@bot.message_handler(commands=['joke2'])
def main(message):
    bot.send_message(message.chat.id,
                     'Хорошего бухгалтера найти трудно, поэтому Вера Павловна уже двадцать лет числится в федеральном розыске.')


@bot.message_handler(commands=['joke1'])
def main(message):
    bot.send_message(message.chat.id,
                     'Обезьяна стала человеком, когда взяла в руку палку. И стала чиновником, когда начала совать палки в колёса.')


@bot.message_handler(commands=['joke0'])
def main(message):
    bot.send_message(message.chat.id,
                     'Извилины у человека, как кассы в супермаркетах — несмотря на то, что их создали очень много, не факт, что будут работать все.')


bot.infinity_polling()