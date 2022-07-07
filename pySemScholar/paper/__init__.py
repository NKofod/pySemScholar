import requests 
import json 
from pySemScholar.utils import assemble_query_fields

GRAPH_API_REF = "https://api.semanticscholar.org/graph/v1/"

def paperSearch(query:str ="",   
                    limit: int=100,
                    offset: int =0,
                    fields: str ='Basic',
                    custom_fields: list =False,
                    api_key: str =False,
                    paginate=False) -> list[dict]: 
    """
    Provides a wrapper for the Semantic Scholar Graph API's paper search endpoint. 

    Inputs: \n
    query: A string containing the keywords being searched for \n
    limit: An int containing the number of results per call to the API's endpoint. \n
    offset: An int containing the number of results to skip. \n
    fields: One of either 'Basic', 'Extended', 'All' or 'Custom'. Basic contains 'paperId', 'title', 'abstract', 'publicationDate', 'journal' and 'authors'. Extended containts all of the above, as well as 'externalIds', 'url', 'venue', 'year', 'publicationType' and 'publicationDate'. All contains all possible fields. Custom allows for the use of the custom_fields parameter to specify a custom list of fields to be included in the output. \n
    custom_fields: A list of strings containing the names of fields to be included. For a full list of fields, see https://api.semanticscholar.org/api-docs/graph. \n
    paginate: A boolean describing whether to get more than the first page of results.  \n
    api_key: A string containing an api_key for the Semantic Scholar API \n

    Outputs: 
    A list of dictionaries containing the results. 
    """
    # Check for input integrity 
    if fields not in ['Basic', 'Extended','All','Custom']: 
        raise ValueError('"fields" parameter must be either "Basic", "Extended", "All" or "Custom"')
    if not isinstance(limit, int): 
        raise TypeError('"limit" parameter must be of type int.')
    if not isinstance(paginate, bool):
        raise TypeError('"paginate" parameter must of type bool.')
    if not isinstance(offset, int): 
        raise TypeError('"offset" parameter must be of type int.')
    if not isinstance(query,str):
        raise TypeError('"name" parameter must be of type str.')
    if not isinstance(custom_fields, (bool,list)):
        raise TypeError('"custom_fields" parameter must be of type list or type bool.')
    if not isinstance(api_key, (bool,str)):
        raise TypeError('"api_key" parameter must be of type str or type bool')
    if fields == 'Custom' and not isinstance(custom_fields,list): 
        raise TypeError('"custom_fields" parameter must be of type list when using the "Custom" option for "fields".')

    # Convert the search phrase to lowercase, strip extraneous 
    # whitespace and split based on spaces 
    keywords = query.lower().strip().split(' ')

    # Construct the base query from the endpoint in use plus 
    # the name joined with +'s. 
    base_query = f'paper/search?query={"+".join(keywords)}' 
    
    # Assemble query fields to a string for use in request 
    query_fields = assemble_query_fields(fields,custom_fields,'Paper')

    # Construct the final query prior to adding limits and onset 
    final_query = GRAPH_API_REF + base_query + "&fields=" + query_fields


    # Add limit to the query if limit is not equal to 100, as 
    # 100 is the standard for the endpoint in question. 
    if limit != 100:
        final_query += f"&limit={limit}"
    
    # Add offset to the query, if offset is not equal to 0, as 
    # 0 is the standard for the endpoint in question. 
    if offset != 0: 
        final_query += f"&offset={offset}"

    # Fetch the data from the Semantic Scholar API 
    if api_key: 
        request = requests.get(final_query,headers={'x-api-key':api_key})
    else: 
        request = requests.get(final_query)

    # Check to see if the request came through succesfully 
    # If so, extract the contents into a dictionary 
    # If not, extract the error message and raise a 
    # ConnectionError with the error message 
    if request.status_code == 200: 
        request_content = request.content 
        request_json = json.loads(request_content)
    else: 
        request_content = request.content 
        request_json = json.loads(request_content)
        raise ConnectionError(f"{request_json['error']}")
    
    # Extract the results from from the requestion into a list 
    results = list(request_json['data'])
    
    next_offset = request_json['next']
    past_offset = 0 

    # If paginate, then iterate over requests and generate output 
    if paginate:
        while request_json['next'] <= 10000 - limit and past_offset != next_offset: 
            past_offset = next_offset 
            if offset != 0: 
                query = final_query[:-len(str(offset))] + str(next_offset)
            else: 
                query = final_query + "&offset" + str(next_offset)
            if api_key: 
                request = requests.get(final_query,headers={'x-api-key':api_key})
            else: 
                request = requests.get(query)
            if request.status_code == 200: 
                request_content = request.content 
                request_json = json.loads(request_content)
            else: 
                request_content = request.content 
                request_json = json.loads(request_content)
                raise ConnectionError(f"{request_json['error']}")
            results.extend(request_json['data'])
            print(request_json['next'])
            next_offset = request_json['next']

    return results 


