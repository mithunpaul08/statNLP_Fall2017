from __future__ import division
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from csv import DictReader
from sklearn.feature_extraction.text import TfidfTransformer


nltk.download('punkt')
#nltk.download('wordnet')


stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))




def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

def tokenize(document):
    #todo:Try out with each of the following- and report change in accuracy
#     strip_accents : {‘ascii’, ‘unicode’, None}
# analyzer
#     stop_words
#     lowercase
#     max_df
#     min_df

    vectorizer = CountVectorizer(tokenizer=normalize, stop_words='english')
    X = vectorizer.fit_transform(document).toarray()
    ##print("features are:"+str(vectorizer.get_feature_names()))
    return X,vectorizer

def tokenizeWithBigrams(document):

    vectorizer = CountVectorizer(tokenizer=normalize, stop_words='english',ngram_range=(2, 2))
    X = vectorizer.fit_transform(document).toarray()

    ##print("features are:"+str(vectorizer.get_feature_names()))
    return X,vectorizer


def tokenizeWithBothUniBigrams(document):

    vectorizer = CountVectorizer(tokenizer=normalize, stop_words='english',ngram_range=(1, 2), min_df=5)
    X = vectorizer.fit_transform(document).toarray()




    ##print("features are:"+str(vectorizer.get_feature_names()))
    return X,vectorizer


def createAtfidfVectorizer():
    vectorizer2 = TfidfVectorizer(tokenizer=normalize, stop_words='english')
    return vectorizer2

def createAtfidfVectorizer():
    vectorizer2 = TfidfVectorizer(tokenizer=normalize, stop_words='english')
    return vectorizer2
