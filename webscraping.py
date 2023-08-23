from bs4 import BeatifulSoup
import urllib.request
from time import sleep
from datetime import datetime

def getGoldPrice():
  url = 'https://www.gold.org/'
  req = urllib.request.urlopen(url)
  page = req.read()
  scraping = BeatifulSoup(page)
  price = scraping.findAll('td', attrs = {'id': spotpriceCellAsk'})[0]
                                          .text
                                          return price


                                        
