# PYTHON ....
# Telegram : @U_OOS
# Codeder : WESTON| HODE
W = "\033[0m"
G = '\033[32;1m'
R = '\033[31;1m'
Y = '\033[33;1m'
B = '\033[34;1m'
P = '\033[35;1m'
B2 = '\033[36;1m'
import os,sys,time
def pr(z):
    for e in z:
     sys.stdout.write(e) 
     sys.stdout.flush() 
     time.sleep(0.006)
clear = lambda : os.system('clear')


clear()


print("\n\n\n\n         - ضع توكن البوت هنا :")
T = input("   "+P+ " → "+W+" T O K E N : ")



#- - - - - - - - - - - - • LIB

def pip(p):
	for i in p:
		os.system(f'pip install {i}')
try:
	import random ,json,logging
	import requests
	import telebot
	import gdolib
	from gdolib import *
	from telebot import types
except:
	pip(['json','random','requests','pyTelegramBotAPI','gdolib','logging'])
	import random,json,logging
	import requests
	import telebot
	import gdolib
	from telebot import types
	from gdolib import *
clear()

#- - - - - - - - - - - - • 


bot = telebot.TeleBot(T)

logging.basicConfig(filename='bot.log', level=logging.INFO)


pr(f"""\n\n\n{W}		-  {R} #    {W}Coder: WESTON {R}   # {W} -  
		-   {R}#  {W}TeLeGraM: U_OOS {R}  # {W} -
		-   {R}#  {W} Version: 2.0      {R} # {W} -\n\n""")
pr("\n\n\n\n  "+P+" \n                [★] "+W+" R U N ...    || تم تشغيل البوت 🟢\n\n")
#- - - - - - - - - - - - • Telecommunications..
class ch_email:

	def state(email):
		if check_email.gmail(email)['status']=='Success':
			return True
		else:
			return False
	
	def reset(em):
		try:
			if gdo_drow.reset(em)['reset'] ==True:
				return True
		except:
			return False
			
#- - - - - - - - - - - - • 
			
	
	





#- - - - - - - - - - - - • k1.. start 
def k1():
	A1 = types.InlineKeyboardButton(f" الدخول للأقسام ",callback_data="run")
	inline = types.InlineKeyboardMarkup(keyboard=[[A1]])
	return inline
#- - - - - - - - - - - - • START ...
@bot.message_handler(commands=['start'])
def start(m):
	id = m.chat.id
	name = m.chat.first_name
	user = f'tg://user?id={id}'
	link_account = f' |  [ ؍{name}؍ ]({user})  | '
	link_ch = f' |  [WESTON 🐍](t.me/U_OOS)  | '
	link_dev_acc = f' |  [WESTON](t.me/U_OOS)  | '
	text = f"""
✦ اهلا بك عزيزي {link_account} في البوت
✦ البوت مقدم WESTON
✦ وضيفة البوت : صيد متاحات جيميل فقط عشوائي ..
 
| المطور : {link_dev_acc}"""
	bot.send_message(id,text,parse_mode='markdown', disable_web_page_preview='true',reply_markup=k1())
#- - - - - - - - - - - - • 





#- - - - - - - - - - - - | •••••• edie message
def edit(done,bad,email,id,id_msg):
	bot.edit_message_text(chat_id=id,message_id=id_msg,text=' جار صيد المتاحات \nانتظر من فضلك ⏳..\n. ',reply_markup=keyboard(done,bad,email),parse_mode='markdown', disable_web_page_preview='true')



#- - - - - - - - - - - - | •••••• keyBoard call•••••
def keyboard(done,bad,email):
	A1 = types.InlineKeyboardButton(f" متاح ✅: {done}",callback_data="iii")
	A2 = types.InlineKeyboardButton(f" غير متاح 🔴: {bad} ",callback_data="iran")
	A3 = types.InlineKeyboardButton(f"{email} ",url ='t.me/U_OOS')
	A4 = types.InlineKeyboardButton("ايقاف",callback_data="stop")
	inline = types.InlineKeyboardMarkup(keyboard=[[A1],[A2],[A3],[A4]])
	return inline

