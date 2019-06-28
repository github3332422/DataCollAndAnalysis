# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from BossSpider.items import BossspiderItem


class BossSpider(CrawlSpider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    start_urls = [
        # 'https://www.zhipin.com/c101010100-p100599/?ka=search_100599'
        # 'https://www.zhipin.com/c101010100-p100506/?ka=search_100506'
        # 'https://www.zhipin.com/c101010100-p100507/?ka=search_100507'
        # 'https://www.zhipin.com/c101010100-p100508/?ka=search_100508'
        # 'https://www.zhipin.com/c101010100-p100509/?ka=search_100509'
        # 'https://www.zhipin.com/c101010100-p100511/?ka=search_100511'
        # 'https://www.zhipin.com/c101010100-p100512/?ka=search_100512'
        # 'https://www.zhipin.com/c101010100-p100513/?ka=search_100513'
        'https://www.zhipin.com/c101010100-p100101/?query=%E5%AE%9E%E4%B9%A0%E7%94%9F&page=1&ka=page-1'
    ]

    rules = (
        # Rule(LinkExtractor(allow="page=\d+"),  follow=True),
        Rule(LinkExtractor(allow="/?query=.*?&page=\d+"), follow=True),
        Rule(LinkExtractor(allow="/job_detail/.*?"), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item =BossspiderItem()
        name = response.xpath("//div[@class='info-primary']/div[@class='name']/h1//text()").extract()[0]
        salary = response.xpath("//div[@class='info-primary']/div[@class='name']/span//text()").extract()[0].split('-')
        highSalary = salary[0]
        lowSalary = salary[1]
        msg = response.xpath("//div[@class='job-primary detail-box']/div[@class='info-primary']/p//text()").extract()
        place = msg[0]
        expersion = msg[1]
        education = msg[2]
        fulis = response.xpath("//div[@class='job-tags']/span//text()").extract()
        fuli = ''.join([x.strip() for x in fulis])
        yaoqius = response.xpath("//div[@class='job-sec']/div[@class='text']//text()").extract()
        yaoqiu = ''.join([x.strip() for x in yaoqius if len(str(x.strip())) > 0 and str(x.strip())[0] not in ['岗','职','任','【']])

        item['name'] = name
        item['highSalary'] = highSalary
        item['lowSalary'] = lowSalary
        item['place'] = place
        item['expersion'] = expersion
        item['education'] = education
        item['fuli'] = fuli
        item['yaoqiu'] = yaoqiu
        print(item)
        return item
