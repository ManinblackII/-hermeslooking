import bs4 as bs
from bs4 import BeautifulSoup
import requests
import re
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import openpyxl
import time



def looking_items():
    item_list_juery = requests.get('https://www.hermes.com/jp/ja/category/jewelry/silver-jewelry/#||カテゴリー')
    soup = BeautifulSoup(item_list_juery.text, 'html.parser')
    elems_total = soup.find("span", class_="total")
    item_list_juery_men = requests.get('https://www.hermes.com/jp/ja/category/men/jewelry-and-fashion-jewelry/#||カテゴリー')
    soup2 = BeautifulSoup(item_list_juery_men.text, 'html.parser')
    elems_total_men = soup2.find("span", class_="total")
    item=elems_total_men.getText()
    item2 = elems_total.getText()
    return item,item2

def create_message(from_addr, to_addr, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = formatdate()
    return msg


def send_mail(from_addr, to_addr, body_msg):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login("u.chihiro@librus.jp", "chihiro19961996")###########自分のグーグルアドレスとパスワードを入力する（低セキュリティ解除必要
    smtpobj.sendmail(from_addr, to_addr, body_msg.as_string())
    smtpobj.close()



item_record = None
item_record2 = None
while True:
    item,item2 = looking_items()
    print(item,item2)

    if (item_record ==item and item_record2==item2) or (item_record == None and item_record2 ==None):
        print('変化なし')
    else:
        my_addr='luluchan743@gmail.com'
        sub_individual='商品が入荷しました'#######タイトルの作成　everyeachnameには自動的に送信者の名前が入力されます
        body_individual='商品が入荷しました'
        everyeach_addr = "luluchan743@gmail.com"
        msg=create_message(my_addr,everyeach_addr,subject=sub_individual,body=body_individual)
        send_mail(my_addr,everyeach_addr,msg)
    time.sleep(900)
    item_record = item
    item_record2 = item2

print('サイトが予期せぬエラーが生じました')
my_addr='luluchan743@gmail.com'
sub_individual='プログラミングが止まりました'#######タイトルの作成　everyeachnameには自動的に送信者の名前が入力されます
body_individual='プログラミングが止まりました'
everyeach_addr = "luluchan743@gmail.com"
msg=create_message(my_addr,everyeach_addr,subject=sub_individual,body=body_individual)
send_mail(my_addr,everyeach_addr,msg)
