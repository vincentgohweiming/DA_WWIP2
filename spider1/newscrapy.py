import scrapy
class newvin(scrapy.Spider):
    name = "new_spider"
    start_urls = ["http://192.168.0.120/spicyx/"]
    def parse(self,response):
        for every_line in response.css("img"):
            yield {
                "Image Link": every_line.xpath("@src").extract_first(),
            }
        Page_Selector = ".next a ::attr(href)"
        next_page = response.css(Page_Selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
