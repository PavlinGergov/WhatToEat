import string
import json
import sklearn
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn.cluster import KMeans

# import mpld3


def instructions_split(instructions):  # tokenize
    instructions = instructions.lower()
    # letters = 'абвгдежзийклмнопрстуфхцчшщъьюя'
    instructions = instructions.split()
    instructions = [word.strip(string.punctuation) for word in instructions]
    instructions = [word for word in instructions if word.isalpha() and len(word) > 2]

    return instructions


def to_words(a_file):

    result = set()

    with open(a_file, 'r') as f:
        content = json.loads(f.read())
    for recipe in content:
        info = instructions_split(recipe['instructions'])
        for word in info:
            if word not in result:
                result.add(word)
    return list(result)

print(len(to_words('all_recepies.json')))

stop_words = ['без', 'бърка', 'веднага', 'вкус', 'вода', 'водата', 'време', 'връзка',
'всички', 'всичко', 'всяка', 'във', 'върху', 'гарнитура', 'глава', 'глави', 'готви', 'готовност',
'готово', 'градуса', 'двете', 'добавя', 'добавят', 'добре', 'докато', 'дълбок', 'дълбока', 'едри',
'едро', 'желание', 'загрята', 'заедно', 'залива', 'заливат', 'захлупва', 'златисто', 'ивици', 'изважда',
'изваждат', 'измива', 'измиват', 'изсипва', 'или', 'капак', 'като', 'когато', 'което', 'които', 'колелца',
'коричка', 'котлона', 'която', 'кубчета', 'купа', 'къкри', 'към', 'леко', 'листа', 'малки', 'малко',
'минути', 'много', 'може', 'накрая', 'налива', 'намазва', 'напълно', 'нареждат', 'нарязан', 'нарязани',
'нарязаните', 'нарязаният', 'нарязва', 'нарязват', 'настърган', 'него', 'нея', 'няколко', 'обелват',
'овалват', 'овкусява', 'овкусяват', 'огън', 'около', 'омекване', 'омекнат', 'омекне', 'опаковката',
'оставя', 'оставят', 'отгоре', 'отстранява', 'отцежда', 'отцеждат', 'още', 'парченца', 'парчета',
'под', 'поднася', 'подправките', 'подправя', 'подреждат', 'подсолена', 'поеме', 'покрива', 'половин',
'половината', 'полумесеци', 'получената', 'порции', 'поръсва', 'поръсват', 'посолява', 'посоляват',
'поставя', 'поставят', 'почиства', 'предварително', 'преди', 'през', 'пресен', 'при', 'прибавя',
'прибавят', 'приготвя', 'продуктите', 'пълна', 'разбиват', 'разбитите', 'разбърква', 'разбъркват',
'сгъсти', 'сервира', 'сервират', 'ситно', 'слага', 'слагат', 'след', 'според', 'стане', 'старателно',
'страна', 'страни', 'студена', 'със', 'също', 'тази', 'така', 'течността', 'час', 'часа', 'част', 'щом']


with open('all_recepies.json', 'r') as f:
    content = json.loads(f.read())
tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,
                                 min_df=0.05, stop_words=stop_words,
                                 use_idf=True, tokenizer=instructions_split)

instructions = [item['instructions'] for item in content]
tfidf_matrix = tfidf_vectorizer.fit_transform(instructions)


num_clusters = 100

km = KMeans(n_clusters=num_clusters)

km.fit_predict(tfidf_matrix)

clusters = km.labels_.tolist()


print(tfidf_matrix.shape)
print(tfidf_vectorizer.get_feature_names())
print(len(clusters))

print('\nNew recipe:'.join([item[0] for item in zip(instructions, clusters) if item[-1] == 15]))
