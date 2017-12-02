from newspaper import *

titles = []

def collect_papers():
    """The function calls the API to extract information from a given newspaper"""
    cnn_paper = build('http://money.cnn.com/news/traders/')
    return cnn_paper

def parse_articles(articles):
    for article in articles:
        article.download()
        article.parse()
    return articles

def collect_articles_to(paper):
    articles = []
    title_to_body = {}
    for url in paper.category_urls():
        print(url)
        article = Article(url=url)
        articles.append(article)
    parsed_articles = parse_articles(articles)
    for article in parsed_articles:
        titles.append(article.title)
        title_to_body[article.title] = article.text
    return title_to_body

def sentbyte():
    print('What do the markets say today?')
    paper_to_articles = {}
    paper = collect_papers()
    news_brand = paper.brand
    paper_to_articles[news_brand] = collect_articles_to(paper=paper)
    for title in titles:
        if "Terms of Service" in paper_to_articles[news_brand][title]:
            pass
        else:
            print(paper_to_articles[news_brand][title])
            print("\n")

if __name__ == '__main__':
    sentbyte()
