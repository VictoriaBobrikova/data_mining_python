from scrapy.spiders import CrawlSpider


class StudentSpider(CrawlSpider):
    name = "students_edu_spider"
    allowed_domains = ["vk.com"]
    start_urls = [
        "https://vk.com/search?c%5Bcity%5D=2&c%5Bcountry%5D=1&c%5Bper_page%5D=40&c%5Bphoto%5D=1&c%5Bsection%5D=people&c%5Buniversity%5D=56"
    ]
    rules = (
        Rule(),
        Rule()
    )
