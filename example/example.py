import sys
import os
sys.path.append(os.path.abspath("./"))
import downloader as downloader


downloader.download(1000,'csv/NNST_data.csv','20180914')