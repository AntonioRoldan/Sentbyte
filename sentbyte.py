from newspaper import *


def collect_papers():
    """The function calls the API to extract information from a given newspaper"""
    cnn_paper = build('http://money.cnn.com/news/traders/')
    return cnn_paper

def curate_data(key, articles):
    for article in articles:
        article.download()
        article.parse()
        if key not in list(article.title):
            if key not in list(article.text):
                pass
            else:
                articles.remove(article)
                article_found = True
        else:
            articles.remove(article)
            article_found = True
    return articles

def filter_by_keyword(title):
    keywords = ("business", "investment", "investing", "markets", "currency", "bitcoin", "bank", "banking", "currency", "stock-market", "nasdaq")
    title = []
    for keyword in keywords:
        if keyword in title:
            return title
        else:
            return False

def collect_articles_to(key, paper):
    articles = []
    title_to_body = {}
    articles_found = False
    for url in paper.category_urls():
        print(url)
        article = Article(url=url)
        articles.append(article)
    articles = curate_data(key, articles)
    for article in articles:
        title_to_body[article.title] = article.text
        print(article.text.split())
        print("\n")
    return articles

def sentbyte():
    key = print('What do the markets say today?')
    paper_to_articles = {}
    paper = collect_papers()
    news_brand = paper.brand
    paper_to_articles[news_brand] = collect_articles_to(key=key, paper=paper)




sentbyte()
