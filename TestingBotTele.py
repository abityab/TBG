#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import sys
import time
import telebot
import pickle


# In[ ]:


with open("TestingAja.pkl", 'rb') as file:  
    Pickled_RF_Model = pickle.load(file)

Pickled_RF_Model


# In[ ]:


botToken = ''
bot = telebot.TeleBot(botToken)


# In[ ]:


@bot.message_handler(commands=['help'])
def help_message(message):
    pesan = 'Separator menggunakan koma'
    bot.reply_to(message, pesan)



@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    try:
        if message.chat.type == "group":
            text = message.text
            x = text.split(sep=",")[0]
            y = text.split(sep=",")[1]
            z = text.split(sep=",")[2]

#             time.sleep(1)
            hasil = Pickled_RF_Model.predict([[x,y,z]])
            time.sleep(1)
            if hasil == 0:
                hasil = "A"
            elif hasil == 1:
                hasil = "B"
            elif hasil == 2:
                hasil = "C"
            elif hasil == 3:
                hasil = "D"
            elif hasil == 4:
                hasil = "E"
            elif hasil == 5:
                hasil = "F"
            elif hasil == 6:
                hasil = "G"

            bot.reply_to(message, f'Hasil klasifikasi data\n {x},{y},{z} = {hasil}')

#             bot.reply_to(message, f'nilai x : {x}, nilai y : {y}, nilai z : {z}')
        
    except:
        pesan = 'Separator menggunakan koma'

        bot.reply_to(message, pesan)


# In[ ]:


try:
    print('Running')
    bot.polling(none_stop=True)
except:
    quit()



# In[ ]:


@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    try:
        text = message.text
        x = text.split(sep=",")[0]
        y = text.split(sep=",")[1]
        z = text.split(sep=",")[2]

        hasil = Pickled_RF_Model.predict([[x,y,z]])
        time.sleep(1)
        if hasil == 0:
            hasil = "A"
        elif hasil == 1:
            hasil = "B"
        elif hasil == 2:
            hasil = "C"
        elif hasil == 3:
            hasil = "D"
        elif hasil == 4:
            hasil = "E"
        elif hasil == 5:
            hasil = "F"
        elif hasil == 6:
            hasil = "G"

        bot.reply_to(message, f'Hasil klasifikasi data {x},{y},{z} = {hasil}')

#         bot.reply_to(message.chat.id, f'nilai x : {x}, nilai y : {y}, nilai z : {z}')
        
    except:
        pesan = 'Format salah\n\'

        bot.reply_to(message, pesan)


In[ ]:




