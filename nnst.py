import numpy as np
import pandas as pd
import nnst_utils.params as par
import pprint
import random

def load_data(csv_path):
    dataframe = pd.read_csv(csv_path)
    return np.array(
        [(dataframe['text'][i],par.category[dataframe['class'][i]] - 100) for i in range(len(dataframe))]
    )

def random_batch(dataset, batch_size):
    range_list = np.array(range(len(dataset)))
    train_index = random.sample(range_list.tolist(), k=batch_size)

    mask_index = np.ones([len(dataset)])
    mask_index[train_index] = 0

    test_index = range_list[mask_index == 1].tolist()
    return (dataset[train_index], dataset[test_index])



if __name__ == '__main__':
    data = load_data('csv/NNST_data.csv')
    pprint.pprint(random_batch(data,5000))

