import requests
from bs4 import BeautifulSoup
import cgi
import cgitb
import telebot

token = '6802866842:AAF3jEES_o-ge0G2qCf4WSRsbGrkp5NRWLE'


# # # Календарь игр НХЛ # # #
def hockey():
    r = requests.get('https://www.flashscorekz.com/hockey/usa/nhl/#/jovutXrt/table/overall')
    main_text = r.text
    soup = BeautifulSoup(main_text, "html.parser")
    table = soup.find('span', {'class': 'next_round'})
    return [c.text for c in table]


list_hockey = hockey()

for i in list_hockey:
    if i == ', ':
        list_hockey.remove(i)

new_list_hockey = list_hockey


# # # Календарь игр Примьер лиги АНГЛИИ # # #
def football_angl():
    r = requests.get('https://www.flashscorekz.com/football/england/premier-league/#/I3O5jpB2/table/overall')
    main_text = r.text
    soup = BeautifulSoup(main_text, "html.parser")
    table = soup.find('span', {'class': 'next_round'})
    return [c.text for c in table]


list_football_angl = football_angl()

for i in list_football_angl:
    if i == ', ':
        list_football_angl.remove(i)

new_list_football_angl = list_football_angl


# # # Календарь игр Примеры ИСПАНИИ # # #
def football_isp():
    r = requests.get('https://www.flashscorekz.com/football/spain/laliga/#/SbZJTabs/table/overall')
    main_text = r.text
    soup = BeautifulSoup(main_text, "html.parser")
    table = soup.find('span', {'class': 'next_round'})
    return [c.text for c in table]


list_football_isp = football_isp()
for i in list_football_isp:
    if i == ', ':
        list_football_isp.remove(i)

new_list_football_isp = list_football_isp




# # #  BOT # # #
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['начать'])
def hello(message):
    bot.send_message(message.chat.id, 'Что вас интересует: НХЛ, Примьер лига, Примера?')

@bot.message_handler(content_types=['text'])
def sport(message):
    if message.text.lower() == 'нхл':
        bot.send_message(message.chat.id, '\n'.join(new_list_hockey))
    elif message.text.lower() == 'примьер лига':
        bot.send_message(message.chat.id, '\n'.join(new_list_football_angl))
    elif message.text.lower() == 'примера':
        bot.send_message(message.chat.id, '\n'.join(new_list_football_isp))
    else:
        bot.send_message(message.chat.id, 'нужны выбрать из списка: НХЛ, Примьер лига, Примера')


bot.polling()
