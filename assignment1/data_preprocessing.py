import json
import os
import re
import csv

dataSetFilenames = [
    'recipes_raw_nosource_ar.json',
    'recipes_raw_nosource_epi.json',
    'recipes_raw_nosource_fn.json',
]

def replaceLinebreaks(text):
    return text.replace('\n', '<LINEBREAK>')


def main():

    with open('preprocessed_data.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter='|',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])

        csvwriter.writerow(['title', 'ingredients', 'instructions', 'hasPicture'])

        for datasetName in dataSetFilenames:
            dirname = os.path.dirname(__file__)
            filename = os.path.join(dirname, './data/' + datasetName)
            data = json.loads(open(filename).read())

            # data contains some kind of hash as the top level entry, which we dont need

            for entry in data.values():
                if len(entry) == 0 or entry['instructions'] == None:
                    continue
                row = [entry['title'], '<LISTELEMENT>'.join(entry['ingredients']), entry['instructions'],  str(bool(entry['picture_link'] != 'null'))]
                row = map(replaceLinebreaks, row)
                csvwriter.writerow(row)

                
if __name__ == "__main__":
    main()

    