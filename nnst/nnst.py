import numpy as np
import pandas as pd
import nnst.nnst_utils.params as par
import pprint
import random

def load_data(csv_path):
    dataframe = pd.read_csv(csv_path)
    return np.array(
        [(dataframe['text'][i],par.category[dataframe['class'][i]] - 100) for i in range(len(dataframe))]
    )

def div_dataset(dataset, train_size):
    range_list = np.array(range(len(dataset)))
    train_index = random.sample(range_list.tolist(), k=train_size)

    mask_index = np.ones([len(dataset)])
    mask_index[train_index] = 0

    test_index = range_list[mask_index == 1].tolist()
    return (dataset[train_index], dataset[test_index])

def random_batch(dataset, batch_size):
    batch_data = []
    for i in range(len(dataset)//batch_size):
        range_list = np.array(range(len(dataset)))
        train_index = random.sample(range_list.tolist(), k=batch_size)
        batch_data.append(dataset[train_index])

    return np.array(batch_data)

if __name__ == '__main__':
    data = load_data('csv/NNST_data.csv')
    data =div_dataset(data,200)
    pprint.pprint(random_batch(data[0],20))

