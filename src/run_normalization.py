from tqdm import tqdm
from features.normalize import clean
from data.import_dataset import import_set
from tqdm import tqdm
from data.export_dataset import export_dataset
from features.explore import bag_of_words





def main():
    review_set= import_set()
    cleaned_review_set = set()
    for review in tqdm(review_set):
        r = clean(review)
        bag_of_words(r.reviewText)
        cleaned_review_set.add(r)
        export_dataset(cleaned_review_set)
    print(cleaned_review_set)



if __name__ == '__main__':
    main()


