#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import sys
import time
import telebot
import pickle


# In[ ]:


with open("ColoModelRF.pkl", 'rb') as file:  
    Pickled_RF_Model = pickle.load(file)

Pickled_RF_Model


# In[ ]:


botToken = '1817839315:AAE5YdgQ-KChtiMFf46nEi42CmVYCZT50ZI'
bot = telebot.TeleBot(botToken)


# In[ ]:


@bot.message_handler(commands=['help'])
def help_message(message):
    pesan = 'Manual Penggunan Bot Telegram\nKetik nilai RSRP,Lat,Long untuk mendapatkan prediksi COLO\n    contoh :\n    -110.06, -8.68216, 115.197    \n\nNote :\nPemisah nilainya pakai titik ya untuk pemisah antar parameter pakai koma'
    bot.reply_to(message, pesan)


# # Handle All Message Jika Bot ada di group

# In[ ]:


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
                hasil = "Build"
            elif hasil == 1:
                hasil = "H3I DT"
            elif hasil == 2:
                hasil = "ISAT DT"
            elif hasil == 3:
                hasil = "Protel"
            elif hasil == 4:
                hasil = "TSEL DT"
            elif hasil == 5:
                hasil = "XL MR"
            elif hasil == 6:
                hasil = "XL DT"

            bot.reply_to(message, f'Hasil klasifikasi data\n {x},{y},{z} = {hasil}')

#             bot.reply_to(message, f'nilai x : {x}, nilai y : {y}, nilai z : {z}')
        
    except:
        pesan = 'Format Inputan yg anda masukkan Salah\nKetik nilai RSRP,Lat,Long\n        contoh :\n        -110.06, -8.68216, 115.197        \n\nNote :\nPemisah nilainya pakai titik ya untuk pemisah antar parameter pakai koma'

        bot.reply_to(message, pesan)


# In[ ]:


try:
    print('BOT Machine Learning COLO RUNNING')
    bot.polling(none_stop=True)
except:
    quit()


# # Handle Message jika direct ke bot nya

# In[ ]:


# @bot.message_handler(func=lambda message: True)
# def handle_all_message(message):
#     try:
#         text = message.text
#         x = text.split(sep=",")[0]
#         y = text.split(sep=",")[1]
#         z = text.split(sep=",")[2]

#         hasil = Pickled_RF_Model.predict([[x,y,z]])
#         time.sleep(1)
#         if hasil == 0:
#             hasil = "Build"
#         elif hasil == 1:
#             hasil = "H3I DT"
#         elif hasil == 2:
#             hasil = "ISAT DT"
#         elif hasil == 3:
#             hasil = "Protel"
#         elif hasil == 4:
#             hasil = "TSEL DT"
#         elif hasil == 5:
#             hasil = "XL MR"
#         elif hasil == 6:
#             hasil = "XL DT"

#         bot.reply_to(message, f'Hasil klasifikasi data {x},{y},{z} = {hasil}')

# #         bot.reply_to(message.chat.id, f'nilai x : {x}, nilai y : {y}, nilai z : {z}')
        
#     except:
#         pesan = 'Format Inputan yg anda masukkan Salah\nKetik nilai RSRP,Lat,Long\n\
#         contoh :\n\
#         -110.06, -8.68216, 115.197'

#         bot.reply_to(message, pesan)


# In[ ]:




