from instapy import InstaPy
from instapy import smart_run
import random as r
import schedule
import time

username = "akiha8ara"
password = "genjustu111"

def bot():
    session = InstaPy(username=username, password=password, headless_browser=True)
    session.login()

    with smart_run(session):
        session.like_by_tags(["animeedits"], amount=50)
        session.set_do_follow(True, percentage=r.randint(40,60))
        session.set_do_comment(True, percentage=r.randint(10,30))
        session.set_comments(["awesome","wow","nice","Hey New Anime Merch by us","if you ever need anime merch check us out!,""Were a new anime merch store stop by and say hi ^_^","Hello stopping to show your page some love -Akih8ara","hows it going check our our new anime apparel store and tell us what you think","Never been to Akiha8ara we just brought it to you ^_^","looking for new anime merch? give us a chance","come to Akiha8ara please!^_^","Just In!^_^New Anime Apparel!","DUDE!","^_^",])

schedule.every().day.at("18:26").do(bot)
schedule.every().day.at("00:03").do(bot)

while True:
    schedule.run_pending()
    time.sleep(15)