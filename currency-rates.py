import urllib
import json
import datetime
import re

class Currency(object):
    """
    ---Documentation---
    """

    def __init__(self, XXX, date = 'today'):
        self.name = XXX.upper()
        self.__getXmlFile(date)
        self.rate = self.rates[self.name]

    def __getXmlFile(self, date):

        url = urllib.urlopen(self.__createLink(date))
        data = json.load(url)
        url.close()

        self.rates = {}
        self.rates =  data['rates']
        self.rates['EUR'] = 1

    def __createLink(self, date):
        if re.search(r'(\d{1,2})\D+(\d{1,2})\D+(\d{4})', date):
            datePattern = re.compile(r'(\d{2})\D+(\d{2})\D+(\d{4})')
            try:
                (day, month, year) = datePattern.match(date).groups()
                link = "".join(('http://api.fixer.io/', year, '-', month, '-', day))
                return link
            except(AttributeError):
                print "Wrong date format"

        elif date is 'today':
            link = 'http://api.fixer.io/latest'
            return link
        else:
            print "Wrong date format. Contemporary date returned."
            return 'http://api.fixer.io/latest'

class Exchange(object):
    """
    ---Documentation---
    """

    def __init__(self, amount, sell, buy, date='today'):
        self.amount = amount
        self.toSell = Currency(str(sell), date)
        self.toBuy = Currency(str(buy), date)

        self.result = (amount/self.toSell.rate)*self.toBuy.rate

#a = Exchange(1000, 'pln', 'EUR')
#print a.amount, a.toSell.name, '=', a.result, a.toBuy.name
