import pandas
import re
import gensim
from sklearn import linear_model
from sklearn import feature_extraction
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import CountVectorizer

numberOfDataPoints = 10000

def createCorpus(data):
    result = data['instructions'].to_numpy().tolist()[1:numberOfDataPoints]
    result = list(filter(lambda entry: isinstance(entry, str), result))
    return list(map(lambda line: re.findall("[A-Za-z]+", line), result))
    

def createDictionaries(listOfFeatures):
    featureToIndex = {}
    indexToFeature = {}

    index = 0

    for feature in listOfFeatures:
        featureToIndex[feature] = index
        indexToFeature[index] = feature
        index += 1
    return featureToIndex, indexToFeature

def buildEmbeddingTrainingData(corpus, featureToIndex, indexToFeature, vectorSize):
    result = []
    for text in corpus:
        onlyText = re.findall("[A-Za-z]+", text.lower())
        
    return result

def main():
    # stop_words = text.ENGLISH_STOP_WORDS.union(["<LINEBREAK>", "<LISTELEMENT>"])

    data = pandas.read_csv('preprocessed_data.csv', '|')
    corpus = createCorpus(data)

    model = gensim.models.Word2Vec(corpus)

    model.wv.save_word2vec_format('word2vec.bin')

    print(model.wv['cake'])  # get numpy vector of a word

    print(model.wv.most_similar('cake', topn=10))  # get other similar words
if __name__ == "__main__":
    main()
