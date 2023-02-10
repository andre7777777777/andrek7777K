import openai
import telebot
#можете изменить api ключ, но можете оставить этот просто вставив токен бота.
openai.api_key = "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"
bot = telebot.TeleBot("5830689003:AAF8jatVvPvfE0VyLVs4NRNBwdl9R5HYPIQ")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Как я могу Вам помочь?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='Расскажи мне о ' + message.text + '?',
        max_tokens=2048,
        n = 1,
        stop=None,
        temperature=0.5,
    )
    bot.reply_to(message, response["choices"][0]["text"])

bot.polling()
