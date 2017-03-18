#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import json
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
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

#client = MongoClient('mongodb://hydra:WeilWirLiebenGewalt@127.0.0.1')
#db = client.hydradata

KREDIT, LAUFKONT, LAUFZEIT, DLAUFZEIT, MORAL, VERW, HOEHE, DHOEHE, SPARKONT, BESZEIT, RATE, FAMGES, BUERGE, WOHNZEIT, VERM, ALTER, DALTER, WEITKRED, WOHN, BISHKRED, BERUF, PERS, TELEF, GASTARB = range(24)


def start(bot, update):
    #if db.profiles.find({"profile_id": update['message']['chat']['id']}).count() == 0:
    #    db.profiles.insert_one({"profile_id": update['message']['chat']['id']})
    update.message.reply_text('Hi, I am you personal assistaint. How can I help you?')
    reply_keyboard = [['no balance or debit', '0 <= ... < 200 DM', '... >= 200 DM or checking account for at least 1 year', 'no running account']]
    update.message.reply_text('Balance of current account in DM?',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return LAUFKONT

def laufkont(bot, update):
    answer_result = -1
    if update.message.text == 'no balance or debit':
    elif update.message.text == '... >= 200 DM or checking account for at least 1 year':
    elif update.message.text == 'no running account':
    print(update.message.text)
    update.message.reply_text('Duration in months (metric)')
    return LAUFZEIT

def laufzeit(bot, update):
    answer_result = -1
    answer_result = update.message.text
    print(update.message.text)
    reply_keyboard = [['<=6', '6 < ... <= 12', '12 < ... <= 18', '18 < ... <= 24', '24 < ... <= 30', '30 < ... <= 36','36 < ... <= 42','42 < ... <= 48','48 < ... <= 54','> 54']]
    update.message.reply_text('Duration in months (categorized)',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return DLAUFZEIT

def dlaufzeit(bot, update):
    answer_result = -1
    if update.message.text == '<=6':
    elif update.message.text == '6 < ... <= 12':
    elif update.message.text == '12 < ... <= 18':
    elif update.message.text == '18 < ... <= 24':
    elif update.message.text == '24 < ... <= 30':
    elif update.message.text == '30 < ... <= 36':
    elif update.message.text == '36 < ... <= 42':
    elif update.message.text == '42 < ... <= 48':
    elif update.message.text == '48 < ... <= 54':
    elif update.message.text == '> 54':
    print(update.message.text)
    reply_keyboard = [['no previous credits / paid back all previous credits','paid back previous credits at this bank','no problems with current credits at this bank','hesitant payment of previous credits','problematic running account / there are further credits running but at other banks']]
    update.message.reply_text('Payment of previous credits',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return MORAL

def moral(bot, update):
    answer_result = -1
    if update.message.text =='no previous credits / paid back all previous credits':
    elif update.message.text == 'paid back previous credits at this bank':
    elif update.message.text == 'no problems with current credits at this bank':
    elif update.message.text == 'hesitant payment of previous credits':
    elif update.message.text == 'problematic running account / there are further credits running but at other banks':
    print(update.message.text)
    reply_keyboard = [['new car','used car','items of furniture','radio / television','household appliances','repair','education','vacation','retraining','business','other']]
    update.message.reply_text('Purpose of credit',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return VERW

def verw(bot, update):
    answer_result = -1
    if update.message.text == 'new car':
    elif update.message.text == 'used car':
    elif update.message.text == 'items of furniture':
    elif update.message.text == 'radio / television':
    elif update.message.text == 'household appliances':
    elif update.message.text == 'repair':
    elif update.message.text == 'education':
    elif update.message.text == 'vacation':
    elif update.message.text == 'retraining':
    elif update.message.text == 'business':
    elif update.message.text == 'other':
    print(update.message.text)
    update.message.reply_text('Amount of credit in DM (metric)')
    return HOEHE

def hoehe(bot, update):
    answer_result = -1
    answer_result = update.message.text
    print(update.message.text)
    reply_keyboard = [['<=500','500 < ... <= 1000','1000 < ... <= 1500','1500 < ... <= 2500','2500 < ... <= 5000','5000 < ... <= 7500','7500 < ... <= 10000','10000 < ... <= 15000','15000 < ... <= 20000','> 20000']]
    update.message.reply_text('Amount of credit in DM (categorized)',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return DHOEHE

def dhoehe(bot, update):
    answer_result = -1
    if update.message.text == '<=500':
    elif update.message.text == '500 < ... <= 1000':
    elif update.message.text == '1000 < ... <= 1500':
    elif update.message.text == '1500 < ... <= 2500':
    elif update.message.text == '2500 < ... <= 5000':
    elif update.message.text == '5000 < ... <= 7500':
    elif update.message.text == '7500 < ... <= 10000':
    elif update.message.text == '10000 < ... <= 15000':
    elif update.message.text == '15000 < ... <= 20000':
    elif update.message.text == '> 20000':
    print(update.message.text)
    reply_keyboard = [['< 100,- DM','100,- <= ... < 500,- DM','500,- <= ... < 1000,- DM','>= 1000,- DM','not available / no savings']]
    update.message.reply_text('Value of savings or stocks',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return SPARKONT

def sparkont(bot, update):
    print(update.message.text)
    reply_keyboard = [['unemployed','<= 1 year','1 <= ... < 4 years','4 <= ... < 7 years','>= 7 years']]
    update.message.reply_text('Has been employed by current employer for',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return BESZEIT

def beszeit(bot, update):
    print(update.message.text)
    reply_keyboard = [['>= 35','25 <= ... < 35','20 <= ... < 25','< 20']]
    update.message.reply_text('Instalment in % of available income',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return RATE

def rate(bot, update):
    print(update.message.text)
    reply_keyboard = [['male: divorced / living apart','male: single','male: married / widowed','female: single']]
    update.message.reply_text('Marital Status / Sex',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return FAMGES

def famges(bot, update):
    print(update.message.text)
    reply_keyboard = [['none', 'Co-Applicant','Guarantor']]
    update.message.reply_text('Further debtors / Guarantors',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return BUERGE

def buerge(bot, update):
    print(update.message.text)
    reply_keyboard = [['< 1 year','1 <= ... < 4 years','4 <= ... < 7 years','>= 7 years']]
    update.message.reply_text('Living in current household for',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return WOHNZEIT

def wohnzeit(bot, update):
    print(update.message.text)
    reply_keyboard = [['Ownership of house or land','Savings contract with a building society / Life insurance','Car / Other','not available / no assets']]
    update.message.reply_text('Most valuable available assets',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return VERM

def verm(bot, update):
    print(update.message.text)
    update.message.reply_text('Age in years (metric)')
    return ALTER

def alter(bot, update):
    print(update.message.text)
    reply_keyboard = [['0 <= ... <= 25','26 <= ... <= 39','40 <= ... <= 59','60 <= ... <= 64','>= 65']]
    update.message.reply_text('Age in years (categorized)',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return DALTER

def dalter(bot, update):
    print(update.message.text)
    reply_keyboard = [['at other banks','at department store or mail order house','no further running credits']]
    update.message.reply_text('Further running credits',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return WEITKRED

def weitkred(bot, update):
    print(update.message.text)
    reply_keyboard = [['rented flat','owner-occupied flat','free apartment']]
    update.message.reply_text('Type of apartment',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return WOHN

def wohn(bot, update):
    print(update.message.text)
    reply_keyboard = [['one','two or three','four or five','six or more']]
    update.message.reply_text('Number of previous credits at this bank (including the running one)',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return BISHKRED

def bishkred(bot, update):
    print(update.message.text)
    reply_keyboard = [['unemployed / unskilled with no permanent residence','unskilled with permanent residence','skilled worker / skilled employee / minor civil servant','executive / self-employed / higher civil servant']]
    update.message.reply_text('Occupation',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return BERUF

def beruf(bot, update):
    print(update.message.text)
    reply_keyboard = [['0 to 2','3 and more']]
    update.message.reply_text('Number of persons entitled to maintenance',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return PERS

def pers(bot, update):
    print(update.message.text)
    reply_keyboard = [['no','yes']]
    update.message.reply_text('Telephone?',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return TELEF

def telef(bot, update):
    print(update.message.text)
    reply_keyboard = [['yes','no']]
    update.message.reply_text('Foreign worker?',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return GASTARB

def gastarb(bot, update):
    print(update.message.text)
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
    updater = Updater("273419458:AAG_U_OaO8nAbHQbJtK3cCqzJBFbwm75W3M")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            LAUFKONT: [MessageHandler(Filters.text, laufkont)],
            LAUFZEIT: [MessageHandler(Filters.text, laufzeit)],
            DLAUFZEIT: [MessageHandler(Filters.text, dlaufzeit)],
            MORAL: [MessageHandler(Filters.text, moral)],
            VERW: [MessageHandler(Filters.text, verw)],
            HOEHE: [MessageHandler(Filters.text, hoehe)],
            DHOEHE: [MessageHandler(Filters.text, dhoehe)],
            SPARKONT: [MessageHandler(Filters.text, sparkont)],
            BESZEIT: [MessageHandler(Filters.text, beszeit)],
            RATE: [MessageHandler(Filters.text, rate)],
            FAMGES: [MessageHandler(Filters.text, famges)],
            BUERGE: [MessageHandler(Filters.text, buerge)],
            WOHNZEIT: [MessageHandler(Filters.text, wohnzeit)],
            VERM: [MessageHandler(Filters.text, verm)],
            ALTER: [MessageHandler(Filters.text, alter)],
            DALTER: [MessageHandler(Filters.text, dalter)],
            WEITKRED: [MessageHandler(Filters.text, weitkred)],
            WOHN: [MessageHandler(Filters.text, wohn)],
            BISHKRED: [MessageHandler(Filters.text, bishkred)],
            BERUF: [MessageHandler(Filters.text, beruf)],
            PERS: [MessageHandler(Filters.text, pers)],
            TELEF: [MessageHandler(Filters.text, telef)],
            GASTARB: [MessageHandler(Filters.text, gastarb)]
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
