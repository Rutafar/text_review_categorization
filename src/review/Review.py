class Review(object):
    '''
    reviewerID - ID of the reviewer, e.g. A2SUAM1J3GNN3B
    asin - ID of the product, e.g. 0000013714
    reviewerName - name of the reviewer
    helpful - helpfulness rating of the review, e.g. 2/3
    reviewText - text of the review
    overall - rating of the product
    summary - summary of the review
    unixReviewTime - time of the review (unix time)
    reviewTime - time of the review (raw)

    '''

    def __init__(self, reviewerID, productID,  helpful, reviewText, overall, summary, category):
        self.reviewerID = reviewerID
        self.productID = productID
        self.helpful = helpful
        self.reviewText = reviewText
        self.overall = overall
        self.summary = summary
        self.category = category


def create_review_from_sample(sample, category):
    review = Review(sample['reviewerID'], sample['asin'],  sample['helpful'], sample['reviewText'], sample['overall'], sample['summary'],category)
    return review