import asyncio
import logging
import bot
import time
from websites import content
#from scrapers import amazon_com_controller, amazon_com
from scrapers.amazon_scraper import AmazonScraper

logging.basicConfig(filename='./logs/debug.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
scrapers = [
    AmazonScraper(content['amazon_com_ps5']),
    AmazonScraper(content['amazon_de_ps5']),
    AmazonScraper(content['amazon_com_ps5_controller']),
    AmazonScraper(content['amazon_de_ps5_controller'])
]
counter = 0
while True:
    logging.info('_- START SCRAPERS # %d -_' % (counter))
    for scraper in scrapers:
        asyncio.run(scraper.run())
    logging.info('_- END SCRAPERS # %d -_' % (counter))
    time.sleep(0.5)