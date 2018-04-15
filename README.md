## 9GAG Bot
It's a telegram bot that can send you random posts and hottest posts(1000+ upvotes) from the section 'Hot'.

**Note.** This bot receive incoming updates using long polling.
### Installation
Download project:

    $ git clone https://github.com/Senigor/telegag.git

Then create virtual environment for **Python 3**, *commands may vary with your linux distribution*:

    $ virtualenv myenv
    $ source myenv/bin/activate

Now install required python packages:
	
	(myenv) $ pip3 install feedparser telepot

Create your bot using @BotFather and paste the token.