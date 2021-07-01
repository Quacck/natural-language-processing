from numpy import number
import sklearn
import pandas
import json
import os
import re

from sklearn.feature_extraction.text import CountVectorizer

datasetNames = [
    'recipes_raw_nosource_ar.json',
    'recipes_raw_nosource_epi.json',
    'recipes_raw_nosource_fn.json',
]

numberOfSentences = int(0)

def readData():
    result = []

    for datasetName in datasetNames:
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, './data/' + datasetName)
        data = json.loads(open(filename).read())

        # data contains some kind of hash as the top level entry, which we dont need

        for entry in data.values():
            entry.pop('picture_link', None) # more hashes that can we disregarded
            try:
                # Split Instructions into sentence
                # https://towardsdatascience.com/tokenize-text-columns-into-sentences-in-pandas-2c08bc1ca790
                entry['instructions'] = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|!)\s", entry['instructions'])
            except:
                pass

            asJson = json.dumps(entry)
            asJson.encode("ascii", "ignore").decode()
            result.append(asJson)
            global numberOfSentences
            numberOfSentences += len(entry)
    
    return result

def main():
    data = readData()

    global numberOfSentences

    vectorizer = CountVectorizer(encoding='utf-16')
    counts = vectorizer.fit_transform(data)
    # print(vectorizer.get_feature_names())
    print('Number of documents = ', len(data))
    print('Number of tokens = ', len(vectorizer.vocabulary_))
    print('Number of Sentences = ', numberOfSentences)

    panda_counts = pandas.DataFrame.sparse.from_spmatrix(
        data=counts,
        columns=vectorizer.get_feature_names()
    )
    summedUp = panda_counts.sum()

    overallSum = 0
    for count in summedUp.values:
        overallSum += count
    print('Number of Words = ', overallSum)

if __name__ == "__main__":
    main()