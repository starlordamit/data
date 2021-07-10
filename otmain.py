import re
import os
from glob import glob, escape
from subprocess import Popen, PIPE
from time import strftime, strptime, sleep
from contextlib import contextmanager
from telegram import InlineKeyboardButton
import logging
from telegram import InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, MessageHandler, Filters
import telepot
vid=['https://www.youtube.com/watch?v=NPqFtxK1nFA', 'https://www.youtube.com/watch?v=-gh0FYNET4o', 'https://www.youtube.com/watch?v=6vBqTpbbpIY', 'https://www.youtube.com/watch?v=fBzXx2IvvEc', 'https://www.youtube.com/watch?v=Wj0lXQRXiOY', 'https://www.youtube.com/watch?v=-PKo0Pq-JQ8', 'https://www.youtube.com/watch?v=up8EmXRkiFM', 'https://www.youtube.com/watch?v=TTgxUz4OGtE', 'https://www.youtube.com/watch?v=S4_Z-Mpv1EU', 'https://www.youtube.com/watch?v=ZaHIcNSZgXY', 'https://www.youtube.com/watch?v=66i1kLZO-lc', 'https://www.youtube.com/watch?v=4JRX1-1-kJc', 'https://www.youtube.com/watch?v=EiByVHXT_hc', 'https://www.youtube.com/watch?v=_pL1g4mLQUM', 'https://www.youtube.com/watch?v=Q2HXdoLjmM4', 'https://www.youtube.com/watch?v=NwymkRkD2mE', 'https://www.youtube.com/watch?v=8I-QHfG6Ffk', 'https://www.youtube.com/watch?v=O3zocb7ZHkM', 'https://www.youtube.com/watch?v=3UDDXuwmPVc', 'https://www.youtube.com/watch?v=drrawYmxVgo', 'https://www.youtube.com/watch?v=R4Y5Vl-BcOE', 'https://www.youtube.com/watch?v=bMZAIEhCgfY', 'https://www.youtube.com/watch?v=Lt7sJOsZvls', 'https://www.youtube.com/watch?v=PWf1E8kqVZA', 'https://www.youtube.com/watch?v=OS4ZG6eEHp8', 'https://www.youtube.com/watch?v=GenqU32RkAI', 'https://www.youtube.com/watch?v=Ej_lee7riBM', 'https://www.youtube.com/watch?v=DPnwWJ31qNM', 'https://www.youtube.com/watch?v=jAgjYBfRQs0', 'https://www.youtube.com/watch?v=ei90-5ezNTk', 'https://www.youtube.com/watch?v=7F9QmFVeKD8', 'https://www.youtube.com/watch?v=CCDXLStOWtk', 'https://www.youtube.com/watch?v=qkN1ktD-hRM', 'https://www.youtube.com/watch?v=zPkKiMo5ZfQ', 'https://www.youtube.com/watch?v=5P4BJi95uuU', 'https://www.youtube.com/watch?v=rEpOKZeqo0c', 'https://www.youtube.com/watch?v=4m7jKNNyI_8', 'https://www.youtube.com/watch?v=hSDFinrGYVU', 'https://www.youtube.com/watch?v=QBC2isMalYY', 'https://www.youtube.com/watch?v=n4XOVlBrDLc', 'https://www.youtube.com/watch?v=ltmKxmUyZBg', 'https://www.youtube.com/watch?v=V1IMVocd65I', 'https://www.youtube.com/watch?v=ePNPJuFEJ7k', 'https://www.youtube.com/watch?v=zObqBR82ocA', 'https://www.youtube.com/watch?v=kUFtaSyQR6c', 'https://www.youtube.com/watch?v=PpcYEd0JpyM', 'https://www.youtube.com/watch?v=YhGxbrsu8PE', 'https://www.youtube.com/watch?v=uaegLGOHyJY', 'https://www.youtube.com/watch?v=-31K92bxJnw', 'https://www.youtube.com/watch?v=WBAU5pqODGw', 'https://www.youtube.com/watch?v=cXUaH5ataj4', 'https://www.youtube.com/watch?v=YV7Pm4mSIN8', 'https://www.youtube.com/watch?v=YRuC1PhiSZ8', 'https://www.youtube.com/watch?v=ZdlCnr5jkJE', 'https://www.youtube.com/watch?v=uvaGQVh4lXg', 'https://www.youtube.com/watch?v=95G9-kdHw6I', 'https://www.youtube.com/watch?v=pRrlBTQrWEE', 'https://www.youtube.com/watch?v=YOs7QMNX7s8', 'https://www.youtube.com/watch?v=Q5gloSE8eW4', 'https://www.youtube.com/watch?v=fNKCI7Pnu94', 'https://www.youtube.com/watch?v=LfcrAgY25jM', 'https://www.youtube.com/watch?v=vkrquiHOEeg', 'https://www.youtube.com/watch?v=xeqRz7Syizs', 'https://www.youtube.com/watch?v=_n6pjA5aFQ4', 'https://www.youtube.com/watch?v=2PFnPzi9kws', 'https://www.youtube.com/watch?v=UFLgrC-hZl0', 'https://www.youtube.com/watch?v=iny4GenrNkk', 'https://www.youtube.com/watch?v=m1NOb2RSvMs', 'https://www.youtube.com/watch?v=LlulKIWFlvw', 'https://www.youtube.com/watch?v=Xs5os29NhTs', 'https://www.youtube.com/watch?v=JOBg9lIluW4', 'https://www.youtube.com/watch?v=MB1lMSYrHdY', 'https://www.youtube.com/watch?v=HKeft1mGUXw', 'https://www.youtube.com/watch?v=QsxymWG26S0', 'https://www.youtube.com/watch?v=4EIDsNUl4dk', 'https://www.youtube.com/watch?v=_IQQTWIRdJs', 'https://www.youtube.com/watch?v=KVrZu9kt3qw', 'https://www.youtube.com/watch?v=06pyHUP7sSs', 'https://www.youtube.com/watch?v=SDvlzD9_3Ck', 'https://www.youtube.com/watch?v=bfylXs4L-a0', 'https://www.youtube.com/watch?v=f_lgPOH5nOk', 'https://www.youtube.com/watch?v=HYPvJKihhX8', 'https://www.youtube.com/watch?v=aPt5D6NcQB4', 'https://www.youtube.com/watch?v=jxGm2R0zD7s', 'https://www.youtube.com/watch?v=7ozXEc2NmPE', 'https://www.youtube.com/watch?v=YGyQgNldRoU', 'https://www.youtube.com/watch?v=WbRD-trxPNI', 'https://www.youtube.com/watch?v=7MxXhPaDAMg', 'https://www.youtube.com/watch?v=UgSFpEndLnc', 'https://www.youtube.com/watch?v=WCvqN51E0f0', 'https://www.youtube.com/watch?v=it-PM93ihTc', 'https://www.youtube.com/watch?v=Gk6YBGl0mmg', 'https://www.youtube.com/watch?v=pdCMxreTK1s', 'https://www.youtube.com/watch?v=PC57cNMyKTc', 'https://www.youtube.com/watch?v=mKg6IBlIGdY', 'https://www.youtube.com/watch?v=9YlJCz_aZFg', 'https://www.youtube.com/watch?v=A4enHz-ExsE', 'https://www.youtube.com/watch?v=n_8qAfTqJ8U', 'https://www.youtube.com/watch?v=W9rKdg0VUT4', 'https://www.youtube.com/watch?v=UXIb9BieA80', 'https://www.youtube.com/watch?v=1l3M3xWSH5U', 'https://www.youtube.com/watch?v=uOHsyBycJko', 'https://www.youtube.com/watch?v=67apyJAfPTQ', 'https://www.youtube.com/watch?v=O5otExIW9xE', 'https://www.youtube.com/watch?v=VaOdtzdp72k', 'https://www.youtube.com/watch?v=0ac-631SIdQ', 'https://www.youtube.com/watch?v=0YnFbW7Oaac', 'https://www.youtube.com/watch?v=rCpXr2nSaoQ', 'https://www.youtube.com/watch?v=5OnnTzTdtew', 'https://www.youtube.com/watch?v=AhELSLi_aNM', 'https://www.youtube.com/watch?v=d7bfDUrIFPw', 'https://www.youtube.com/watch?v=e6v_SpPzdUE', 'https://www.youtube.com/watch?v=OpVb3m-e9JM', 'https://www.youtube.com/watch?v=ety62-Lp2Z8', 'https://www.youtube.com/watch?v=npCjhuxoqUE', 'https://www.youtube.com/watch?v=ErnGuG8HVFk', 'https://www.youtube.com/watch?v=TFDyjkJWi_E', 'https://www.youtube.com/watch?v=0NcDAIq8Spo', 'https://www.youtube.com/watch?v=tmdEyEmthYA', 'https://www.youtube.com/watch?v=o3dSfzvMEAQ', 'https://www.youtube.com/watch?v=NB-fNw1QaZ4', 'https://www.youtube.com/watch?v=SwtoJKKpaU4', 'https://www.youtube.com/watch?v=vq9jNap5Gu0', 'https://www.youtube.com/watch?v=3PVV3VIcChA', 'https://www.youtube.com/watch?v=wgonC6xNLuk', 'https://www.youtube.com/watch?v=cls5FujvW34', 'https://www.youtube.com/watch?v=2tstLDiQiIU', 'https://www.youtube.com/watch?v=wVKoKHI6xlw', 'https://www.youtube.com/watch?v=Dg_oA5ZWy4A', 'https://www.youtube.com/watch?v=6xupvus1vQQ', 'https://www.youtube.com/watch?v=wc5miYdGce4', 'https://www.youtube.com/watch?v=IveIR1HpK5k', 'https://www.youtube.com/watch?v=dGpyVZLXdTY', 'https://www.youtube.com/watch?v=lRqZGxhXz2M', 'https://www.youtube.com/watch?v=LrvXiJyCWKA', 'https://www.youtube.com/watch?v=zKCcglCO9Tk', 'https://www.youtube.com/watch?v=1Amze_D20Io', 'https://www.youtube.com/watch?v=dq1gMoZdazE', 'https://www.youtube.com/watch?v=EZ2G6oBUlfM', 'https://www.youtube.com/watch?v=j1XAptAU6Fo', 'https://www.youtube.com/watch?v=brOZkM26QLQ', 'https://www.youtube.com/watch?v=KyQwdA7FhEY', 'https://www.youtube.com/watch?v=sTlTGugpX-s', 'https://www.youtube.com/watch?v=Z816F9gkSIU', 'https://www.youtube.com/watch?v=a_fpY6ADncU', 'https://www.youtube.com/watch?v=wABb-gUhBKE', 'https://www.youtube.com/watch?v=f1WlyETkL1I', 'https://www.youtube.com/watch?v=i5RVOeNWJNc', 'https://www.youtube.com/watch?v=LcSJVbLEpp8', 'https://www.youtube.com/watch?v=wxcom0uirPQ', 'https://www.youtube.com/watch?v=9HJbV8hM2HI', 'https://www.youtube.com/watch?v=sHNiEVPrDf4', 'https://www.youtube.com/watch?v=nJshMBph9k0', 'https://www.youtube.com/watch?v=_brIOL4ygBo', 'https://www.youtube.com/watch?v=o4Brptbv310', 'https://www.youtube.com/watch?v=vXFcqk7EJOs', 'https://www.youtube.com/watch?v=zdFeU6S2kBU', 'https://www.youtube.com/watch?v=Y1HVT__2kZA', 'https://www.youtube.com/watch?v=zZeHC6lA0zE', 'https://www.youtube.com/watch?v=842EG49_Qug', 'https://www.youtube.com/watch?v=XJ8OeFI9TQU', 'https://www.youtube.com/watch?v=eRwy-23w4ZM', 'https://www.youtube.com/watch?v=gLMTUCaUSd0', 'https://www.youtube.com/watch?v=cyd2395ux1I', 'https://www.youtube.com/watch?v=5yp4bETMPEw', 'https://www.youtube.com/watch?v=vMF-QIs-IbM', 'https://www.youtube.com/watch?v=yAMFQ7JyFd4', 'https://www.youtube.com/watch?v=o9RLV8gjugw', 'https://www.youtube.com/watch?v=pW7_i1vpwa0', 'https://www.youtube.com/watch?v=Bm2ZI1ZQEI4', 'https://www.youtube.com/watch?v=6dqE3sdDPyo', 'https://www.youtube.com/watch?v=qyUUnxXd_Kg', 'https://www.youtube.com/watch?v=Ork74WaVf7k', 'https://www.youtube.com/watch?v=r6F117vbhOY', 'https://www.youtube.com/watch?v=AvASZsUIcaU']

