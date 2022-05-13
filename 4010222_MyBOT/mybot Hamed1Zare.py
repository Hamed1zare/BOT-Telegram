import telebot
import random
import qrcode
from gtts import gTTS



bot = telebot.TeleBot("5273532615:AAH0klPyFE7Z94Rx3ofdkGqyhW3KOyujbNo")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    UserName=message.from_user.first_name
    bot.reply_to(message,f"سلام {UserName } خوش آمدی ")

@bot.message_handler(commands=['game'])
def send_welcome(message):
    bot.reply_to(message,"این مرحله بازی حدس عدد است.. عدد پیشنهادی خودت را وارد کن")
    r=random.randint(0,50)
    @bot.message_handler(func=lambda m:True)
    def echo(message):
        UserName=message.from_user.first_name
        d=int(message.text)
        if r==d:
            bot.reply_to(message,f"باریکلا {UserName} درست حدس زدی ")
        elif r<d:
            bot.reply_to(message," عدد کوچکتر باشه")
        elif r>d:
            bot.reply_to(message," عدد بزرگتر باشه")

@bot.message_handler(commands=['voice'])
def send_Vocal(message):
    UserName=message.from_user.first_name
    bot.reply_to(message,f"سلام {UserName} اینجا متن شما به صدا تبدیل میشود.. به انگلیسی تایپ کن")
    @bot.message_handler(func=lambda m:True)
    def echo(message):
        Vocal =gTTS(message.text)
        Vocal.save('seda.mp3')
        voice=open('seda.mp3','rb')
        bot.send_Vocal(message.chat.id,voice)

@bot.message_handler(commands =['age'])
def send_a(message):
    myname = message.from_user.first_name
    bot.reply_to(message,f"سلام {myname} سال تولد به شمسی؟")
    @bot.message_handler(func= lambda m: True)
    def echo(message):
        Years = int(message.text)
        Now = 1401 - Years
        bot.reply_to(message,f"{myname} تو الان {Now} سالته!")
    
@bot.message_handler(commands =['QRCode'])
def send_QR(message):
    myname = message.from_user.first_name
    bot.reply_to(message,f"کلمه یا متن خود را برای تبدیل به QR وارد کنید")
    @bot.message_handler(func= lambda m: True)
    def echo(message):
        v = message.text
        Image = qrcode.make(v)
        Image.save("some_file.png")
        photo = open('some_file.png', 'rb')
        bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands =['aray'])
def list(message):
    myname = message.from_user.first_name
    list_num = []
    bot.reply_to(message,f"اعدادت را برای ثبت در آرایه وارد کن. عدد بزرگتر مشخص میشود")
    @bot.message_handler(func= lambda m: True)
    def echo(message):
        if message.text != "/OK":
            num_lst =int(message.text)
            list_num.append(num_lst)
            max_lst = max (list_num)
        if message.text != "/OK":      
            bot.reply_to(message,f"اعدادی که گفتی به آرایه اضافه شد. اگر اعدادت تمام شد /End_Aray بزن")
        
        bot.reply_to(message,f"لیست آرایه شما {list_num} :است و بزرگترین عدد آن \n {max_lst} است")



            
bot.infinity_polling()


