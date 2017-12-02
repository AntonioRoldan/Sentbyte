from newspaper import *
from textblob import TextBlob

papers = []

def collect_papers():
    """The function calls the API to extract information from a given newspaper"""
    cnn_paper = build('http://edition.cnn.com')
    the_guardian = build('https://www.theguardian.com/international', language='en')
    huffington_post = build('http://www.huffingtonpost.co.uk/news/', language='en')
    the_independent = build('http://www.theindependent.com/news/', language='en')
    business_insider = build('http://www.businessinsider.com', language='en')
    return cnn_paper, the_guardian, huffington_post, the_independent, business_insider

def parse_articles(articles):
    for article in articles:
        article.download()
        article.parse()
    return articles

def collect_articles_to(paper):
    """It extracts articles to a given newspaper"""
    articles = []
    title_to_body = {}
    for url in paper.category_urls():
        print(url)
        article = Article(url=url)
        articles.append(article)
    parsed_articles = parse_articles(articles)
    for article in parsed_articles:
        if 'Terms of Service' in article.text.split():
            pass
        else:
            title_to_body[article.title] = article.text
    return title_to_body

def sentbyte():
    print('How much truth is there in the world?')
    paper_to_articles = {} #We store
    for paper in collect_papers():
        papers.append(paper.brand)
        paper_to_articles[paper.brand] = collect_articles_to(paper=paper)
        #print(paper_to_articles[paper.brand])
        #print("\n")
    for paper in papers:
        headlines = paper_to_articles[paper]
        for headline in headlines:
            print(paper_to_articles[paper][headline]) #We extract news one by one
            print("\n")

if __name__ == '__main__':
    sentbyte()
