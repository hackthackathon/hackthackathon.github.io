import requests
import csv
from datetime import datetime

ACCESS_TOKEN = ''
headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}

def add_to_csv(resource, current_papers):
    print(current_papers['title'])
    if resource['title'] not in current_papers['title']:
        with open('resources.csv', 'a', newline='') as csvfile:
            fieldnames = ['timestamp', 'added_by', 'author', 'title','type', 'where']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(resource)


with open('resources_2.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    csv_headers = next(reader)
    # transpose the data
    # --> columns become rows and rows become columns
    csv_data = zip(*reader)
    # create a dictionary by combining the headers with the data
    d = dict(zip(csv_headers, csv_data))
    print(d)

resources = []
# retrieving information from Zenodo
r = requests.get('https://zenodo.org/api/records', params={'communities': 'hack_the_hackathon'}, headers=headers)
print(r.status_code)
hits = r.json()['hits']
for response in hits['hits']:
    title = response['title']
    print(title)
    if title not in d['title']:
            authors = response['metadata']['creators']
            names = []
            size = len(authors)
            if size > 1:
                for author in authors: 
                    first_name = author['name'].split(',')
                    names.append(first_name[0] + ', ' + first_name[1][1]+ '.') 
                    if size > 1:
                        names.append(', ')
                    if size == 2:
                        names.append('& ')
                    size = size-1
            else: 
                first_name = author['name'].split(',')
                names.append(first_name[0] + ', ' + first_name[1][1] + '.') 
            author_names = ''.join(names)
            print(author_names)
            if 'resource_type' in response['metadata']:
                resource_type = response['metadata']['resource_type']['title']
            if resource_type is not None: 
                type = f'HtH, {resource_type}'
            else:
                type = 'HtH'
            link = response['doi_url']
            resource = {'timestamp': datetime.now(), 'added_by': 'zenodo_script', 'author': author_names, 'title': title, 'type': type, 'where': link}
            resources.append(resource)

print(resources)
for x in resources:
    with open('resources.csv', 'a+', newline='') as csvfile:
        fieldnames = ['timestamp', 'added_by', 'author', 'title','type', 'where']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(x)
