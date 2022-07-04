
import requests 
import json 


GRAPH_API_REF = "https://api.semanticscholar.org/graph/v1/"
RECOMMENDER_API_REF = "https://api.semanticscholar.org/recommender/v1/"
DATASETS_API_REF = "https://api.semanticscholar.org/datasets/v1/"


AUTHOR_FIELDS = (
    'authorId',
    'externalIds',
    'url',
    'name',
    'aliases',
    'affiliations',
    'homepage',
    'paperCount',
    'citationCount',
    'hIndex',
    'papers',
    'papers.paperId',
    'papers.externalIds',
    'papers.url',
    'papers.title',
    'papers.abstract',
    'papers.venue',
    'papers.year',
    'papers.referenceCount',
    'papers.citationCount',
    'papers.influentialCitationCount',
    'papers.isOpenAccess',
    'papers.fieldsOfStudy',
    'papers.s2FieldsOfStudy',
    'papers.journal',
    'papers.authors'
)

AUTHOR_FIELDS_BASIC = (
    'authorId',
    'name',
    'affiliations',
    'url'
)

AUTHOR_FIELDS_EXTENDED = (
    'authorId',
    'name',
    'affiliations',
    'homepage',
    'url',
    'aliases',
    'hIndex'
)



PAPER_FIELDS = (
    'paperId',
    'externalIds',
    'url',
    'title',
    'abstract',
    'venue',
    'year',
    'referenceCount',
    'citationCount',
    'influentialCitationCount',
    'isOpenAccess',
    'fieldsOfStudy',
    's2FieldsOfStudy',
    'publicationType',
    'publicationDate',
    'journal',
    'authors'
)

PAPER_FIELDS_BASIC = (
    'paperId',
    'title',
    'abstract',
    'publicationDate',
    'journal',
    'authors'
)

PAPER_FIELDS_EXTENDED = (
    'paperId',
    'externalIds',
    'url',
    'title',
    'abstract',
    'venue',
    'year',
    'publicationType',
    'publicationDate',
    'journal',
    'authors'
)

PAPER_CITATION_FIELDS = (
    'contexts',
    'intents',
    'isInfluential',
    'paperId',
    'corpusId',
    'externalIds',
    'url',
    'title',
    'abstract',
    'venue',
    'year',
    'referenceCount',
    'citationCount',
    'influentialCitationCount',
    'isOpenAccess',
    'fieldsOfStudy',
    's2FieldsOfStudy',
    'publicationTypes',
    'publicationDate',
    'journal',
    'authors'
)

PAPER_CITATION_BASIC = (
    'paperId',
    'title',
    'abstract',
    'year',
    'journal',
    'authors'
)

PAPER_CITATION_EXTENDED = (
    'paperId',
    'title',
    'abstract',
    'year',
    'journal',
    'externalIds',
    'url',
    'referenceCount',
    'citationCount'
)


