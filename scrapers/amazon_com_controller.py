from websites import content
from session import client
from bs4 import BeautifulSoup
import bot

info = content['amazon.com.controller']
url = info['url']
timeout = info['timeout']

async def run():
    res = client.get(url)
    print(res)
    soup = BeautifulSoup(res.text, 'lxml')
    sub_class=soup.find(id='availability')  #finding that particular div 
    print('amazon.com ps5 controller -> ')
    if sub_class:   #above result can be none so checking if result is not none
        text = sub_class.find("span", {"class": "a-size-medium"}).text.strip()
        print("availability : {}".format(text)) 
        msg = ""
        stock = False
        if (text == 'In Stock.'):
            msg = "HOSTIAAAAA 😲 Que el mando de la PS5 esta en stock! 🔥\n%s\nMensaje: %s" % (url, text)
            stock = True
        elif (text == 'Only 1 left in stock - order soon.'):
            msg = "CORREEEEE 😲 Que solo queda un mando de la PS5 en stock! 🔥\n%s\nMensaje: %s" % (url, text)
            stock = True
        else:
            msg = "F... El mando de la PS5 no esta en stock 😢\n%s\nMensaje: %s" % (url, text)
            stock = True
        if (stock): bot.send(msg)
