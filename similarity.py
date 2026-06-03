from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def similarity_score(resume,jd):

    match=[resume,jd]
    vectorizer=TfidfVectorizer()
    matrix=vectorizer.fit_transform(match)
    #features=vectorizer.get_feature_names_out(match)
    
    similarity_score=cosine_similarity(matrix[0:1],matrix[1:2])
    return similarity_score[0][0]*100