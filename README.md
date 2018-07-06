# Valid Proxy Server List
> Grabbing valid &amp; free live proxy list by using Scrapy

## Intro
### Motivation
HTTP Proxy is a promising solution to hide/modify identification info from each request, while it is also helpful to bypass the request limit on the target server. For example: 

- Data collector or social network analyst who frequently collect large size of data from websites using web crawling are sometimes frustrated with the request limit and has to obey it. A proxy can be used to bypass those IP-based request limit.
- Contents that with regional lockout also cannot be accessed successfully and can leverage proxy to change the requester's address in order to get access. 

However, finding the best/fast proxy server for your purpose is difficult and time-consuming, as a massive number of free proxy servers are available online. Also, communication delay is not precisely examined between user host and target URL, instead, an estimated delay is usually offered by the proxy provider.

### Free Proxy
###### HTTP Proxy Type
There are three different types in HTTP Proxy, and this tool provides the option for you to choose the proper proxy type.

> [ref] https://tech.tiq.cc/2012/06/differences-between-transparent-anonymous-and-elite-proxy/

- `Transparent`: A transparent proxy sends your real IP address in the HTTP_X_FORWARDED_FOR header, this means a website that does not only determine your REMOTE_ADDR but also check for specific proxy headers will still know your real IP address. The HTTP_VIA header is also sent, revealing that you are using a proxy server.
- `Anonymous`: An anonymous proxy does not send your real IP address in the HTTP_X_FORWARDED_FOR header, instead it submits the IP address of the proxy or is just blank. The HTTP_VIA header is sent like with a transparent proxy, also revealing that you are using a proxy server.
- `Elite`: An elite proxy only sends REMOTE_ADDR header, the other headers are blank/empty, hence making you seem like a regular internet user who is not using a proxy at all.

###### Available Providers
At moment, a list of available proxy providers that supported in this tool are:

1. https://kuaidaili.com

### Crawling
Once the program is launched, this tool will crawl the free proxies from the known proxy providers in above list, based on user's choice of HTTP proxy type.

### Connection Exam and Delay Measurement
Not all the crawled proxies are always available and also the communication delay has to be re-examined between user host and target URL precisely. Thus, this tool also examines the connection between user host and target URL (https://taobao.com, by default) and calculate the elapsed time during the connection. Finally, ranking the available proxies by response time.

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

