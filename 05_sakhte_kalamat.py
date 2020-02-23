# coding=UTF-8
import os
from os import path
import re
import arabic_reshaper
import matplotlib.pyplot as plt
import numpy as np
from bidi.algorithm import get_display
from PIL import Image
from wordcloud import STOPWORDS, WordCloud

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

text = open(path.join(d, 'data/tweets.txt')).read()

# read the mask image
alice_mask = np.array(Image.open(path.join(d, "file/mask.png")))

# add stopwords
stopwords = STOPWORDS

# make Farsi


def make_farsi(x):
    reshaped_text = arabic_reshaper.reshape(text)
    farsi_text = get_display(reshaped_text)
    return farsi_text


wc = WordCloud(background_color="white", font_path="file/sans.ttf", contour_width=3, contour_color='firebrick', max_words=2000, mask=alice_mask,
               stopwords=stopwords, max_font_size=250, random_state=10).generate(make_farsi(0))

wc.to_file(path.join(d, "final/mabbaszadegan.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
