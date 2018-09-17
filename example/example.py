import sys
import os
sys.path.append(os.path.abspath("./"))
from nnst import downloader as downloader
import pprint
import argparse
import nnst.nnst as nnst

parser=argparse.ArgumentParser()

parser.add_argument('--csv_path', help='csv파일 경로')
parser.add_argument('--date', help='시작할 뉴스 일자')
parser.add_argument('--num', help='파싱할 뉴스 개수')
parser.add_argument('--num_train', help='트레이닝셋 사이즈')

csv_path = 'csv/NNST_data.csv'
date = '20180914'
num = 1000
num_train = 900

print(parser.format_help())
args = parser.parse_args().__dict__

if args['csv_path'] is not None:
    csv_path = str(args['csv_path'])
if args['date'] is not None:
    date = str(args['date'])
if args['num'] is not None:
    num = int(args['num'])
if args['num_train'] is not None:
    num_train = int(args['num_train'])

downloader.download(num, csv_path, date)
data = nnst.load_data(csv_path)

train, test = nnst.div_dataset(data, train_size=num_train)

print('------train set------')
pprint.pprint(train)
print('---------------------\n')
print('------test  set------')
pprint.pprint(test)
print('---------------------\n')

batch = nnst.random_batch(train,batch_size=100)
print('------batch set------')
pprint.pprint(batch)
print('---------------------')

