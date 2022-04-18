import re

import pandas as pd
import csv


def csv_reader(file):
    reader = csv.reader(file)
    phone = []
    email = []
    site = []
    data = {
        'phone number': phone,
        'email adress': email,
                 'website': site}
    for row in reader:

        for item in row:

            if re.search(r'380[0-9]{9}', item) and re.search(r'\w+\.*\w+@\w+\.\w+', item):
                phon = re.search(r'380[0-9]{9}', item).group()
                emai = re.search(r'\w+\.*\w+@\w+\.\w+', item).group()
                si = re.search(
                    r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:]))',
                    item)

                if si:
                    sit = si.group()
                else:
                    sit = 'None'
                phone.append(phon)
                email.append(emai)
                site.append(sit)

            else:
                continue
        frame = pd.DataFrame(data=data)

        frame.to_csv(r'python-talent-acquisition/dataset_sorted.csv', index=False)


if __name__ == '__main__':
    with open(file=r'python-talent-acquisition/dataset.csv', mode='r', encoding='utf-8') as file:
        csv_reader(file)
