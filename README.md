# Valid Proxy Server List
> Grabbing valid &amp; free live proxy list by using Scrapy

## Intro
...todo
## Motivation
...todo
##	Requirements
- `python 3.x.x` (`3.7.0` is currently not supported by Scrapy)
- `Scrapy 1.5.0`
- `requests 2.19.1`: HTTP lib for Python


## Execution
### Parameters
option | description | default
------------ | ------------- | -------------
`proxy` | proxy type (`elite` or `anonymous`) | `anonymous`
`numPage` | number of list pages to crawl | `10`
`target` | url for validation | `https://taobao.com`

### Command
```shell
scrapy crawl KSpider [-a '', ...]
```
### Example 1
```shell
scrapy crawl KSpider -a 'proxy=elite' -a 'numPage=5' -a 'target=https://google.com'
```
### Result
After each successful crawling, a text file will be created in the current working directory, called `ValidProxyList.txt`. All valid proxies are listed in the text file from the least response time to the most.
## Todo
- [ ] Add support for http://www.google-proxy.net
- [ ] Storage pipeline enhancement