def key1():
	A1 = types.InlineKeyboardButton(f"صيد عن طريق اسماء",callback_data="na")
	A2 = types.InlineKeyboardButton(f"صيد عشوائي",callback_data="random")
	A3 = types.InlineKeyboardButton("رجوع",callback_data="back")
	inline = types.InlineKeyboardMarkup(keyboard=[[A1],[A2],[A3]])
	return inline

	
#- - - - - - - - - - - - • CALL ..
@bot.callback_query_handler(lambda call:True)
def call(call):
  global loop
  loop = True
  
  id = call.from_user.id
  name = call.from_user.first_name
  user = f'tg://user?id={id}'
  link_account = f' |  [ ؍{name}؍ ]({user})  | '
  link_ch = f' |  [ArsThon](t.me/U_OOS)  | '
  link_dev_acc = f' |  [WESTON](t.me/U_OOS)  | ' 
  chat_iid=call.message.chat.id
  message_idd=call.message.message_id
  
  text = f"""
✦ اهلا بك عزيزي {link_account} في البوت
✦ البوت مقدم من WESTON
✦ وضيفة البوت : صيد متاحات جيميل فقط عشوائي ..
 
| المطور : {link_dev_acc}"""




  if call.data == "stop":
  	loop = False
  	bot.delete_message(id,call.message.message_id)
  	bot.send_message(id,text,reply_markup=k1(),parse_mode='markdown', disable_web_page_preview='true')
  
  if call.data == 'back':
  	bot.edit_message_text(chat_id=id,message_id=message_idd,text=text,reply_markup=k1(),parse_mode='markdown', disable_web_page_preview='true')
  	
  if call.data == 'run':
  	bot.edit_message_text(chat_id=chat_iid,message_id=message_idd,text=text,reply_markup=key1(),parse_mode='markdown', disable_web_page_preview='true')
  
  if call.data == "na":
  	z = bot.edit_message_text(chat_id=chat_iid,message_id=message_idd,text="حسناً ، ارسل الان الاسم باللغه الانكليزيه لكي يتم صنع الايميلات عليه ...",parse_mode='markdown', disable_web_page_preview='true')
  	bot.register_next_step_handler(z,nam)
  
  
  if call.data == 'nam':
  	Type = 'nam'
  	n = names
  	done , bad = 0,0
  	while loop:
  		gmail,reset = False,False
  		#if loop == False:
  			#break
  		for na in n.split('\n'):
  			email = rand(na)
  			if ch_email.reset(email) == True:
  				reser=True
  				if ch_email.state(email) == True:
  					 gmail=True
  					 pr(G+f'- Reset | Gmail : {email}\n')
  					 done+=1
  					 bot.send_message(id,text = f'تم صيد جيميل متاح ✅ : `{email}`',parse_mode='markdown', disable_web_page_preview='true')
  					 try:
  					 	edit(done,bad,email,id,call.message.message_id)
  					 except telebot.apihelper.ApiException as e:
  					 	if "Too Many Requests" in str(e):
  					 		sec = str(e).split('Too Many Requests: retry after ')[1]
  					 		text=f"تم تجاوز حد الطلبات المسموح به. سيعود البوت للعمل مرة أخرى بعد {int(sec)} ثانية."
  					 		logging.warning(text)
  					 		time.sleep(int(sec))
  					 		continue
  					 	else:
  					 		continue 
  					 	
	  				 
	  			else:
	  				 		pr(R+f'- No Gmail : {email}\n')
	  				 		bad+=1
	  				 		
	  				 		try:
	  				 			edit(done,bad,email,id,call.message.message_id)
  					 		except telebot.apihelper.ApiException as e:
  					 			if "Too Many Requests" in str(e):
  					 				sec = str(e).split('Too Many Requests: retry after ')[1]
  					 				text=f"تم تجاوز حد الطلبات المسموح به. سيعود البوت للعمل مرة أخرى بعد {int(sec)} ثانية."
  					 				logging.warning(text)
  					 				time.sleep(int(sec))
  					 				continue
  					 			else:
  					 				continue 
  				 	
  			else:
		  		pr(P+f'- No Reset : {email}\n')
		  		bad+=1
		  		try:
  					edit(done,bad,email,id,call.message.message_id)
  				except telebot.apihelper.ApiException as e:
  					 	if "Too Many Requests" in str(e):
  					 		sec = str(e).split('Too Many Requests: retry after ')[1]
  					 		text=f"تم تجاوز حد الطلبات المسموح به. سيعود البوت للعمل مرة أخرى بعد {sec} ثانية."
  					 		logging.warning(text)
  					 		time.sleep(int(sec))
  					 		continue
  					 	else:
  					 		continue 


  if call.data == 'random':
  	Type='random'
  	done , bad = 0,0
  	while loop:
  		#if loop == False:
	  		#break
	  	email = get_user()
	  	if loop:
		  	if ch_email.reset(email) == True:
		  		if ch_email.state(email) == True:
		  			done+=1
		  			pr(G+f'- Reset | gmail : {email}\n')
		  			bot.send_message(id,text = f'تم صيد جيميل متاح  ✅ : `{email}`',parse_mode='markdown', disable_web_page_preview='true')
		  			try:
  					 	edit(done,bad,email,id,call.message.message_id)
  					except telebot.apihelper.ApiException as e:
  					 	if "Too Many Requests" in str(e):
  					 		sec = str(e).split('Too Many Requests: retry after ')[1]
  					 		text=f"تم تجاوز حد الطلبات المسموح به. سيعود البوت للعمل مرة أخرى بعد {int(sec)} ثانية."
  					 		logging.warning(text)
  					 		time.sleep(int(sec))
  					 		continue
  					 	else:
  					 		continue 
		  			
		  			
		  		else:
		  			pr(R+f'- No Gmail : {email} \n')
		  			bad+=1
		  			try:
  					 	edit(done,bad,email,id,call.message.message_id)
  					except telebot.apihelper.ApiException as e:
  					 	if "Too Many Requests" in str(e):
  					 		sec = str(e).split('Too Many Requests: retry after ')[1]
  					 		text=f"تم تجاوز حد الطلبات المسموح به. سيعود البوت للعمل مرة أخرى بعد {int(sec)} ثانية."
  					 		logging.warning(text)
  					 		time.sleep(int(sec))
  					 		continue
  					 	else:
  					 		continue 
		  			
		  	else:
		  		pr(P+f'- No Reset : {email}\n')
		  		bad+=1
		  		try:
  					edit(done,bad,email,id,call.message.message_id)
  				except telebot.apihelper.ApiException as e:
  					 	if "Too Many Requests" in str(e):
  					 		sec = str(e).split('Too Many Requests: retry after ')[1]
  					 		text=f"تم تجاوز حد الطلبات المسموح به. سيعود البوت للعمل مرة أخرى بعد {int(sec)} ثانية."
  					 		logging.warning(text)
  					 		time.sleep(int(sec))
  					 		continue
  					 	else:
  					 		continue 




