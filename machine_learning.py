from __future__ import print_function
import string
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors
from sklearn.externals import joblib
# import numpy as np
# import sklearn
# import nltk
# import re
# import os
# import codecs
# from sklearn import feature_extraction
# import mpld3


def instructions_split(instructions):  # tokenize
    instructions = instructions.lower()
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

def get_suggested(last_cooked):
    with open('all_recepies.json', 'r') as f:
        content = json.loads(f.read())
    tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,
                                     min_df=0.05, stop_words=stop_words,
                                     use_idf=True, tokenizer=instructions_split)

    instructions = [item['instructions'] for item in content]
    titles = [item["title"] for item in content]
    ingredients = [item["ingredients"] for item in content]
    tfidf_matrix = tfidf_vectorizer.fit_transform(instructions)

    num_clusters = 100

    km = KMeans(n_clusters=num_clusters)

    km.fit_predict(tfidf_matrix)

    clusters = km.labels_.tolist()


    # print(tfidf_matrix.shape)
    # print(tfidf_vectorizer.get_feature_names())
    # print(len(clusters))
    # print('\nNew recipe:'.join([item[0] for item in zip(instructions, clusters) if item[-1] == 15]))

    for i in range(len(content)):
        if content[i]["title"] == last_cooked:
            index = i
            break

    near = NearestNeighbors(n_neighbours=5, algorithm='ball_tree').fit(tfidf_matrix)

    dist, indices = near.kneighbors(tfidf_matrix[index])
    title_result = [titles[index] for index in indices[0]]
    instructions_result = [instructions[index] for index in indices[0]]
    ingredients_result = [ingredients[index] for index in indices[0]]
    data = {}
    for i in range(1, len(title_result)):
        data[i] = [title_result[i], ingredients_result[i], instructions_result[i]]
    with open("suggested_recipe.json", 'w') as f:
        json.dump(data, f, indent=True, ensure_ascii=False)
    # print('\nNew recipe'.join([instructions[index] for index in indices[0]]))
    # print(''.join([titles[index] for index in indices[0]]))
get_suggested("Панирано пилешко вретено със сусам")
