from src.data.import_dataset import import_cleaned_training_set, import_cleaned_testing_set
from features.explore import only_nouns, bag_of_words
from models.classification_model import model_bag_of_words, model_bigrams
from datetime import datetime
from visualization.visualize import display_features
import numpy as np


def main():
    start = datetime.now()
    print(start)

    print('Importing training....')
    training = import_cleaned_training_set()

    print('Importing testing....')
    testing = import_cleaned_testing_set()

    print('Taking Out comments')
    comments_training = extract_comments_from_reviews(training)
    comments_testing = extract_comments_from_reviews(testing)
    bow_vec, bow_feat= bag_of_words(comments_training)
    print(comments_training[20000:20020])
    print(display_features(bow_feat[20000:20010, 49700:49820].toarray(), bow_vec.get_feature_names()[49700:49820]))

    '''
    print('Taking Out categories')
    categories_training = extract_categories_from_reviews(training)
    categories_testing = extract_categories_from_reviews(testing)
    categories_training = np.asarray(categories_training)
    categories_testing = np.asarray(categories_testing)

    
    nouns_training = only_nouns(comments_training)
    nouns_testing = only_nouns(comments_testing)
    model_bag_of_words(nouns_training, nouns_testing,categories_training, categories_testing)
    '''

def extract_comments_from_reviews(dataset):
    comments_only = [review.reviewText for review in dataset]
    return comments_only


def extract_categories_from_reviews(dataset):

    categories_only = [review.category for review in dataset]
    return categories_only


def extract_for_wordcloud(dataset):
    movies = [[review.reviewText, review.category] for review in dataset]
    return movies




if __name__ == '__main__':
    main()