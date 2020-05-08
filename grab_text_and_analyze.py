# Import Statements
from readability import Document
from requests import get
import bs4
import en_core_web_sm
from collections import Counter

# Instantiate global vars
nlp = en_core_web_sm.load()

# Function to grab text from the article body
def grab_text_from_article(url):

    response = get(url)
    doc = Document(response.text)

    title = doc.title()

    summary = doc.summary()
    article_body = bs4.BeautifulSoup(summary, features="lxml").get_text()

    return f"{title} : {article_body}"

# Function to derive Named Entity Recognition (ner) with counts
def ner_with_counts(text):

    doc = nlp(text)
    labels = [(x.text, x.label_) for x in doc.ents]
    counter = Counter(labels)

    return counter

# Function to derive Part of Speech (pos) with lemma
def pos_with_lemma(text):

    doc = nlp(text)
    stop_punct = [y for y in doc if not y.is_stop and y.pos_ != 'PUNCT']
    pos_tagg = [(x.lemma_, x.pos_) for x in stop_punct]

    return pos_tagg
