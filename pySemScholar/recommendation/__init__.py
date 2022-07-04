import requests 
import json 
from pySemScholar.utils import assemble_query_fields

RECOMMENDER_API_REF = "https://api.semanticscholar.org/recommender/v1/"


def paperRecommenderMulti(positivePaperIds: list = [], 
                        negativePaperIds: list = [], 
                        limit: int = 100,
                        fields: str = 'Basic',
                        custom_fields: list = None, 
                        api_key: str = None) -> list[dict]:

    """
    Provides a wrapper for the Semantic Scholar Recommendations API's paper recommendations endpoint. 

    Inputs: \n
    positivePaperIds: A list containing positive paper ids \n
    negativePaperIds: A list containing negative paper ids \n
    limit: An int containing the number of results per call to the API's endpoint. \n
    fields: One of either 'Basic', 'Extended', 'All' or 'Custom'. Basic contains 'paperId', 'title', 'abstract', 'year', 'journal' and 'authors'. Extended contains all of the above, as well as 'externalIds', 'url', 'referenceCount' and 'citationCount'. All contains all possible fields. Custom allows for the use of the custom_fields parameter to specify a custom list of fields to be included in the output. \n
    custom_fields: A list of strings containing the names of fields to be included. For a full list of fields, see https://api.semanticscholar.org/api-docs/graph. \n
    api_key: A string containing an api_key for the Semantic Scholar API \n
    
    Outputs: \n
    A list of dictionaries containing the results. 
    """
    # Check for input integrity 
    if not isinstance(positivePaperIds,list):
        raise TypeError('positivePaperIds parameter must be of type list.')
    if not isinstance(negativePaperIds,list):
        raise TypeError('negativePaperIds parameter must be of type list.')
    if not isinstance(custom_fields, (bool,list)):
        raise TypeError('"custom_fields" parameter must be of type list or type bool.')
    if not isinstance(api_key, (bool,str)):
        raise TypeError('"api_key" parameter must be of type str or type bool')
    if fields == 'Custom' and not isinstance(custom_fields,list): 
        raise TypeError('"custom_fields" parameter must be of type list when using the "Custom" option for "fields".')
    if not isinstance(limit, int): 
        raise TypeError('"limit" parameter must be of type int.')
    
    # Instantiate json payload 
    payload = {
        'positivePaperIds': positivePaperIds,
        'negativePaperIds': negativePaperIds
    }

    # Construct base query for the endpoint
    base_query = 'papers/'

    # Assemble query fields to a string for use in request 
    query_fields = assemble_query_fields(fields,custom_fields,'Paper')
    
    # Construct the final query 
    final_query = RECOMMENDER_API_REF + base_query + query_fields 
    
    # Add limit to the query if limit is not equal to 100
    if limit != 100:
        final_query += f"&limit={limit}"
    
    # Make the request to the endpoint 
    if api_key: 
        request = requests.post(final_query, data = payload, headers={'x-api-key':api_key})
    else: 
        request = requests.post(final_query, data = payload)
    
    # Check status code on the request and generate output 
    if request.status_code == 200: 
        request_content = request.content 
        request_json = json.loads(str(request_content))
    else: 
        request_content = request.content 
        request_json = json.loads(str(request_content))
        raise ConnectionError(f"{request_json['error']}")

    return request_json['recommendedPapers']


def paperRecommenderSingle(paperId:str, 
                            limit: int = 100,
                            fields: str = 'Basic',
                            custom_fields: list = None, 
                            api_key: str = None) -> list[dict]: 
    """
    Provides a wrapper for the Semantic Scholar Recommendations API's paper recommendations endpoint. 

    Inputs: \n
    paperId: A string containing the paper id \n
    limit: An int containing the number of results per call to the API's endpoint. \n
    fields: One of either 'Basic', 'Extended', 'All' or 'Custom'. Basic contains 'paperId', 'title', 'abstract', 'year', 'journal' and 'authors'. Extended contains all of the above, as well as 'externalIds', 'url', 'referenceCount' and 'citationCount'. All contains all possible fields. Custom allows for the use of the custom_fields parameter to specify a custom list of fields to be included in the output. \n
    custom_fields: A list of strings containing the names of fields to be included. For a full list of fields, see https://api.semanticscholar.org/api-docs/graph. \n
    api_key: A string containing an api_key for the Semantic Scholar API \n
    
    Outputs: \n
    A list of dictionaries containing the results. 
    """
    # Check for input integrity 
    if not isinstance(paperId,str):
        raise TypeError('paperId parameter must be of type str')
    if not isinstance(custom_fields, (bool,list)):
        raise TypeError('"custom_fields" parameter must be of type list or type bool.')
    if not isinstance(api_key, (bool,str)):
        raise TypeError('"api_key" parameter must be of type str or type bool')
    if fields == 'Custom' and not isinstance(custom_fields,list): 
        raise TypeError('"custom_fields" parameter must be of type list when using the "Custom" option for "fields".')
    if not isinstance(limit, int): 
        raise TypeError('"limit" parameter must be of type int.')

    # Construct base query for the endpoint with the 
    # given paper ID 
    base_query = f'papers/forpaper/{paperId}?'

    # Assemble query fields to a string for use in request 
    query_fields = assemble_query_fields(fields,custom_fields,'Paper')

    # Construct the final query 
    final_query = RECOMMENDER_API_REF + base_query + query_fields 

    # Add limit to the query if limit is not equal to 100, as 
    # 100 is the standard for the endpoint in question. 
    if limit != 100:
        final_query += f"&limit={limit}"
    
    # Make the request to the endpoint 
    if api_key: 
        request = requests.get(final_query, headers={'x-api-key':api_key})
    else: 
        request = requests.get(final_query)
    
    # Check status code on the request and generate output 
    if request.status_code == 200: 
        request_content = request.content 
        request_json = json.loads(str(request_content))
    else: 
        request_content = request.content 
        request_json = json.loads(str(request_content))
        raise ConnectionError(f"{request_json['error']}")
    return request_json['recommendedPapers']