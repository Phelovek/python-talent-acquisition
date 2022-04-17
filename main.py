import re

import pandas as pd
import csv


def csv_reader(file):

    reader = csv.reader(file)

    for row in reader:

        for item in row:

            if re.search(r'380[0-9]{9}', item) and re.search(r'\w+\.*\w+@\w+\.\w+', item):
                phone = re.search(r'380[0-9]{9}', item).group()
                email = re.search(r'\w+\.*\w+@\w+\.\w+', item).group()
                sit = re.search(r'www/[A-Za-z]/[a-z]', item)

                if sit:
                    site = sit.group()
                else:
                    site = 'None'
                data1 = {
                    'phone number': phone,
                    'email adress': email,
                    'website': site}

                frame = pd.DataFrame(data=data1, index=[0])

                frame.to_csv(r'python-talent-acquisition/dataset1.csv', mode='a', index=False)


if __name__ == '__main__':
    with open(file=r'python-talent-acquisition/dataset.csv', mode='r', encoding='utf-8') as data:
        csv_reader(data)