def assemble_query_fields(fields:str='Basic', 
                    custom_fields:list = False,
                    search_type:str = False):

    AUTHOR_FIELDS = (
    'authorId',
    'externalIds',
    'url',
    'name',
    'aliases',
    'affiliations',
    'homepage',
    'paperCount',
    'citationCount',
    'hIndex',
    'papers',
    'papers.paperId',
    'papers.externalIds',
    'papers.url',
    'papers.title',
    'papers.abstract',
    'papers.venue',
    'papers.year',
    'papers.referenceCount',
    'papers.citationCount',
    'papers.influentialCitationCount',
    'papers.isOpenAccess',
    'papers.fieldsOfStudy',
    'papers.s2FieldsOfStudy',
    'papers.journal',
    'papers.authors'
    )

    AUTHOR_FIELDS_BASIC = (
        'authorId',
        'name',
        'affiliations',
        'url'
    )

    AUTHOR_FIELDS_EXTENDED = (
        'authorId',
        'name',
        'affiliations',
        'homepage',
        'url',
        'aliases',
        'hIndex'
    )



    PAPER_FIELDS = (
        'paperId',
        'externalIds',
        'url',
        'title',
        'abstract',
        'venue',
        'year',
        'referenceCount',
        'citationCount',
        'influentialCitationCount',
        'isOpenAccess',
        'fieldsOfStudy',
        's2FieldsOfStudy',
        'publicationType',
        'publicationDate',
        'journal',
        'authors'
    )

    PAPER_FIELDS_BASIC = (
        'paperId',
        'title',
        'abstract',
        'publicationDate',
        'journal',
        'authors'
    )

    PAPER_FIELDS_EXTENDED = (
        'paperId',
        'externalIds',
        'url',
        'title',
        'abstract',
        'venue',
        'year',
        'publicationType',
        'publicationDate',
        'journal',
        'authors'
    )

    PAPER_CITATION_FIELDS = (
        'contexts',
        'intents',
        'isInfluential',
        'paperId',
        'corpusId',
        'externalIds',
        'url',
        'title',
        'abstract',
        'venue',
        'year',
        'referenceCount',
        'citationCount',
        'influentialCitationCount',
        'isOpenAccess',
        'fieldsOfStudy',
        's2FieldsOfStudy',
        'publicationTypes',
        'publicationDate',
        'journal',
        'authors'
    )

    PAPER_CITATION_BASIC = (
        'paperId',
        'title',
        'abstract',
        'year',
        'journal',
        'authors'
    )

    PAPER_CITATION_EXTENDED = (
        'paperId',
        'title',
        'abstract',
        'year',
        'journal',
        'externalIds',
        'url',
        'referenceCount',
        'citationCount'
    )
    
    if search_type == "Author": 
        # Check which field configuration has been specified, if any. 
        # Then create a string of the appropriate fields, joined 
        # with ,'s. 
        if fields == 'Basic': 
            query_fields = ",".join(AUTHOR_FIELDS_BASIC)
        elif fields == "Extended": 
            query_fields = ",".join(AUTHOR_FIELDS_EXTENDED)
        elif fields == "All": 
            query_fields = ",".join(AUTHOR_FIELDS)
        elif fields == "Custom": 
            # Check each fields in the custom_fields list against the 
            # list of valid fields. If a field is not included in the list
            # of valid fields, raise a ValueError. 
            for field in custom_fields: 
                if field not in AUTHOR_FIELDS: 
                    raise ValueError(f'{field} is not a valid field to include in custom fields.')
            
            query_fields = ",".join(custom_fields)
    elif search_type == 'Paper': 
        # Check which field configuration has been specified, if any. 
        # Then create a string of the appropriate fields, joined 
        # with ,'s. 
        if fields == 'Basic': 
            query_fields = ",".join(PAPER_FIELDS_BASIC)
        elif fields == "Extended": 
            query_fields = ",".join(PAPER_FIELDS_EXTENDED)
        elif fields == "All": 
            query_fields = ",".join(PAPER_FIELDS)
        elif fields == "Custom": 
            # Check each fields in the custom_fields list against the 
            # list of valid fields. If a field is not included in the list
            # of valid fields, raise a ValueError. 
            for field in custom_fields: 
                if field not in PAPER_FIELDS: 
                    raise ValueError(f'{field} is not a valid field to include in custom fields.')
            
            query_fields = ",".join(custom_fields)
    elif search_type == 'Citation': 
        # Check which field configuration has been specified, if any. 
        # Then create a string of the appropriate fields, joined 
        # with ,'s. 
        if fields == 'Basic': 
            query_fields = ",".join(PAPER_CITATION_BASIC)
        elif fields == "Extended": 
            query_fields = ",".join(PAPER_CITATION_EXTENDED)
        elif fields == "All": 
            query_fields = ",".join(PAPER_CITATION_FIELDS)
        elif fields == "Custom": 
            # Check each fields in the custom_fields list against the 
            # list of valid fields. If a field is not included in the list
            # of valid fields, raise a ValueError. 
            for field in custom_fields: 
                if field not in PAPER_CITATION_FIELDS: 
                    raise ValueError(f'{field} is not a valid field to include in custom fields.')
            
            query_fields = ",".join(custom_fields)
    return query_fields




