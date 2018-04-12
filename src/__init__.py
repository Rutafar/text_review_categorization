import json
import os.path
from review.Review import create_review_from_sample
import datetime
import pandas as pd
from features.normalize import remove_stopwords, letters_only, lower_only





#path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data\\raw\\reviews_Automotive.json")
reviews_set = set()
start =datetime.datetime.now()
with open("C:\\Users\\Serras\\Documents\\Fac\\2s\\TA\\textanalytics1\\data\\raw\\reviews_Video_Games.json", encoding="utf8") as json_file:
    dataframe = pd.read_json(json_file, lines=True)

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
print(datetime.datetime.now() - start)
'''