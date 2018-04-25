from src.utils.utils import get_file_names, get_file_path
import matplotlib.pyplot as plt

def main():
    file = open(get_file_path("explained_nouns.txt"), "r")
    total = 0.0
    data = list()
    data_y = list()
    i = 1
    for num in file.read().split():
        total = float(num) + total
        data.append(total)
        data_y.append(i)
        i+=1
    plt.plot( data, data_y)
    plt.ylabel('Number of Components')
    plt.xlabel('Explained Variance')
    plt.title('Bag Of Nouns SVD Components Explained Variance')
    plt.show()

if __name__ == '__main__':
    main()