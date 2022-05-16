import wikipediaapi
from flask_restful import Resource


class SourceWikiPedia(Resource):
    @classmethod
    def get(cls, word: str):
        wiki_wiki = wikipediaapi.Wikipedia('pt')

        page_py = wiki_wiki.page(word)
        texto = page_py.summary
        if texto:
            return texto.replace('\n', " ")
        else:
            return f"Nada encontrado para {word}"
