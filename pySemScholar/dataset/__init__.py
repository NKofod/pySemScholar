import requests 
import json 
from pySemScholar.utils import assemble_query_fields

DATASETS_API_REF = "https://api.semanticscholar.org/datasets/v1/"

def datasetReleases(api_key:str = None ) -> list[str]:
    """ 
    Provides a wrapper for the Semantic Scholar Datasets API Releases endpoint 

    Input: \n
    api_key: A string containing a key for the Semantic Scholar API 

    Output: \n
    A list of strings containing release names 
    """
    # Construct the query  
    query = DATASETS_API_REF + "release/"

    # Make the request to the endpoint 
    if api_key:
        request = requests.get(query,headers={'x-api-key':api_key})
    else: 
        request = requests.get(query)

    # Check status code and create output 
    if request.status_code == 200: 
        request_content = request.content 
        request_json = json.loads(request_content)
    else: 
        request_content = request.content 
        request_json = json.loads(str(request_content))
        raise ConnectionError(f"{request_json['error']}")
    return request_json 

def datasetsInRelease(release_id:str=None,
                        api_key:str = None) -> dict: 
    """ 
    Provides a wrapper for the Semantic Scholar Datasets API Datasets in Release endpoint 

    Input: \n
    release_id: A string containing the release id. \n
    api_key: A string containing a key for the Semantic Scholar API \n

    Output: \n
    A dictionary containing the response from the endpoint. See https://api.semanticscholar.org/api-docs/datasets#operation/get_release for details. 
    """

    # Construct the query 
    query = DATASETS_API_REF + "release/" + release_id 

    # Make the request to the endpoint 
    if api_key:
        request = requests.get(query,headers={'x-api-key':api_key})
    else: 
        request = requests.get(query)

    # Check status code and create output 
    if request.status_code == 200: 
        request_content = request.content 
        request_json = json.loads(request_content)
    else: 
        request_content = request.content 
        request_json = json.loads(str(request_content))
        raise ConnectionError(f"{request_json['error']}")
    return request_json 

def datasetLinks(dataset_name: str = None,
                release_id: str = None, 
                api_key: str = None) -> dict: 
    """ 
    Provides a wrapper for the Semantic Scholar Datasets API Links for Dataset endpoint 

    Input: 
    dataset_name: A string containing the name of the dataset 
    release_id: A string containing the release id. 
    api_key: A string containing a key for the Semantic Scholar API 

    Output: 
    A dictionary containing the response from the endpoint. See https://api.semanticscholar.org/api-docs/datasets#operation/get_release for details. 
    """
    # Construct the query 
    query = DATASETS_API_REF + "release/" + release_id + "/dataset/" + dataset_name
    
    # Make the request to the endpoint 
    if api_key:
        request = requests.get(query,headers={'x-api-key':api_key})
    else: 
        request = requests.get(query)
    
    # Check status code and create output 
    if request.status_code == 200: 
        request_content = request.content 
        request_json = json.loads(str(request_content))
    else: 
        request_content = request.content 
        request_json = json.loads(str(request_content))
        raise ConnectionError(f"{request_json['error']}")

    return request_json 