def paperDetails(paper_id:str ="",   
                    fields: str ='Basic',
                    custom_fields: list =False,
                    api_key: str =False) -> dict: 
    """
    Provides a wrapper for the Semantic Scholar Graph API's paper details endpoint. 

    Inputs: \n
    paper_id: A string containing the paper_id  \n
    fields: One of either 'Basic', 'Extended', 'All' or 'Custom'. Basic contains 'authorId', 'name', 'affiliations' and 'url'. Extended contains all of the above as well as 'homepage', 'hIndex' and 'aliases'. All contains all possible fields. Custom allows for the use of the custom_fields parameter to specify a custom list of fields to be included in the output. \n
    custom_fields: A list of strings containing the names of fields to be included. For a full list of fields, see https://api.semanticscholar.org/api-docs/graph. \n
    api_key: A string containing an api_key for the Semantic Scholar API \n

    Outputs: \n
    A dictionary containing the results. 
    """

    # Check for input integrity 
    if fields not in ['Basic', 'Extended','All','Custom']: 
        raise ValueError('"fields" parameter must be either "Basic", "Extended", "All" or "Custom"')
    if not isinstance(paper_id,str): 
        raise TypeError('author_id must be of type list.')
    if not isinstance(custom_fields, (bool,list)):
        raise TypeError('"custom_fields" parameter must be of type list or type bool.')
    if not isinstance(api_key, (bool,str)):
        raise TypeError('"api_key" parameter must be of type str or type bool')
    if fields == 'Custom' and not isinstance(custom_fields,list): 
        raise TypeError('"custom_fields" parameter must be of type list when using the "Custom" option for "fields".')

    # Construct base query for the endpoint with the 
    # given paper ID 
    base_query = f'paper/{paper_id}?'

    # Assemble query fields to a string for use in request 
    query_fields = assemble_query_fields(fields,custom_fields,'Paper')

    # Construct the final query 
    final_query = GRAPH_API_REF + base_query + "&fields=" + query_fields

    # Make the request to the endpoint 
    if api_key: 
        request = requests.get(final_query,headers={'x-api-key':api_key})
    else: 
        request = requests.get(final_query)

    # Check status code on the request and generate output 
    if request.status_code == 200: 
        request_content = request.content 
        request_json = json.loads(request_content)
    else: 
        request_content = request.content 
        request_json = json.loads(request_content)
        raise ConnectionError(f"{request_json['error']}")
    return request_json

