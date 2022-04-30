import requests, user_agent, json, flask, random, os, sys, time
import ttbotapi
import threading
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

BOT_TOKEN = "Yp0Zisu4-3V853wb9KZitCv99kjx_jhkX5q7oIrJwN8"
bot = ttbotapi.Bot(access_token=BOT_TOKEN)
server = Flask(__name__)
logger = ttbotapi.logger
logger.setLevel(logging.DEBUG)




            
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://bottelem.herokuapp.com/" + str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
