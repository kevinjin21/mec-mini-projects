import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        # lets you search by tag in command line
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

        # alternatively just make a list of urls. self.parse with be called by default
    """start_urls = [
        'http://quotes.toscrape.com/page/1/',
        #'http://quotes.toscrape.com/page/2/',
    ]"""

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield{
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            # build an absolute url in case the urls for next page are relative
            #next_page = response.urljoin(next_page)
            #yield scrapy.Request(next_page, callback=self.parse)
            yield response.follow(next_page, callback=self.parse)
            # this follows urls directly without a need to join the url

        """page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)"""