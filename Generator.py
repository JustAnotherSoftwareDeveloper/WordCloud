from os import path
from PIL import Image
import numpy as np
import random
import string
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


class WordCloudGenerator:
    def __init__(self, mask, color_func, excludes: set, height: int, width: int, text: string, output, color):
        self.image_mask = mask
        self.color_func = color_func
        self.excluding_words = excludes
        self.height = height
        self.width = width
        self.document_text = text
        self.output_name = output
        self.background_color = color

    def generate(self):
        stopwords = set(STOPWORDS)
        stopwords.union(self.excluding_words)
        wc = WordCloud(collocations=False, height=self.height, width=self.width, background_color=self.background_color,
                       mask=self.image_mask, stopwords=stopwords)
        wc.recolor(self.color_func)
        return wc

    def generate_and_write(self):
        d = path.dirname(__file__)
        wc = self.generate()
        wc.to_file(path.join(d, self.output_name))