def paperAuthors(paper_id:str ="",   
                    fields: str ='Basic',
                    custom_fields: list =False,
                    api_key: str =False,
                    paginate=False,
                    limit: int=100,
                    offset: int =0) -> list[dict]: 
    """
    Provides a wrapper for the Semantic Scholar Graph API's paper authors endpoint. 

    Inputs: \n
    paper_id: A string containing the paper_id\n
    limit: An int containing the number of results per call to the API's endpoint. \n
    offset: An int containing the number of results to skip. \n
    fields: One of either 'Basic', 'Extended', 'All' or 'Custom'. Basic contains 'authorId', 'name', 'affiliations' and 'url'. Extended contains all of the above as well as 'homepage', 'hIndex' and 'aliases'. All contains all possible fields. Custom allows for the use of the custom_fields parameter to specify a custom list of fields to be included in the output. \n
    custom_fields: A list of strings containing the names of fields to be included. For a full list of fields, see https://api.semanticscholar.org/api-docs/graph. \n
    paginate: A boolean describing whether to get more than the first page of results.  \n
    api_key: A string containing an api_key for the Semantic Scholar API \n
    
    Outputs: \n
    A list of dictionaries containing the results. 
    """

    # Check for input integrity 
    if fields not in ['Basic', 'Extended','All','Custom']: 
        raise ValueError('"fields" parameter must be either "Basic", "Extended", "All" or "Custom"')
    if not isinstance(paper_id,str): 
        raise TypeError('author_id must be of type list.')
    if not isinstance(custom_fields, (bool,list)):
        raise TypeError('"custom_fields" parameter must be of type list or type bool.')
    if not isinstance(api_key, (bool,str)):
        raise TypeError('"api_key" parameter must be of type str or type bool')
    if fields == 'Custom' and not isinstance(custom_fields,list): 
        raise TypeError('"custom_fields" parameter must be of type list when using the "Custom" option for "fields".')
    if not isinstance(limit, int): 
        raise TypeError('"limit" parameter must be of type int.')
    if not isinstance(paginate, bool):
        raise TypeError('"paginate" parameter must of type bool.')
    if not isinstance(offset, int): 
        raise TypeError('"offset" parameter must be of type int.')

    # Construct base query for the endpoint with the 
    # given paper ID 
    base_query = f'paper/{paper_id}/authors?'

    # Assemble query fields to a string for use in request 
    query_fields = assemble_query_fields(fields,custom_fields,'Author')

    # Construct the final query 
    final_query = GRAPH_API_REF + base_query + "&fields=" + query_fields

    # Add limit to the query if limit is not equal to 100, as 
    # 100 is the standard for the endpoint in question. 
    if limit != 100:
        final_query += f"&limit={limit}"
    
    # Add offset to the query, if offset is not equal to 0, as 
    # 0 is the standard for the endpoint in question. 
    if offset != 0: 
        final_query += f"&offset={offset}"
    
    # Make the request to the endpoint 
    if api_key: 
        request = requests.get(final_query,headers={'x-api-key':api_key})
    else: 
        request = requests.get(final_query)
    
    # Check status code on the request and generate output 
    if request.status_code == 200: 
        request_content = request.content 
        request_json = json.loads(request_content)
    else: 
        request_content = request.content 
        request_json = json.loads(request_content)
        raise ConnectionError(f"{request_json['error']}")

    results = list(request_json['data'])

    next_offset = request_json['next']
    past_offset = 0 
    # If paginate, then iterate over requests and generate output 
    if paginate:
        while request_json['next'] <= 10000 - limit and past_offset != next_offset: 
            past_offset = next_offset 
            if offset != 0: 
                query = final_query[:-len(str(offset))] + str(next_offset)
            else: 
                query = final_query + "&offset" + str(next_offset)
            if api_key: 
                request = requests.get(final_query,headers={'x-api-key':api_key})
            else: 
                request = requests.get(query)
            if request.status_code == 200: 
                request_content = request.content 
                request_json = json.loads(request_content)
            else: 
                request_content = request.content 
                request_json = json.loads(request_content)
                raise ConnectionError(f"{request_json['error']}")
            results.extend(request_json['data'])
            print(request_json['next'])
            next_offset = request_json['next']
    return results 


