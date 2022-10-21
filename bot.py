try:
  import telebot
  from requests import *
  from telebot import TeleBot,types
  import time
except:
	import os
	os.system("pip install telebot")
	os.system("pip install time")
	os.system("pip install requests")
token = "5490297673:AAGHTc_3UG5mq0_bF-zKuyN4WuJ9sNvNjkU"
bot = TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text="  •قم بل اشتراك في هاذهي القناة : @deferent_404 •")
    time.sleep(5)
    first = message.from_user.first_name
    bot.send_message(message.chat.id, text="  • SeNd UsEr InstaGram •")
@bot.message_handler(content_types = ['text'])
def basha(m):
 ba = m.text
 try:
  hd = {
'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
'viewport-width':'412',
'x-asbd-id':'198387',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'}
  rr=get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={ba}',headers=hd).json()
  Name = rr['data']['user']['full_name']
  FOLO=rr['data']['user']['edge_followed_by']['count']
  bayo = rr['data']['user']['biography']
  ID = rr['data']['user']['id']
  lok = get(f"https://o7aa.pythonanywhere.com/?id={ID}").json()['date']
  FLO = (rr['data']['user']['edge_follow']['count'])
  tlg =(f"""𝁵 deferent  𝁵
𓏳𓏳𓏳𓏳𓏳𓏳𓏳
𓊒 𝑁𝐴𝑀𝐸 :- {Name}
𓊒 𝑈𝑆𝐸𝑅 :- {ba}
𓊒 𝐹𝑂𝐿𝐿𝑂𝑊𝐸𝑅𝑆 :- {FOLO}
𓊒 𝐹𝑂𝐿𝐿𝑂𝑊𝐼𝑁𝐺 :- {FLO}
𓊒 id : {ID}
𓊒 𝐷𝐴𝑇𝐸 :- {lok}
𓊒 BaYo :- {bayo}
𓊒 𝐿𝐼𝑁𝐾 :- https://www.instagram.com/{ba}
bv : @deferent_404
𓏳𓏳𓏳𓏳𓏳𓏳𓏳 
.""")

  bot.send_message(m.chat.id,tlg)
  bot.send_message(m.chat.id, text="• SeNd UsEr InstaGram •")
 except:
  bot.send_message(m.chat.id, text="  - USER NOT FOUND !\n- TRY ? SEND USER :")

bot.polling()
