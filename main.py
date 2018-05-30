import sys
import urllib.request
import time
import feedparser
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    global hottest_count

    if content_type == 'text':

        if msg['text'] == 'Get Random Post':
            response = urllib.request.urlopen('http://9gag.com/random')
            bot.sendMessage(chat_id, 'Here you go!')
            bot.sendMessage(chat_id, response.geturl())

        elif msg['text'] == 'Get Hottest Posts':
            posts_rss = feedparser.parse('http://www.9gag-rss-feed.ovh/rss/9GAG_-_Hot.atom')

            if hottest_count >= len(posts_rss.entries):
                hottest_count = 0

            for post in posts_rss.entries[hottest_count:hottest_count+10]:
                hottest_count += 1
                bot.sendMessage(chat_id, post.link)

        else:
            bot.sendMessage(chat_id, "I don't understand you, I'm not a human, please use the keyboard :(")

    else:
        bot.sendMessage(chat_id, 'You should type something.')

    bot.sendMessage(chat_id, 'What do you want?',
                    reply_markup=ReplyKeyboardMarkup(
                        keyboard=[
                            [KeyboardButton(text="Get Random Post"), KeyboardButton(text="Get Hottest Posts")]
                        ], resize_keyboard=True
                    ))


if __name__ == '__main__':
    hottest_count = 0
    TOKEN = sys.argv[1]  # get token from command-line

    bot = telepot.Bot(TOKEN)
    MessageLoop(bot, handle).run_as_thread()

    while 1:
        time.sleep(10)
