#use scrapy
import scrapy
#create a class
class newvin(scrapy.Spider):
    name = "new_vin"
    #set the target url
    start_urls = ["http://192.168.0.120/spicyx/"]
    #this is to get the  image for every line in the website
    def parse(self,response):
        for every_line in response.css("img"):
            yield {
                "Image link": every_line.xpath("@src").extract_first(),
            }
        #to recurse next page
        Page_Selector = ".next a ::attr(href)"
        next_page = response.css(Page_Selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