def paperCitations(paper_id:str ="",   
                    fields: str ='Basic',
                    custom_fields: list =False,
                    api_key: str =False,
                    paginate=False,
                    limit: int=100,
                    offset: int =0) -> list[dict]:
    """
    Provides a wrapper for the Semantic Scholar Graph API's paper citations endpoint. 

    Inputs: \n
    paper_id: A string containing the paper_id \n
    limit: An int containing the number of results per call to the API's endpoint. \n
    offset: An int containing the number of results to skip. \n
    fields: One of either 'Basic', 'Extended', 'All' or 'Custom'. Basic contains 'paperId', 'title', 'abstract', 'year', 'journal' and 'authors'. Extended contains all of the above, as well as 'externalIds', 'url', 'referenceCount' and 'citationCount'. All contains all possible fields. Custom allows for the use of the custom_fields parameter to specify a custom list of fields to be included in the output. \n
    custom_fields: A list of strings containing the names of fields to be included. For a full list of fields, see https://api.semanticscholar.org/api-docs/graph. \n
    paginate: A boolean describing whether to get more than the first page of results.  \n
    api_key: A string containing an api_key for the Semantic Scholar API \n
    
    Outputs: \n
    A list of dictionaries containing the results. 
    """
    # Check for input integrity 
    if fields not in ['Basic', 'Extended','All','Custom']: 
        raise ValueError('"fields" parameter must be either "Basic", "Extended", "All" or "Custom"')
    if not isinstance(paper_id,str): 
        raise TypeError('author_id must be of type list.')
    if not isinstance(custom_fields, (bool,list)):
        raise TypeError('"custom_fields" parameter must be of type list or type bool.')
    if not isinstance(api_key, (bool,str)):
        raise TypeError('"api_key" parameter must be of type str or type bool')
    if fields == 'Custom' and not isinstance(custom_fields,list): 
        raise TypeError('"custom_fields" parameter must be of type list when using the "Custom" option for "fields".')
    if not isinstance(limit, int): 
        raise TypeError('"limit" parameter must be of type int.')
    if not isinstance(paginate, bool):
        raise TypeError('"paginate" parameter must of type bool.')
    if not isinstance(offset, int): 
        raise TypeError('"offset" parameter must be of type int.')

    # Construct base query for the endpoint with the 
    # given paper ID 
    base_query = f'paper/{paper_id}/citations?'

    # Assemble query fields to a string for use in request 
    query_fields = assemble_query_fields(fields,custom_fields,'Citation')

    # Construct the final query 
    final_query = GRAPH_API_REF + base_query + "&fields=" + query_fields

    # Add limit to the query if limit is not equal to 100, as 
    # 100 is the standard for the endpoint in question. 
    if limit != 100:
        final_query += f"&limit={limit}"
    
    # Add offset to the query, if offset is not equal to 0, as 
    # 0 is the standard for the endpoint in question. 
    if offset != 0: 
        final_query += f"&offset={offset}"
    

    # Make the request to the endpoint 
    if api_key: 
        request = requests.get(final_query,headers={'x-api-key':api_key})
    else: 
        request = requests.get(final_query)
    
    # Check status code on the request and generate output 
    if request.status_code == 200: 
        request_content = request.content 
        request_json = json.loads(request_content)
    else: 
        request_content = request.content 
        request_json = json.loads(request_content)
        raise ConnectionError(f"{request_json['error']}")

    results = list(request_json['data'])

    next_offset = request_json['next']
    past_offset = 0 
    # If paginate, then iterate over requests and generate output 
    if paginate:
        while request_json['next'] <= 10000 - limit and past_offset != next_offset: 
            past_offset = next_offset 
            if offset != 0: 
                query = final_query[:-len(str(offset))] + str(next_offset)
            else: 
                query = final_query + "&offset" + str(next_offset)
            if api_key: 
                request = requests.get(final_query,headers={'x-api-key':api_key})
            else: 
                request = requests.get(query)
            if request.status_code == 200: 
                request_content = request.content 
                request_json = json.loads(request_content)
            else: 
                request_content = request.content 
                request_json = json.loads(request_content)
                raise ConnectionError(f"{request_json['error']}")
            results.extend(request_json['data'])
            print(request_json['next'])
            next_offset = request_json['next']
    return results 

