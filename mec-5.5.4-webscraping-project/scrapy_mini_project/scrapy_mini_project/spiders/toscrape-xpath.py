import scrapy

# scrape information for tag 'love'

class InsXPath(scrapy.Spider):
    name = 'toscrape-xpath'

    def start_requests(self):
        url = 'http://quotes.toscrape.com/tag/inspirational/'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        j = 0
        for i in response.xpath('//div[@class]'):
            j+=1
            yield{
                'text': response.xpath('//div[@class][' + str(j) + ']/span/text()').get()
            }