class Video:
    def __init__(self, link, init_keyboard=False):
        self.link = link
        self.file_name = None
        
        if init_keyboard:
            self.formats = self.get_formats()
            self.keyboard = self.generate_keyboard()

    def get_formats(self):
        formats = []

        cmd = "youtube-dl -F {}".format(self.link)
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE).communicate()
        it = iter(str(p[0], 'utf-8').split('\n')) # iterator of output lines

        try:
            while "code  extension" not in next(it): pass # Remove garbage lines
        except StopIteration:
            raise BadLink # Isn't a valid youtube link

        while True:
            try:
                line = next(it)
                if not line:
                    raise StopIteration # Usually the last line is empty
                if "video only" in line:
                    continue # I don't need video without audio
            except StopIteration:
                break
            else:
                format_code, extension, resolution, *_ = line.strip().split()
                formats.append([format_code, extension, resolution])
        return formats

    def generate_keyboard(self):
        """ Generate a list of InlineKeyboardButton of resolutions """
        kb = []

        for code, extension, resolution in self.formats:
            kb.append([InlineKeyboardButton("{0}, {1}".format(extension, resolution),
                                     callback_data="{} {}".format(code, self.link))]) # maybe callback_data can support a list or tuple?
        return kb

    def download(self):
        cmd = "youtube-dl -f best {}".format(self.link)
        print('cmd')
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE).communicate()
        print('work')
        for line in str(p[0], 'utf-8').split('\n'):
            if "[download] Destination:" in line:
                self.file_name = line[24:] # name of the file

    def check_dimension(self):
        if os.path.getsize(self.file_name) > 50 * 1024 * 1023:
            os.system('split -b 49M "{0}" "{1}"'.format(self.file_name, self.file_name))
            os.remove(self.file_name)
        return glob(escape(self.file_name) + '*')

    @contextmanager
    def send(self):
        files = self.check_dimension() # split if size >= 50MB
        yield files
        for f in files: #removing old files
            os.remove(f)
def main(ids):
    for i in vid:
            print('1')
            video = Video(i)
            a=bot.sendMessage(ids,'Added.. '+i)
            c=telepot.message_identifier(a)
            video.download()
            
            with video.send() as files:
                l=1
                for f in files:
                    bot.editMessageText(c,str(l)+' out of'+str(len(files)))
                    l+=1
                    bot.sendDocument(chat_id=ids, document=open(f, 'rb'))

def handle(msg):
    chat_id = msg['chat']['id']
    try:
        text =  msg['text']
    except:
        text = ''
    sender = msg['from']['id']
    msgid=['message_id']
    main(chat_id)
token='1889379061:AAHPX8zP1QwvswZI8qVulXNkLZmOsRrwfks'
import time
bot = telepot.Bot(token)
bot.message_loop(handle)
while 1:
    time.sleep(10)

#updater = Updater(')

#updater.dispatcher.add_handler(MessageHandler(Filters.text, main))
#updater.dispatcher.add_handler(CallbackQueryHandler(download_choosen_format))


#updater.start_polling()
#updater.idle()
