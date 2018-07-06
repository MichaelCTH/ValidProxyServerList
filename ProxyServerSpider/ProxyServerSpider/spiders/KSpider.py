import scrapy
from ProxyServerSpider.items import ProxyserverspiderItem
import time

class KSpider(scrapy.Spider):
    #Global Variables
    name = 'KSpider'
    numPage = 10
    target = 'https://www.taobao.com/'
    urls = []

    # Constructor
    def __init__(self, *args, **kwargs):
        proxy = kwargs.pop('proxy',[])
        page = kwargs.pop('numPage',[])
        web = kwargs.pop('target',[])

        if page:
            self.numPage = int(page)
        if web:
            self.target = web

        #generate urls for request
        for num in range(1,self.numPage+1):
            if proxy == 'elite':
                self.urls.append('https://www.kuaidaili.com/free/inha/{}'.format(num))
            else:
                self.urls.append('https://www.kuaidaili.com/free/intr/{}'.format(num))

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)
            time.sleep(1)
            #Wait 1 second between requests to avoid 503 and robot-detect

    def parse(self, response):
        if '200' not in str(response):
            print(str(response))
            return

        if 'Invalid Page' == response.xpath('/html/body/text()').extract():
            return

        proxyList = response.xpath('//*[@id="list"]/table/tbody/tr')
        IP = proxyList.xpath('./td[1]/text()').extract()
        PORT = proxyList.xpath('./td[2]/text()').extract()
        ProxyType = proxyList.xpath('./td[3]/text()').extract()
        ProxyType = ['elite' if val == '高匿名' else 'anonymous' for val in ProxyType]
        ReqType = proxyList.xpath('./td[4]/text()').extract()
        Loc = proxyList.xpath('./td[5]/text()').extract()
        Delay = proxyList.xpath('./td[6]/text()').extract()

        items = []
        for e in zip(IP, PORT, ProxyType, ReqType, Loc, Delay):
            item = ProxyserverspiderItem()
            item['target'] = self.target
            item['IP'] = e[0]
            item['PORT'] = e[1]
            item['ProxyType'] = e[2]
            item['ReqType'] = e[3]
            item['Loc'] = e[4]
            item['Delay'] = e[5]
            items.append(item)
        return items
