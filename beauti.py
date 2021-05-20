import requests
from bs4 import BeautifulSoup


url = "https://www.gachon.ac.kr/community/opencampus/03.jsp?boardType_seq=358"
headers={"User-Agent":"Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 (Gecko와 같은 KHTML) Chrome / 90.0.4430.212 Safari / 537.36"}
res = requests.get(url, headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# rank = soup.find("tbody")
ranks = soup.find_all("td", attrs = {"class":"tl"})
# print(rank.get_text())
# title = ranks[0].a.get_text()
# link = ranks[0].a["href"]
# print(title)
# print("https://www.gachon.ac.kr/community/opencampus/03.jsp?boardType_seq=358"+link)
for rank in ranks:
    title = rank.a.get_text()
    link = rank.a["href"]
    # print(title)
    # print("https://www.gachon.ac.kr/community/opencampus/03.jsp?boardType_seq=358"+link)


import telegram
토큰 = "1835518048:AAFzzz7WNfrdGD1bG8sHdl5sE4fltlK3LUE"
봇 = telegram.Bot(token=토큰)

#id 알아보기
# for i in 봇.getUpdates():
#     print(i.message)

봇.send_message(1895249171,title)    