def author_search(name:str ="",   
                    limit: int=100,
                    offset: int =0,
                    fields: str ='Basic',
                    custom_fields: list =False,
                    api_key: str =False,
                    paginate=False) -> list[dict]: 
    """
    Provides a wrapper for the Semantic Scholar Graph API's author search endpoint. 

    Inputs: \n
    name: A string containing the name being searched for \n
    limit: An int containing the number of results per call to the API's endpoint. \n
    offset: An int containing the number of results to skip. \n
    fields: One of either 'Basic', 'Extended', 'All' or 'Custom'. Basic contains 'authorId', 'name', 'affiliations' and 'url'. Extended contains all of the above as well as 'homepage', 'hIndex' and 'aliases'. All contains all possible fields. Custom allows for the use of the custom_fields parameter to specify a custom list of fields to be included in the output. \n
    custom_fields: A list of strings containing the names of fields to be included. For a full list of fields, see https://api.semanticscholar.org/api-docs/graph. \n
    paginate: A boolean describing whether to get more than the first page of results.  \n
    api_key: A string containing an api_key for the Semantic Scholar API  \n

    Outputs: \n
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
    if not isinstance(name,str):
        raise TypeError('"name" parameter must be of type str.')
    if not isinstance(custom_fields, (bool,list)):
        raise TypeError('"custom_fields" parameter must be of type list or type bool.')
    if not isinstance(api_key, (bool,str)):
        raise TypeError('"api_key" parameter must be of type str or type bool')
    if fields == 'Custom' and not isinstance(custom_fields,list): 
        raise TypeError('"custom_fields" parameter must be of type list when using the "Custom" option for "fields".')

    # Convert the search phrase to lowercase, strip extraneous 
    # whitespace and split based on spaces 
    name_strip = name.lower().strip().split(' ')
    
    # Construct the base query from the endpoint in use plus 
    # the name joined with +'s. 
    base_query = f'author/search?query={"+".join(name_strip)}' 
    
    
    query_fields = assemble_query_fields(fields,custom_fields,'Author')
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
    if paginate:
        while request_json['next'] <= 10000 - limit and next_offset != past_offset: 
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
            next_offset = request_json['next']
            print(len(results))
    return results 

def author_details(author_id:str ="",   
                    fields: str ='Basic',
                    custom_fields: list =False,
                    api_key: str =False) -> dict: 
    """
    Provides a wrapper for the Semantic Scholar Graph API's author details endpoint. 

    Inputs: 
    author_id: A string containing the author_id  
    fields: One of either 'Basic', 'Extended', 'All' or 'Custom'. Basic contains 'authorId', 'name', 'affiliations' and 'url'. Extended contains all of the above as well as 'homepage', 'hIndex' and 'aliases'. All contains all possible fields. Custom allows for the use of the custom_fields parameter to specify a custom list of fields to be included in the output. 
    custom_fields: A list of strings containing the names of fields to be included. For a full list of fields, see https://api.semanticscholar.org/api-docs/graph. 
    api_key: A string containing an api_key for the Semantic Scholar API 

    Outputs: 
    A dictionary containing the results. 
    """
    # Check for input integrity 
    if fields not in ['Basic', 'Extended','All','Custom']: 
        raise ValueError('"fields" parameter must be either "Basic", "Extended", "All" or "Custom"')
    if not isinstance(author_id,str): 
        raise TypeError('author_id must be of type list.')
    if not isinstance(custom_fields, (bool,list)):
        raise TypeError('"custom_fields" parameter must be of type list or type bool.')
    if not isinstance(api_key, (bool,str)):
        raise TypeError('"api_key" parameter must be of type str or type bool')
    if fields == 'Custom' and not isinstance(custom_fields,list): 
        raise TypeError('"custom_fields" parameter must be of type list when using the "Custom" option for "fields".')

    # Construct base query for the endpoint with the 
    # given author ID
    base_query = f'author/{author_id}?'

    # Assemble query fields to a string for use in request 
    query_fields = assemble_query_fields(fields,custom_fields,'Author')

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

def author_papers(author_id:str ="",   
                    fields: str ='Basic',
                    custom_fields: list =False,
                    api_key: str =False,
                    paginate=False,
                    limit: int=100,
                    offset: int =0) -> list[dict]:
    """
    Provides a wrapper for the Semantic Scholar Graph API's author papers endpoint. 

    Inputs: 
    author_id: A string containing the author_id
    limit: An int containing the number of results per call to the API's endpoint. 
    offset: An int containing the number of results to skip. 
    fields: One of either 'Basic', 'Extended', 'All' or 'Custom'. Basic contains 'authorId', 'name', 'affiliations' and 'url'. Extended contains all of the above as well as 'homepage', 'hIndex' and 'aliases'. All contains all possible fields. Custom allows for the use of the custom_fields parameter to specify a custom list of fields to be included in the output. 
    custom_fields: A list of strings containing the names of fields to be included. For a full list of fields, see https://api.semanticscholar.org/api-docs/graph. 
    paginate: A boolean describing whether to get more than the first page of results.  
    api_key: A string containing an api_key for the Semantic Scholar API 4
    
    Outputs: 
    A list of dictionaries containing the results. 
    """
    # Check for input integrity 
    if fields not in ['Basic', 'Extended','All','Custom']: 
        raise ValueError('"fields" parameter must be either "Basic", "Extended", "All" or "Custom"')
    if not isinstance(author_id,str): 
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
    # given author ID     
    base_query = f'author/{author_id}/papers?'

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
        print(request_json.keys())
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

def paper_search(query:str ="",   
                    limit: int=100,
                    offset: int =0,
                    fields: str ='Basic',
                    custom_fields: list =False,
                    api_key: str =False,
                    paginate=False) -> list[dict]: 
    """
    Provides a wrapper for the Semantic Scholar Graph API's paper search endpoint. 

    Inputs: 
    query: A string containing the keywords being searched for 
    limit: An int containing the number of results per call to the API's endpoint. 
    offset: An int containing the number of results to skip. 
    fields: One of either 'Basic', 'Extended', 'All' or 'Custom'. Basic contains 'paperId', 'title', 'abstract', 'publicationDate', 'journal' and 'authors'. Extended containts all of the above, as well as 'externalIds', 'url', 'venue', 'year', 'publicationType' and 'publicationDate'. All contains all possible fields. Custom allows for the use of the custom_fields parameter to specify a custom list of fields to be included in the output. 
    custom_fields: A list of strings containing the names of fields to be included. For a full list of fields, see https://api.semanticscholar.org/api-docs/graph. 
    paginate: A boolean describing whether to get more than the first page of results.  
    api_key: A string containing an api_key for the Semantic Scholar API 4

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

