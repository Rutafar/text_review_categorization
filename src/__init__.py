import json
from review.Review import create_review_from_sample
from src.utils.utils import get_file_names
from src.data.make_first_raw_dataset import import_dataset, export_sampled_datasets
from features.normalize import remove_stopwords, letters_only, lower_only
import datetime
from tqdm import tqdm
import pandas as pd


start = datetime.datetime.now()
files = get_file_names()

for file in tqdm(files):
    test = import_dataset(file)
    export_sampled_datasets(test, file)


#export_sampled_datasets(train, test)

'''
for index, line in train.iterrows():
    review = create_review_from_sample(line)
    reviews_set_train.add(review)

print(reviews_set_train)

'''
'''
for review in reviews_set:
    text = review.reviewText
    text = letters_only(text)
    text = lower_only(text)
    text  = remove_stopwords(text)

'''
print(datetime.datetime.now() - start)
