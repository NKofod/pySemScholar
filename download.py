import pySemScholar as Search 
import json 

with open("api_key.txt", "r") as infile:
    API_KEY = infile.read()

tmp = Search.dataset.datasetReleases()
tmp = json.loads(tmp)
print(tmp)



tmp_two = Search.dataset.datasetsInRelease(str(tmp[-1]),api_key=API_KEY)

for dataset in tmp_two['datasets']:
    if dataset['name'] == "papers":
        print(dataset)
