from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import date, timedelta
import urllib.request as req
import re
import nnst.nnst_utils.params as par

category = par.category
base_url = 'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId={}&date={}'


def download(data_per_category: int, csv_path: str, last_date: str = '20180918'):

    opener = req.build_opener()
    dataset = []
    progress = 0
    for keyword in category:
        date = last_date
        spare = data_per_category
        while spare > 0:
            date = __date_decrease__(date)
            #print(date)
            f = opener.open(base_url.format(category[keyword],date))
            #print(f.read)
            soup = BeautifulSoup(f, 'html.parser')
            li = soup.select("ol[class='ranking_list'] > li > div >  a")
            # print('data set count: {}'.format(len(li)))

            if spare < 30:
                dataset += [{'class': keyword, 'text': __clean_text__(t['title'])} for t in li][:spare]
                print('[Status] ----- category {} download complete -----'.format(keyword))
            else:
                dataset += [{'class':keyword, 'text': __clean_text__(t['title'])} for t in li]

            try:
                progress = (100 / (data_per_category * 6) * len(dataset))
            except:
                pass

            dataframe = pd.DataFrame(dataset)
            dataframe.to_csv(csv_path,index=False)
            if spare // 100 == 1:
                print('[Progress] {} % download complete'.format(progress))
            spare -= len(li)


    print('[Success] All download was complete')

def __date_decrease__(news_date : str):
    t = time.strptime(news_date, '%Y%m%d')
    newdate = date(t.tm_year, t.tm_mon, t.tm_mday) - timedelta(1)
    return newdate.strftime('%Y%m%d')

def __clean_text__(text):
    #cleaned_text = re.sub('[a-zA-Z]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
                          ' ', text)
    return cleaned_text



if __name__ =='__main__':
    download(1000,'csv/NNST_data.csv','20180914')