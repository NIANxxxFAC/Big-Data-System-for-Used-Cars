# Mar 7, 2021 created by Sun, Tuo
# get car ids from cars.com.
# split ids with '-'
# python3.8 src/get_car_url_list.py --zipcode 92101 --radius 50
#######################################

from bs4 import BeautifulSoup
import os
import requests
import json
import argparse

def already_found(zipcode, one_year):
    path = "car_url"  # 文件夹目录
    files = os.listdir(path)
    return "{zc}car_url_list_{year}.txt".format(zc=args.zipcode, year=one_year) in files


def get_url_list_year(year):
    """
    TODO(tuosun): we should create txt first and save them periodically instead of saving it in one time
    :param year: the year for spider
    :return: save a txt file including all car ids for one year.
    """
    Ids_list = list()
    for color in colors:
        for i in range(1, 51):
            base_curr = base.format(color=color,
                                    page_num=i,
                                    year_id=years[year],
                                    radius=args.radius,
                                    zipcode=args.zipcode)
            response = requests.get(base_curr, headers=headers, timeout=30).content
            soup = BeautifulSoup(response, 'html.parser', from_encoding='utf-8')
            container = soup.find_all(class_='shop-srp-listings__listing-container')
            Ids = list()
            _ = [Ids.append(div.a.get('data-goto-vdp')) for div in container if div.a.get('data-goto-vdp')]
            if not Ids:
                break
            Ids_list += Ids
        else:
            print("\033[31;1mSearching result is out of range:\033[0m", year, color)
    else:
        print(year, ':', len(Ids_list))
    with open("car_url/{zc}car_url_list_{year}.txt".format(zc=args.zipcode, year=year), 'w+') as f:
        f.write('-'.join(Ids_list))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--zipcode', nargs='?', const=1, type=int, default=90013)
    parser.add_argument('--radius', nargs='?', const=1, type=int, default=20)
    args = parser.parse_args()

    # TODO(tuosun): use more user agent.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/'
                      '605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    }
    base = 'https://www.cars.com/for-sale/searchresults.action/' \
           '?clrId={color}&page={page_num}&perPage=100&rd={radius}' \
           '&searchSource=GN_REFINEMENT&sort=relevance&stkTypId=28881&yrId={year_id}&zc={zipcode}'

    # cars.com limits the maximum number of searching results.
    # we can use colors and years to distribute searching results
    years = json.load(open('src/years.json'))
    colors = ['27122',
              '27123',
              '27124',
              '27125',
              '27126',
              '27127',
              '27128',
              '27129',
              '27130',
              '27132',
              '27133',
              '27131',
              '27134',
              '27135',
              '29637'
              ]
    for i in years:
        if already_found(args.zipcode, i):
            print(args.zipcode, i, 'already found')
            continue
        get_url_list_year(i)