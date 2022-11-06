import requests
import telebot
from user_agent import generate_user_agent
from telebot import types
import json
import random
import urllib
from threading import Thread

bot = telebot.TeleBot(input("[~] Enter Token : "))

key = "a68df5578398eecd9931c8348d19f7cb"

url = "https://smmcpan.com/api/v2"

headers = {
'Host': 'smmcpan.com',
'Connection': 'keep-alive',
'Content-Length': '794',
'Cache-Control': 'max-age=0',
'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Android"',
'Upgrade-Insecure-Requests': '1',
'Origin': 'https://smmcpan.com',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': generate_user_agent(),
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-User': '?1',
'Sec-Fetch-Dest': 'document',
'Referer': 'https://smmcpan.com/order/7201841',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
'Cookie': '_BEAMER_USER_ID_tHZfxtNs19623=fba01522-724e-44ed-988e-a9dd66d03ad1; _BEAMER_FIRST_VISIT_tHZfxtNs19623=2022-05-31T09:18:26.064Z; _BEAMER_BOOSTED_ANNOUNCEMENT_DATE_tHZfxtNs19623=2022-05-31T09:18:28.083Z; _gid=GA1.2.2138485929.1660317017; _BEAMER_FILTER_BY_URL_tHZfxtNs19623=false; _BEAMER_LAST_PUSH_PROMPT_INTERACTION_tHZfxtNs19623=1660317023813; _identity_user=cd12a3f7cb3c905058a551a9733359f6b79da04c156753d56044a8d2fd0dfdb4a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_identity_user%22%3Bi%3A1%3Bs%3A18%3A%22%5B83548%2C%22%22%2C2592000%5D%22%3B%7D; hash=04dfefc153df17ad4df95817ac60de7b4fb2edcdd7ac24d94858f2e2f95fc663a%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22hash%22%3Bi%3A1%3Bs%3A64%3A%22b9a533242cd3df6d8d08f951484210d2689f8b5b5cbb89da39dac08807a1c27d%22%3B%7D; PHPSESSID=5mj6t2jta9nloljf5jmca5prb6; _csrf=be9c8bae150332e4dd3c0ed1cf81a982870c6685fb7f29fa0535f36da4c93578a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22mC8QfnQ5UtdZfNyDsKwp-STB_3VLnYiQ%22%3B%7D; _ga_071DV2E820=GS1.1.1660317016.2.1.1660317766.0; _ga=GA1.2.103009363.1653988697; _gat_gtag_UA_142022689_1=1'
}

call = types.InlineKeyboardButton(text = "Views Tiktok", callback_data = 's1')
call2 = types.InlineKeyboardButton(text = "Views Twitter", callback_data = 's2')
call3 = types.InlineKeyboardButton(text = "Views Instagram", callback_data = 's3')
call4 = types.InlineKeyboardButton(text = "My Orders", callback_data = 's4')
call5 = types.InlineKeyboardButton(text = "Programmer", url="t.me/VZX_TEAM")

n = 0

@bot.message_handler(commands=["tiktok"])
def orders_tiktok(message):
	id = message.from_user.id
	try:
		with open(f'tiktok-{id}.json','r') as f1:
			data = json.load(f1)
		status = data["orders"][f"{id}"]["status"]
		if status == True:	
			order_tiktok = data["orders"][f"{id}"]["order"]			
			bot.send_message(message.chat.id, text=f"Tiktok Info\nOrder : True\nOrder Number : {order_tiktok}")
	except:
			bot.send_message(message.chat.id, text=f"Tiktok Info\nOrder : False")

@bot.message_handler(commands=["twitter"])
def orders_twitter(message):
	id = message.from_user.id
	try:
		with open(f'twitter-{id}.json','r') as f1:
			data = json.load(f1)
		status = data["orders"][f"{id}"]["status"]
		if status == True:	
			order_twitter = data["orders"][f"{id}"]["order"]			
			bot.send_message(message.chat.id, text=f"Twitter Info\nOrder : True\nOrder Number : {order_twitter}")
	except:
			bot.send_message(message.chat.id, text=f"Twitter Info\nOrder : False")

@bot.message_handler(commands=["instagram"])
def orders_instagram(message):
	id = message.from_user.id
	try:
		with open(f'instagram-{id}.json','r') as f1:
			data = json.load(f1)
		status = data["orders"][f"{id}"]["status"]
		if status == True:	
			order_instagram = data["orders"][f"{id}"]["order"]			
			bot.send_message(message.chat.id, text=f"Instagram Info\nOrder : True\nOrder Number : {order_instagram}")
	except:
			bot.send_message(message.chat.id, text=f"Instagram Info\nOrder : False")	
		
