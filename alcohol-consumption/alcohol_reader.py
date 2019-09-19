import os
import csv
import collections
from typing import List

data= []

Record = collections.namedtuple(
    'Record', 
    'country, beer_servings, spirit_servings, wine_servings, total_litres_of_pure_alcohol'
)

def init():
    base_dir = os.path.dirname(__file__)
    file_name= os.path.join(base_dir, 'data', 'drinks.csv')
    
    with open(file_name, 'r', encoding='utf-8') as fin:
        reader= csv.DictReader(fin)
        data.clear()

        for row in reader:
            record= parse_row(row)
            data.append(record)

def parse_row(row):
    row['country']= row['country']
    row['beer_servings'] = int(row['beer_servings'])
    row['spirit_servings']= int(row['spirit_servings'])
    row['wine_servings']= int(row['wine_servings'])
    row['total_litres_of_pure_alcohol']= float(row['total_litres_of_pure_alcohol'])

    record= Record(
        **row
    )

    return record

def top_beer_drinkers() -> List[Record]:
    #print('top 10 drinkng nations')
    return sorted(data, key= lambda r: -r.beer_servings)


def lowest_beer_drinkers() -> List[Record]:
    return sorted(data, key= lambda r: r.beer_servings)