def paper_lookup(paper_id:str ="",   
                    fields: str ='Basic',
                    custom_fields: list =False,
                    api_key: str =False) -> dict: 
    """
    Provides a wrapper for the Semantic Scholar Graph API's paper details endpoint. 

    Inputs: 
    paper_id: A string containing the paper_id  
    fields: One of either 'Basic', 'Extended', 'All' or 'Custom'. Basic contains 'authorId', 'name', 'affiliations' and 'url'. Extended contains all of the above as well as 'homepage', 'hIndex' and 'aliases'. All contains all possible fields. Custom allows for the use of the custom_fields parameter to specify a custom list of fields to be included in the output. 
    custom_fields: A list of strings containing the names of fields to be included. For a full list of fields, see https://api.semanticscholar.org/api-docs/graph. 
    api_key: A string containing an api_key for the Semantic Scholar API 

    Outputs: 
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
    base_query = f'author/{paper_id}?'

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

def paper_authors(paper_id:str ="",   
                    fields: str ='Basic',
                    custom_fields: list =False,
                    api_key: str =False,
                    paginate=False,
                    limit: int=100,
                    offset: int =0) -> list[dict]: 
    """
    Provides a wrapper for the Semantic Scholar Graph API's paper authors endpoint. 

    Inputs: 
    paper_id: A string containing the paper_id
    limit: An int containing the number of results per call to the API's endpoint. 
    offset: An int containing the number of results to skip. 
    fields: One of either 'Basic', 'Extended', 'All' or 'Custom'. Basic contains 'authorId', 'name', 'affiliations' and 'url'. Extended contains all of the above as well as 'homepage', 'hIndex' and 'aliases'. All contains all possible fields. Custom allows for the use of the custom_fields parameter to specify a custom list of fields to be included in the output. 
    custom_fields: A list of strings containing the names of fields to be included. For a full list of fields, see https://api.semanticscholar.org/api-docs/graph. 
    paginate: A boolean describing whether to get more than the first page of results.  
    api_key: A string containing an api_key for the Semantic Scholar API 4
    
    Outputs: 
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

