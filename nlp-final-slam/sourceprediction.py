"""

In which we look at how accurately a classifier predicts sources based on training data

"""

from newsapi import NewsApiClient
import datetime

now = datetime.datetime.now()
now_str = now.strftime('%Y') + "-" + now.strftime('%m') + "-" + now.strftime('%d')
monthago = now - datetime.timedelta(days=30)
monthago_str = monthago.strftime('%Y') + "-" + monthago.strftime('%m') + "-" + monthago.strftime('%d')


# build a toy corpus of headlines given a source
def build_source(source):
    source_headlines = []
    news_api = NewsApiClient(api_key='063f02817dbb49528058d7372964f645')
    x = 1
    while x <= 4:
        s_headlines = \
            news_api.get_everything(sources=source, from_param=monthago_str, to=now_str,
                                    language='en',
                                    sort_by='relevancy', page_size=100, page=x)['articles']
        s_titles = [article['title'] for article in s_headlines]
        s_titles = list(filter(None.__ne__, s_titles))
        source_headlines.extend(s_titles)
    return source_headlines





if __name__ == '__main__':
    text = input('Would you like to test headlines or sources? (enter headlines or sources) ')
    if text == 'headlines':
        headlines = input('Please type in your headline: ')
    if text == 'sources':
        source = input('Please type in your source, found on the sources.txt list: ')