#- - - - - - - - - - - - - - - - - - - - - - -
def nam(m):
	global names
	names = m.text
	
	A = types.InlineKeyboardButton("بدأ الصيد",callback_data="nam")
	inline = types.InlineKeyboardMarkup(keyboard=[[A]])
	
	bot.send_message(m.chat.id,text = f'this names are add.. : `{names}`',reply_markup=inline,parse_mode='markdown', disable_web_page_preview='true')
	
#- - - - - - - - - - - - • 

	

#- - - - - - - - - - - - • names
def rand(name):
	domin = "@gmail.com"
	rand_num = random.randint(99,9999)
	return name + str(rand_num) + domin
#- - - - - - - - - - - - • 




#- - - - - - - - - - - - • users
try:
	import string
except:
	pip("string") 
	import string
use = string.ascii_lowercase+'0987654321'
use2 = string.ascii_lowercase
def get_user():
	
	u1 = random.choice(use2)
	u2 = random.choice(use)
	user = u1*2+u2+''.join(random.choice(random.choice(random.choice(use+'.'))) for i in range(random.randint(2,4)))+"@gmail.com"
	
	return user if user[0] != '.' and ".." not in user and '.' not in user[-1]  and (user.count('.') < 2) else get_user()
#- - - - - - - - - - - - • 






#- - - - - - - - - - - - • R U N ..

bot.infinity_polling(interval=1, timeout=10)	

	