def paperReferences(paper_id:str ="",   
                    fields: str ='Basic',
                    custom_fields: list =False,
                    api_key: str =False,
                    paginate=False,
                    limit: int=100,
                    offset: int =0) -> list[dict]: 
    """
    Provides a wrapper for the Semantic Scholar Graph API's paper references endpoint. 

    Inputs: \n
    paper_id: A string containing the paper_id\n
    limit: An int containing the number of results per call to the API's endpoint. \n
    offset: An int containing the number of results to skip. \n
    fields: One of either 'Basic', 'Extended', 'All' or 'Custom'. Basic contains 'paperId', 'title', 'abstract', 'year', 'journal' and 'authors'. Extended contains all of the above, as well as 'externalIds', 'url', 'referenceCount' and 'citationCount'. All contains all possible fields. Custom allows for the use of the custom_fields parameter to specify a custom list of fields to be included in the output. \n
    custom_fields: A list of strings containing the names of fields to be included. For a full list of fields, see https://api.semanticscholar.org/api-docs/graph. \n
    paginate: A boolean describing whether to get more than the first page of results.  \n
    api_key: A string containing an api_key for the Semantic Scholar API \n
    
    Outputs: \n
    A list of dictionaries containing the results. 
    """
    # Check for input integrity 
    if fields not in ['Basic', 'Extended','All','Custom']: 
        raise ValueError('"fields" parameter must be either "Basic", "Extended", "All" or "Custom"')
    if not isinstance(paper_id,str): 
        raise TypeError('author_id must be of type list.')
    if not isinstance(custom_fields, (bool,list)):
        raise TypeError('"custom_fields" parameter must be of type list or type bool.')
    if not isinstance(api_key, (bool,str)):
        raise TypeError('"api_key" parameter must be of type str or type bool')
    if fields == 'Custom' and not isinstance(custom_fields,list): 
        raise TypeError('"custom_fields" parameter must be of type list when using the "Custom" option for "fields".')
    if not isinstance(limit, int): 
        raise TypeError('"limit" parameter must be of type int.')
    if not isinstance(paginate, bool):
        raise TypeError('"paginate" parameter must of type bool.')
    if not isinstance(offset, int): 
        raise TypeError('"offset" parameter must be of type int.')

    # Construct base query for the endpoint with the 
    # given paper ID 
    base_query = f'paper/{paper_id}/references?'

    # Assemble query fields to a string for use in request 
    query_fields = assemble_query_fields(fields,custom_fields,'Citation')

    # Construct the final query 
    final_query = GRAPH_API_REF + base_query + "&fields=" + query_fields

    # Add limit to the query if limit is not equal to 100, as 
    # 100 is the standard for the endpoint in question. 
    if limit != 100:
        final_query += f"&limit={limit}"
    
    # Add offset to the query, if offset is not equal to 0, as 
    # 0 is the standard for the endpoint in question. 
    if offset != 0: 
        final_query += f"&offset={offset}"
    

    # Make the request to the endpoint 
    if api_key: 
        request = requests.get(final_query,headers={'x-api-key':api_key})
    else: 
        request = requests.get(final_query)
    
    # Check status code on the request and generate output 
    if request.status_code == 200: 
        request_content = request.content 
        request_json = json.loads(request_content)
    else: 
        request_content = request.content 
        request_json = json.loads(request_content)
        raise ConnectionError(f"{request_json['error']}")

    results = list(request_json['data'])

    next_offset = request_json['next']
    past_offset = 0 
    # If paginate, then iterate over requests and generate output 
    if paginate:
        while request_json['next'] <= 10000 - limit and past_offset != next_offset: 
            past_offset = next_offset 
            if offset != 0: 
                query = final_query[:-len(str(offset))] + str(next_offset)
            else: 
                query = final_query + "&offset" + str(next_offset)
            if api_key: 
                request = requests.get(final_query,headers={'x-api-key':api_key})
            else: 
                request = requests.get(query)
            if request.status_code == 200: 
                request_content = request.content 
                request_json = json.loads(request_content)
            else: 
                request_content = request.content 
                request_json = json.loads(request_content)
                raise ConnectionError(f"{request_json['error']}")
            results.extend(request_json['data'])
            print(request_json['next'])
            next_offset = request_json['next']

    return results 
