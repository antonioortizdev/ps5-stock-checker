from websites import content
from session import client
from bs4 import BeautifulSoup
import bot

class Scraper:
    client = client
    content = content

    def __init__(self, data):
        self.data = data
        self.url = data['url']
        self.messages = data['messages']
        self.stock = False
        self.sent = False
    def soup(self):
        res = self.client.get(self.url)
        print(res)
        return BeautifulSoup(res.text, 'lxml') 
    def notify(self, msg):
        bot.send(msg)
    async def run(self):
        pass