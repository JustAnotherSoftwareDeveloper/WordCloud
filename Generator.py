from os import path
from PIL import Image
import numpy as np
import random
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def green_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    shade = random.randint(10, 30)
    return "hsl(127, 80%, " + str(shade) + "%)"


if __name__ == '__main__':
    d = path.dirname(__file__)
    text = open(path.join(d, 'const.txt')).read()

    liberty_mask = np.array(Image.open(path.join(d, "liberty.png")))
    stopwords = set(STOPWORDS)
    stopwords.add("Article")
    stopwords.add("United")
    stopwords.add("States")
    stopwords.add("State")

    wc = WordCloud(collocations=False, height=2129, width=2000, background_color="white", mask=liberty_mask,
                   stopwords=stopwords)

    wc.generate(text)
    wc.recolor(color_func=green_color_func, random_state=3)
    wc.to_file(path.join(d, "liberty_cloud.png"))
    print("Done")
