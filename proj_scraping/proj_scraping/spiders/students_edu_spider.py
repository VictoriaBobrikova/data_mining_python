from scrapy.spiders import CrawlSpider

class StudentSpider(CrawlSpider):
    name = "StudentEdu"
    allowed_domains = ["vk.com"]
    start_urls = []
    rules = (
        Rule(),
        Rule()
    )