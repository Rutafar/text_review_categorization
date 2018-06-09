from features.explore import bag_of_words, tf_idf, bigrm, only_nouns
from src.data.import_dataset import import_cleaned_training_set
from visualization.visualize import display_features
from features.normalize import lemmatize, letters_only, lower_only, remove_contractions, remove_stopwords
from src.utils.utils import  get_file_path
from nltk.corpus import stopwords


print(type(stopwords.words('English')))
with open(get_file_path("stopwords.txt"), "w") as file:
    for word in stopwords.words('English'):
        file.write("%s\n" % word)