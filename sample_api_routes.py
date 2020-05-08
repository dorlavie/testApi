from fastapi import FastAPI
import collections
from sample_api_fastapi import *

app = FastAPI()


@app.get("/")
async def root():
    return "Welcome to our wonderful API!"


@app.get("/analyze-text/text")
async def grab_text(url: str = None):
    article_text = grab_text_from_article(url)
    return {'article_text': article_text}


@app.get("/analyze-text/ner")
async def analyze_ner(url: str = None):
    article_text = grab_text_from_article(url)
    ner = ner_with_counts(article_text)

    items = collections.Counter(str(tuple(item)) for item in ner)

    return {'Entities': items}


@app.get("/analyze-text/pos")
async def analyze_pos(url: str):
    article_text = grab_text_from_article(url)
    pos = pos_with_lemma(article_text)

    return {"Parts of Speech": pos}
