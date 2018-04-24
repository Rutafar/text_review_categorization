from src.data.import_dataset import import_cleaned_training_set
from data.export_dataset import export_comments
from models.classification_model import lsa
from features.explore import bag_of_words, only_nouns, tf_idf
import matplotlib.pyplot as plt

def main():
    training = import_cleaned_training_set()
    comments = extract_comments_from_reviews(training)

    bow_vectorizer, bow_features = bag_of_words(comments)
    lsa(bow_features)
    tf, idf = tf_idf(comments)
    '''
    nouns = only_nouns(comments)
    print(nouns)
    bow_vectorizer_nouns, bow_features_nouns = bag_of_words(nouns)
    '''





def extract_comments_from_reviews(dataset):
    comments_only = [review.reviewText for review in dataset]
    return comments_only



if __name__ == '__main__':
    main()