@bot.message_handler(commands=["start"])
def start(message):
	name = message.from_user.first_name
	Keyy = types.InlineKeyboardMarkup()
	Keyy.row_width = 1
	Keyy.add(call,call2,call3,call4,call5)
	bot.send_message(message.chat.id, text=f"Welcome my dear : {name} 😁\nBot increase views of all social media sites 🔥\nChoose one of the buttons below 🤔\nProgrammer: @Mr_Aws | @VZX_TEAM 🙋‍♂",reply_markup=Keyy)

@bot.callback_query_handler(func=lambda m:True)
def nova(call):
	if call.data == 's1':
		txt = bot.send_message(call.message.chat.id,f"Send Link")
		bot.register_next_step_handler(txt,views_tiktok)
	if call.data == 's2':
		txt = bot.send_message(call.message.chat.id,f"Send Link")
		bot.register_next_step_handler(txt,views_twitter)
	if call.data == 's3':
		txt = bot.send_message(call.message.chat.id,f"Send Link")
		bot.register_next_step_handler(txt,views_instagram)
	if call.data == 's4':
		bot.send_message(call.message.chat.id, text="Send /tiktok To View Tiktok Orders\nSend /twitter To View Twitter Orders\nSend /instagram To View Instagram Orders")

def views_tiktok(message):
	link = message.text
	if "tiktok.com" not in link:
		bot.send_message(message.chat.id, text="Please Enter Link")
	else:
		data = {
		"key": key,
		"action": "add",
		"service": "5578",
		"link": link,
		"quantity": "100"
		}
		global n
		n+=100
		try:
			url_ord =requests.post(url,headers =headers,data =data).json()
			order = url_ord["order"]
			id = message.from_user.id
			data = {
			"orders": {
				f"{id}": {
					'status': True,
					'order': order
				}
			}
		}
			with open(f'tiktok-{id}.json', 'w') as f:
				json.dump(data,f)		
			f.close()
			bot.send_message(message.chat.id, text="Done Make Order\nOrder : 100 Views Tiktok\nProgrammer : @Mr_Aws | @VZX_TEAM")
		except:
			bot.send_message(message.chat.id, text="Error Make Order\nOrder : 100 Views Tiktok\nProgrammer : @Mr_Aws | @VZX_TEAM")
		
def views_twitter(message):
	link = message.text
	if "twitter.com" not in link:
		bot.send_message(message.chat.id, text="Please Enter Link")
	else:
		data = {
		"key": key,
		"action": "add",
		"service": "5817",
		"link": link,
		"quantity": "50"
		}
		global n
		n+=50
		try:
			url_ord =requests.post(url,headers =headers,data =data).json()
			order = url_ord["order"]
			id = message.from_user.id
			data = {
			"orders": {
				f"{id}": {
					'status': True,
					'order': order
				}
			}
		}
			with open(f'twitter-{id}.json', 'w') as f:
				json.dump(data,f)		
			f.close()
			bot.send_message(message.chat.id, text="Done Make Order\nOrder : 50 Views Twitter\nProgrammer : @Mr_Aws | @VZX_TEAM")
		except:
			bot.send_message(message.chat.id, text="Error Make Order\nOrder : 50 Views Twitter\nProgrammer : @Mr_Aws | @VZX_TEAM")
		
def views_instagram(message):
	link = message.text
	if "instagram.com" not in link:
		bot.send_message(message.chat.id, text="Please Enter Link")
	else:
		data = {
		"key": key,
		"action": "add",
		"service": "5576",
		"link": link,
		"quantity": "100"
		}
		global n
		n+=100
		try:
			url_ord =requests.post(url,headers =headers,data =data).json()
			order = url_ord["order"]
			id = message.from_user.id
			data = {
			"orders": {
				f"{id}": {
					'status': True,
					'order': order
				}
			}
		}
			with open(f'instagram-{id}.json', 'w') as f:
				json.dump(data,f)		
			f.close()
			bot.send_message(message.chat.id, text="Done Make Order\nOrder : 100 Views Instagram\nProgrammer : @Mr_Aws | @VZX_TEAM")
		except:
			bot.send_message(message.chat.id, text="Error Make Order\nOrder : 100 Views Instagram\nProgrammer : @Mr_Aws | @VZX_TEAM")

def views_telegram(message):
	link = message.text
	if "https://t.me" in link:
			bot.reply_to(message,"Please Wait ...")
			for i in range(10000):
				  try :
				  	time.sleep(float(0.1))
				  	th = Thread(target=send_seen, args=(link.split("/")[3], link.split("/")[4], random.choice(prox_list)))
				  	th.start()
				  except:
		        		pass
				  bot.reply_to(message, "Done Send 10000 Views")
	else:
		bot.send_message(message.chat.id, text="Please Enter Link")
			
bot.infinity_polling()