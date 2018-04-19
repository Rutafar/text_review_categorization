from tqdm import tqdm
from features.normalize import clean
from data.import_dataset import import_set
from tqdm import tqdm





def main():
    review_set= import_set()
    cleaned_review_set = set()
    for review in tqdm(review_set):
        r = clean(review)
        cleaned_review_set.add(r)
    print(cleaned_review_set)


if __name__ == '__main__':
    main()


