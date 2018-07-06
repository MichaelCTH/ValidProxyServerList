# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import csv

class ProxyserverspiderPipeline(object):
    def process_item(self, item, spider):
        print(item)
        return item

class ProxyserverValidatePipeline(object):
    def process_item(self, item, spider):
        proxy = {item['ReqType'].lower():'http://'+item['IP']+':'+item['PORT']}
        try:
            r = requests.get(item['target'],proxies=proxy, timeout=3)
            if r.status_code == 200:
                #update new measured delay
                item['Delay'] = r.elapsed.total_seconds()
                return item
        except:
            return None

class ProxyserverTxtPipeline(object):
    fields = ['IP','PORT','ProxyType','ReqType','Loc','Delay']
    sortList = {}

    def close_spider(self, spider):
        order = sorted(self.sortList.keys())
        with open('ValidProxyList.txt','w') as f:
            f.write('\t'.join(self.fields)+'\n')
            for p in order:
                f.write('\t'.join(str(self.sortList[p][field]) for field in self.fields)+'\n')

    def process_item(self, item, spider):
        if item:
            self.sortList[item['Delay']] = item
