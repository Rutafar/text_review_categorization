import json
import os.path
from review.Review import create_review_from_sample
import datetime
print(os.chdir(".\data\raw\reviews_Books.json"))
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data\\raw\\reviews_Books.json")
reviews_set = set()
start =datetime.datetime.now()
print(start)
with open(path) as json_file:
    for line in json_file:
        sample = json.loads(line)
        if "reviewerName" in sample:
            review = create_review_from_sample(sample)
            reviews_set.add(review)

print(datetime.datetime.now() - start)