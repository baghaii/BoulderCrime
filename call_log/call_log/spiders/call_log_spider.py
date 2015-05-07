import scrapy
import time
from call_log.items import CallLogItem

from datetime import date,timedelta

#use todays date to build a URL
def build_urls():
	urls = []
	base = "https://bouldercolorado.gov/pages/call-log-"

	#Build URLs for the last two weeks
	for i in range(1, 14):
		today = date.today() - timedelta(days=i)
		str_date = today.strftime("%B-%-d-%Y")
		url = base + str_date
		urls.append(url)
	return urls

class CallSpider(scrapy.Spider):
	name = "call"
	allowed_domains = ["bouldercolorado.gov"]
	start_urls = build_urls()

#extracts the text of a given format from the page
	def parse(self, response):
		for sel in response.xpath('//tr'):
			item = CallLogItem()
			[case, date, time, loc, call_type]  = sel.xpath('td/text()').extract()
			item['case'] = case
			item['date'] = date
			item['time'] = time
			item['loc']  = loc
			item['call_type'] = call_type
			yield item
