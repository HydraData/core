#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
import logging
from pymongo import MongoClient

import TreeWrapper as tw
tw.build_tree("ProfileDataset", "save_money")

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

client = MongoClient()
db = client.hydradata

INCOME, SOCIAL_STATUS, GENDER, CREDIT_EXP, SAVE_MONEY, AGE = range(6)


def start(bot, update):
    if db.profiles.find({"profile_id": update['message']['chat']['id']}).count() == 0:
        db.profiles.insert_one({"profile_id": update['message']['chat']['id']})
        print 'wrote to database'

    update.message.reply_text('Hi, in order to help you I need some basic information')
    update.message.reply_text('What is your monthly income in Kyrgyz soms?')
    return INCOME

def income(bot, update):
    user = update.message.from_user
    db.profiles.update_one({"profile_id": update['message']['chat']['id']},{"$set": {"monthly_income": update.message.text}})
    reply_keyboard = [['Yes', 'No', 'Other']]
    update.message.reply_text('Are you married?',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return SOCIAL_STATUS

def social_status(bot, update):
    user = update.message.from_user
    bool_answer = 1 if update.message.text == "Yes" else 0 #we have yes or no as an answer, so we convert it to bool 1 or 0 respectively
    db.profiles.update_one({"profile_id": update['message']['chat']['id']},{"$set": {"social_status": bool_answer}})
    reply_keyboard = [['Male', 'Female']]
    update.message.reply_text('Are you male or female?',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return GENDER

def gender(bot, update):
    user = update.message.from_user
    bool_answer = 1 if update.message.text == "Male" else 0 #we have Male or Female as an answer, so we convert it to bool 1 or 0 respectively
    db.profiles.update_one({"profile_id": update['message']['chat']['id']},{"$set": {"gender": bool_answer}})
    update.message.reply_text('How old are you?')
    return AGE

def age(bot, update):
    user = update.message.from_user
    db.profiles.update_one({"profile_id": update['message']['chat']['id']},{"$set": {"age": update.message.text}})
    update.message.reply_text('Rate your previous credit experience from 1 to 5 (0 if you have no experience)')
    return CREDIT_EXP

def credit_exp(bot, update):
    user = update.message.from_user
    db.profiles.update_one({"profile_id": update['message']['chat']['id']},{"$set": {"credit_exp": update.message.text}})
    update.message.reply_text('Rate how good you save your money from 1 to 5 (0 if you do not save)')
    return SAVE_MONEY

def save_money(bot, update):
    user = update.message.from_user
    db.profiles.update_one({"profile_id": update['message']['chat']['id']},{"$set": {"save_money": update.message.text}})
    update.message.reply_text('Seems like i can make a desicion already')
    monthly_income = db.profiles.find_one({"profile_id": update['message']['chat']['id']})["monthly_income"]
    social_status = db.profiles.find_one({"profile_id": update['message']['chat']['id']})["social_status"]
    gender = db.profiles.find_one({"profile_id": update['message']['chat']['id']})["gender"]
    age = db.profiles.find_one({"profile_id": update['message']['chat']['id']})["age"]
    credit_exp = db.profiles.find_one({"profile_id": update['message']['chat']['id']})["credit_exp"]
    
    update.message.reply_text("Here is your rating for financial literacy (minimum is 1, maximum is 5)")
    update.message.reply_text(tw.clf.predict([[monthly_income,social_status,gender,age,credit_exp]])[0])
    return ConversationHandler.END

def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation." % user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("286787560:AAG0j11pb5vkSkvmAA9eWRm624V_dQZvJeE")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            INCOME: [MessageHandler(Filters.text, income)],
            SOCIAL_STATUS: [MessageHandler(Filters.text, social_status)],
            GENDER: [MessageHandler(Filters.text, gender)],
            AGE: [MessageHandler(Filters.text, age)],
            CREDIT_EXP: [MessageHandler(Filters.text, credit_exp)],
            SAVE_MONEY: [MessageHandler(Filters.text, save_money)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