def paper_citations(paper_id:str ="",   
                    fields: str ='Basic',
                    custom_fields: list =False,
                    api_key: str =False,
                    paginate=False,
                    limit: int=100,
                    offset: int =0) -> list[dict]:
    """
    Provides a wrapper for the Semantic Scholar Graph API's paper citations endpoint. 

    Inputs: 
    paper_id: A string containing the paper_id
    limit: An int containing the number of results per call to the API's endpoint. 
    offset: An int containing the number of results to skip. 
    fields: One of either 'Basic', 'Extended', 'All' or 'Custom'. Basic contains 'paperId', 'title', 'abstract', 'year', 'journal' and 'authors'. Extended contains all of the above, as well as 'externalIds', 'url', 'referenceCount' and 'citationCount'. All contains all possible fields. Custom allows for the use of the custom_fields parameter to specify a custom list of fields to be included in the output. 
    custom_fields: A list of strings containing the names of fields to be included. For a full list of fields, see https://api.semanticscholar.org/api-docs/graph. 
    paginate: A boolean describing whether to get more than the first page of results.  
    api_key: A string containing an api_key for the Semantic Scholar API 4
    
    Outputs: 
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

def paper_references(paper_id:str ="",   
                    fields: str ='Basic',
                    custom_fields: list =False,
                    api_key: str =False,
                    paginate=False,
                    limit: int=100,
                    offset: int =0) -> list[dict]: 
    """
    Provides a wrapper for the Semantic Scholar Graph API's paper references endpoint. 

    Inputs: 
    paper_id: A string containing the paper_id
    limit: An int containing the number of results per call to the API's endpoint. 
    offset: An int containing the number of results to skip. 
    fields: One of either 'Basic', 'Extended', 'All' or 'Custom'. Basic contains 'paperId', 'title', 'abstract', 'year', 'journal' and 'authors'. Extended contains all of the above, as well as 'externalIds', 'url', 'referenceCount' and 'citationCount'. All contains all possible fields. Custom allows for the use of the custom_fields parameter to specify a custom list of fields to be included in the output. 
    custom_fields: A list of strings containing the names of fields to be included. For a full list of fields, see https://api.semanticscholar.org/api-docs/graph. 
    paginate: A boolean describing whether to get more than the first page of results.  
    api_key: A string containing an api_key for the Semantic Scholar API 4
    
    Outputs: 
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

def paper_recommender_multi(positivePaperIds: list = [], 
                        negativePaperIds: list = [], 
                        limit: int = 100,
                        fields: str = 'Basic',
                        custom_fields: list = None, 
                        api_key: str = None) -> list[dict]:

    """
    Provides a wrapper for the Semantic Scholar Recommendations API's paper recommendations endpoint. 

    Inputs: 
    positivePaperIds: A list containing positive paper ids 
    negativePaperIds: A list containing negative paper ids 
    limit: An int containing the number of results per call to the API's endpoint. 
    fields: One of either 'Basic', 'Extended', 'All' or 'Custom'. Basic contains 'paperId', 'title', 'abstract', 'year', 'journal' and 'authors'. Extended contains all of the above, as well as 'externalIds', 'url', 'referenceCount' and 'citationCount'. All contains all possible fields. Custom allows for the use of the custom_fields parameter to specify a custom list of fields to be included in the output. 
    custom_fields: A list of strings containing the names of fields to be included. For a full list of fields, see https://api.semanticscholar.org/api-docs/graph. 
    api_key: A string containing an api_key for the Semantic Scholar API 4
    
    Outputs: 
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


def paper_recommender_single(paperId:str, 
                            limit: int = 100,
                            fields: str = 'Basic',
                            custom_fields: list = None, 
                            api_key: str = None) -> list[dict]: 
    """
    Provides a wrapper for the Semantic Scholar Recommendations API's paper recommendations endpoint. 

    Inputs: 
    paperId: A string containing the paper id 
    limit: An int containing the number of results per call to the API's endpoint. 
    fields: One of either 'Basic', 'Extended', 'All' or 'Custom'. Basic contains 'paperId', 'title', 'abstract', 'year', 'journal' and 'authors'. Extended contains all of the above, as well as 'externalIds', 'url', 'referenceCount' and 'citationCount'. All contains all possible fields. Custom allows for the use of the custom_fields parameter to specify a custom list of fields to be included in the output. 
    custom_fields: A list of strings containing the names of fields to be included. For a full list of fields, see https://api.semanticscholar.org/api-docs/graph. 
    api_key: A string containing an api_key for the Semantic Scholar API 4
    
    Outputs: 
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

def dataset_releases(api_key:str = None ) -> list[str]:
    """ 
    Provides a wrapper for the Semantic Scholar Datasets API Releases endpoint 

    Input: 
    api_key: A string containing a key for the Semantic Scholar API 

    Output: 
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
    else: 
        request_content = request.content 
        request_json = json.loads(str(request_content))
        raise ConnectionError(f"{request_json['error']}")
    return request_content 

def datasetsInRelease(release_id:str=None,
                        api_key:str = None) -> dict: 
    """ 
    Provides a wrapper for the Semantic Scholar Datasets API Datasets in Release endpoint 

    Input: 
    release_id: A string containing the release id. 
    api_key: A string containing a key for the Semantic Scholar API 

    Output: 
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
        request_json = json.loads(str(request_content))
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