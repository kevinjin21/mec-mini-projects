import scrapy

# scrape information for tag 'love'

class LoveCSS(scrapy.Spider):
    name = 'toscrape-css'

    def start_requests(self):
        url = 'http://quotes.toscrape.com/tag/love/'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page,
                                  callback=self.parse)

