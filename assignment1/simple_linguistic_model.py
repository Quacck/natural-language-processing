import pandas
import re
import gensim
from sklearn import linear_model
from sklearn import feature_extraction
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import CountVectorizer

numberOfDataPoints = 100000

def createCorpus(data):
    result = data['instructions'].to_numpy().tolist()[1:numberOfDataPoints]
    result = list(filter(lambda entry: isinstance(entry, str), result))
    return list(map(lambda line: re.findall("[A-Za-z]+", line.lower()), result))

def main():
    data = pandas.read_csv('preprocessed_data.csv', '|')
    corpus = createCorpus(data)


    model = gensim.models.Word2Vec(corpus)

    model.wv.save('word2vec.bin')
    #model = gensim.models.KeyedVectors.load('word2vec.bin')

    #print(model.most_similar('beans', topn=10))  # get other similar words
if __name__ == "__main__":
    main()
