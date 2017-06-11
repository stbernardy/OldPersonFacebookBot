import praw 
import config
import random
from time import sleep

#This method generates these three lines of broken-ness
def shittyBot():
   shittBot = [
   "Wow, it was nice meeting you Jan",
   "WARNING: I PLAN TO BLOCK EVERYONE ON FACEBOOK THAT DOESNT USE THE ENGLISH LANGUAGE.",
   "Love you, that's it, send it siri.",
   "Thanks you BABBY",
   "THIS IS URE GRANDMA SPEAKING",
   "THIS IS NOT FOR KIDS, INNAPROPRIATE",
   "Looking great dear, your mom has been hospitalized it is not good your grandman",
   ]

#Bot OAuth  
def bot():
    print("Logging in...")
    r = praw.Reddit(username = config.username,
        password = config.password,
        client_id = config.client_id,
        client_secret = config.client_secret,
        user_agent = "Cody's shitty bot commentor v0.2")
    print("Logged in!")

    return r
#The actual bot itself
def running_bot(r):
    print("Gathering the past 25 posts...")
    for comment in r.subreddit('oldpeoplefacebook').comments(limit=25):
        if "insert comment here" in comment.body:
            print("String with \"#insert comment here\" found in comment ") + comment.id
            comment.reply = shittyBot.random()
            print("Replied to comment") + comment.id
#Keeps the bot running ALL FUCKIN DAY LONG       
r = bot()
while True:
    running_bot(r)
