import pySemScholar as Search 
import requests
from rich.progress import Progress

with open("api_key.txt", "r") as infile:
    API_KEY = infile.read()
    
tmp = Search.dataset.datasetReleases(API_KEY)

tmp_datasets = Search.dataset.datasetsInRelease(tmp[-1],API_KEY)
datasets = []
for i in tmp_datasets['datasets']:
    datasets.append(i['name'])
files = 0
for dataset in datasets: 
    tmp_links = Search.dataset.datasetLinks(dataset,tmp[-1],API_KEY)
    files += len(tmp_links['files'])
    


with Progress() as progress:
    task_0 = progress.add_task("[red]Datasets",total=files)
    for dataset in datasets: 
        tmp_links = Search.dataset.datasetLinks(dataset,tmp[-1],API_KEY)
        task_1 = progress.add_task(f"[green]{dataset}",total=len(tmp_links['files']))
        for link in enumerate(tmp_links['files']):
            request = requests.get(link[1],stream=True)
            length = request.headers['content-length']
            task_2 = progress.add_task(f"[blue]{dataset}_{link[0]}",total=int(length)/32)
            with open(f"./data/{dataset}_{link[0]}.gz","wb") as outfile:
                for chunk in request.iter_content(chunk_size=32):
                    outfile.write(chunk)
                    progress.advance(task_2,1)
            progress.finished(task_2)
            progress.advance(task_1,1)
            progress.advance(task_0,1)
            