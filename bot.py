from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings



logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Вызван /start'
    #print(text)
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    u_m = update.message
    user_text = "Hello {}! You are wrote: {}".format(u_m.chat.first_name, u_m.text)
    logging.info("User: %s, Chat id: %s, Message: %s", u_m.chat.username, u_m.chat.id, u_m.text)
    print(u_m)
    u_m.reply_text(user_text)

def main():
    mybot = Updater(settings.API_KEY, request_kwargs = settings.PROXY, use_context=True)

    logging.info("Bot is starting...")

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start',greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()



main()
