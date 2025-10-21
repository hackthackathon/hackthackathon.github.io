import requests
from datetime import datetime
import csv

headers = {'Zotero-API-Version': '3',}
# Zotero Awesome Hackathon List ID
GROUP_ID = '5538025'
resources = []
titles = []

r = requests.get(f'https://api.zotero.org/groups/{GROUP_ID}/items', params={'limit': '100'}, headers=headers)
with open('../files/docs/resources.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    csv_headers = next(reader)
    # transpose the data
    # --> columns become rows and rows become columns
    csv_data = zip(*reader)
    # create a dictionary by combining the headers with the data
    d = dict(zip(csv_headers, csv_data))

responses = r.json()
for response in responses:
    data = response['data']
    if 'title' in data:
        title = data['title']
    else:
        continue
    if title in d['title']:
        continue
    if title in titles:
        continue
    titles.append(title)
    if 'creatorSummary' in response['meta']:
        authors = response['meta']['creatorSummary']
    else:
        continue
    resource = ''
    if 'url' in data:
        resource = data['url']
    else:
        if 'DOI' in data:
            resource = data['DOI']
    type = 'Other'
    if data['itemType'] == 'journalArticle':
        type = 'Journal'
    if data['itemType'] == 'book':
        type = 'Book'
    added_by = response['meta']['createdByUser']['name']
    resource = {'timestamp': datetime.now(), 'added_by': added_by, 'author': authors, 'title': title, 'type': type, 'where': resource}
    resources.append(resource)

with open('../files/docs/resources.csv', 'a+', newline='') as csvfile:
    csvfile.write('\n')
    fieldnames = ['timestamp', 'added_by', 'author', 'title','type', 'where']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for x in resources:
        writer.writerow(x)