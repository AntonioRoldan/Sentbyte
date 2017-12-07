from newspaper import *
from textblob import TextBlob
from matplotlib import pyplot as plt
from matplotlib import style
import seaborn as sns
import pandas as pd

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
        article = Article(url=url)
        articles.append(article)
    parsed_articles = parse_articles(articles)
    for article in parsed_articles:
        article_sentiment = TextBlob(article.text).sentiment
        if not article_sentiment.polarity and not article_sentiment.subjectivity: #Neutral articles must be filtered out
            pass
        else:
            title_to_body[article.title] = article.text
    return title_to_body

def print_space(str):
    print(str)
    print("\n")
def set_data(xs, ys):
    data = pd.DataFrame()
    data['x'] = xs
    data['y'] = ys
    return data


def display_articles(truthful, deceitful, paper):
    print_space("Source: ")
    print_space(paper)
    print_space("Truthful articles: ")
    truthful = list(set(truthful))
    deceitful = list(set(deceitful))
    for article in truthful:
        print_space(article)
    print_space("Deceitful articles: ")
    for article in deceitful:
        print_space(article)

def plot_articles(x, y, paper):
    plt.plot(x, y)
    plt.title(paper)
    plt.ylabel('Deceitful')
    plt.xlabel('Truthful')
    plt.show()

def scatter_articles(xs, ys, paper):
    data = set_data(xs, ys)
    sns.set_context("notebook", font_scale=1.1)
    sns.set_style("darkgrid")
    sns.lmplot('x', 'y', data=data, fit_reg=True)
    plt.title(paper)
    plt.xlabel('Truthfulness')
    plt.ylabel('Deceitfulness')

def sentbyte():
    """It will find out if news from different sources are fake or real"""
    print('How much truth is there in the world today?')
    colour_index = 0
    paper_to_articles = {} #We store
    for paper in collect_papers():
        papers.append(paper.brand)
        paper_to_articles[paper.brand] = collect_articles_to(paper=paper)
    for paper in papers:
        x = []  # Stores truthful news
        y = []  # Stores deceitful news
        truthful = []
        deceitful = []
        headlines = paper_to_articles[paper]
        for headline in headlines:
            article = TextBlob(paper_to_articles[paper][headline]) #We extract news one by one
            if article.sentiment.polarity > article.sentiment.subjectivity:
                truthful.append(article)
            else:
                deceitful.append(article)
            x.append(article.sentiment.polarity*2)
            y.append(article.sentiment.subjectivity*2)
        scatter_articles(x, y, paper)
        plot_articles(x, y, paper)
        display_articles(truthful, deceitful, paper)
if __name__ == '__main__':
    sentbyte()
