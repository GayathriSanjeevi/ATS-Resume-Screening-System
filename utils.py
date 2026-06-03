import string
import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
nltk.download('punkt_tab')

from nltk.corpus import stopwords
from nltk import word_tokenize

def text_processing(file1):
    stopword=nltk.corpus.stopwords.words("english")

    file1=file1.lower()
    file1_token=word_tokenize(file1)
    file1_no_stopword=[i for i in file1_token if i not in stopword]
    
    punctuation=string.punctuation
    file1_no_punc=[i for i in file1_no_stopword if i not in punctuation]
    
    file1_cleaned=" ".join(file1_no_punc)

    return file1_cleaned



