import requests
from bs4 import BeautifulSoup
import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request as req
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

토큰 = "1835518048:AAFzzz7WNfrdGD1bG8sHdl5sE4fltlK3LUE"
id = "1895249171"
bot = telegram.Bot(token=토큰)
updater = Updater(token=토큰, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def campus_crawling():
        
    url = "https://www.gachon.ac.kr/community/opencampus/03.jsp?boardType_seq=358"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")

    ranks = soup.select("table > tbody > tr")
    for row in ranks :
        columns = row.find_all("td")
        # tr 태그 안에 td 가 하나 이하인 데이터는 skip
        if len(columns) <= 1 :
            continue

        link = 'https://www.gachon.ac.kr/community/opencampus/'
        
        post_num = columns[0].get_text().strip()
        title = columns[1].get_text().strip()
        link += columns[1].find('a').attrs['href']



    #id 알아보기
    # for i in 봇.getUpdates():
    #     print(i.message)

        if(post_num == '') :
            text = '<가천대 게시글 업데이트>' + '\n'
            text += "공지" + '\n'
            text += title + '\n'
            text += link

            bot.sendMessage(chat_id=id, text=text)

            continue
        
        text = '<가천대 게시글 업데이트>' + '\n'
        text += post_num + '\n'
        text += title + '\n'
        text += link

        bot.sendMessage(chat_id=id, text=text)

def computer_crawling():
    url = "https://www.gachon.ac.kr/major/bbs.jsp?boardType_seq=159"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

# table -> tbody -> tr -> td 순서대로 긁음
    data_rows = soup.find("table").find("tbody").find_all("tr")

    for row in data_rows :
        columns = row.find_all("td")
    # tr 태그 안에 td 가 하나 이하인 데이터는 skip
        if len(columns) <= 1 :
            continue

        link = 'https://www.gachon.ac.kr/major/'
    
        post_num = columns[0].get_text().strip()
        title = columns[1].get_text().strip()
        link += columns[1].find('a').attrs['href']

    # 만약 post_num 이 빈 문자열이면 뛰어넘기(image 파일)
        if(post_num == '') :
            text = '<가천대 게시글 업데이트>' + '\n'
            text += "공지" + '\n'
            text += title + '\n'
            text += link

            bot.sendMessage(chat_id=id, text=text)
            continue
        
        text = '<가천대 게시글 업데이트>' + '\n'
        text += post_num + '\n'
        text += title + '\n'
        text += link

        bot.sendMessage(chat_id=id, text=text)
# bot.send_message(1895249171,title+finallink)
# titles = soup.select('.boardlist>tbody>tr>td')



info_message = '''- 학교 공지사항 : "학교" or "ㅎㄱ" 입력
- 컴공 공지사항 : "컴공" or "ㅋㄱ" 입력'''
bot.sendMessage(chat_id=id, text=info_message)


def handler(update, context):
    user_text = update.message.text 
    if (user_text == "학교") or (user_text == "ㅎㄱ"):
        campus_crawling()
        bot.sendMessage(chat_id=id, text=info_message)
        
    elif (user_text == "컴공") or (user_text == "ㅋㄱ"):
        computer_crawling()
        bot.sendMessage(chat_id=id, text=info_message)
        
    else:
         bot.send_message(chat_id=id, text="다시 입력해주세요")
         bot.sendMessage(chat_id=id, text=info_message)

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
