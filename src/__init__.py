import json
from review.Review import create_review_from_sample
from src.data.make_first_raw_dataset import import_dataset
from features.normalize import remove_stopwords, letters_only, lower_only
import datetime
import pandas as pd


reviews_set_train = set()
review_set_test = set()
start = datetime.datetime.now()

train, test = import_dataset("reviews_Video_Games.json")

'''
with open(join(_BASIC_PATH ,"interim\\train.json"), 'w') as outfile:
    json.dump(train.to_dict(), outfile)
'''
'''
for index, line in train.iterrows():
    review = create_review_from_sample(line)
    reviews_set_train.add(review)

print(reviews_set_train)

'''
'''
with open("C:\\Users\Xavaios\\Documents\\Fac\\2 semestre\\TM\\TA_project%20_1\\data\\raw\\reviews_Automotive.json", encoding="utf8") as json_file:
    for line in json_file:
        sample = json.loads(line)
        if "reviewerName" in sample:
            review = create_review_from_sample(sample)

            reviews_set.add(review)


for review in reviews_set:
    text = review.reviewText
    text = letters_only(text)
    text = lower_only(text)
    text  = remove_stopwords(text)

'''
print( datetime.datetime.now - start)