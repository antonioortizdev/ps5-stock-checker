from scrapers.scraper import Scraper

class AmazonScraper(Scraper):
    async def run(self):
        try:
            soup = self.soup()
            found=soup.find(id='selectQuantity')  
            availability = soup.find(id='availability').find('span', {'class':'a-size-medium'}).text.strip()
            productTitle = soup.find(id='productTitle').text.strip()
            print('%s -> %s' % (availability, productTitle))
            if found:   #above result can be none so checking if result is not none
                self.stock = True
                msg = self.messages['stock'] + "\nMensaje: %s\n%s" % (availability, self.url)
                if (not self.sent and self.stock):
                    self.notify(msg)
                    self.sent = True
            else:
                self.stock = False
                self.sent = False
        except Exception as ex:
            print('error, try again')


