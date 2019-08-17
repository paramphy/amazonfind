import requests
from bs4 import BeautifulSoup
import smtplib
import time
import locale

link = 'https://www.amazon.in/Philips-Trimmer-Cordless-QT4001-15/dp/B00L8PEEAI/ref=lp_16269137031_1_1?s=hpc&ie=UTF8&qid=1566023806&sr=1-1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
#print(soup.prettify())

def check_price():
    def get_title(s,url):
        s.headers['User-Agent'] = 'Mozilla/5.0'
        response = s.get(url)
        soup = BeautifulSoup(response.text,"html.parser")
        return soup.find_all(id="productTitle")

    if __name__ == '__main__':    
        with requests.Session() as s:
            for title in get_title(s,link):
                print(title.text.strip())


    def get_price(s,url):
        s.headers['User-Agent'] = 'Mozilla/5.0'
        response = s.get(url)
        soup = BeautifulSoup(response.text,"html.parser")
        return soup.find_all(id="priceblock_ourprice")
    

    if __name__ == '__main__':    
        with requests.Session() as s:
            for price in get_price(s,link):
                print(f'{price.text}\n')
                locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
                converted_price = locale.atof(price.text[2:12])
                print(converted_price)

    #def get_shipping(s,url):
        #s.headers['User-Agent'] = 'Mozilla/5.0'
        #response = s.get(url)
        #soup = BeautifulSoup(response.text,"html.parser")
        #return soup.find_all(id="ourprice_shippingmessage")
    

    #if __name__ == '__main__':    
        #with requests.Session() as s:
            #for shipping in get_shipping(s,link):
                #print(f'{shipping.text.strip()}\n')
                #converted_shipping = float(shipping.text[100])
                #print(converted_shipping)

    if(converted_price < 1000):
        send_mail()     

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('parameshchandra28@gmail.com', 'bjolwoworupketvl')

    subject = 'Price is under 1000'
    body = 'https://www.amazon.in/Philips-Trimmer-Cordless-QT4001-15/dp/B00L8PEEAI/ref=lp_16269137031_1_1?s=hpc&ie=UTF8&qid=1566023806&sr=1-1'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'parameshchandra28@gmail.com',
        'parameshchandra.rs@visva-bharati.ac.in',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()


while(True):
    check_price()
    time.sleep(60*60*24)
        
