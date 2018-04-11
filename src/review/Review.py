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

    def __init__(self, reviewerID, productID, reviewerName, helpful, reviewText, overall, summary):
        self.reviewerID = reviewerID
        self.productID = productID
        self.reviewerName = reviewerName
        self.helpful = helpful
        self.reviewText = reviewText
        self.overall = overall
        self.summary = summary


def create_review_from_sample(sample):
    review = Review(sample['reviewerID'], sample['asin'], sample['reviewerName'], sample['helpful'], sample['reviewText'], sample['overall'], sample['summary'])
    return review