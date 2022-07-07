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
    'papers.publicationTypes',
    'papers.publicationDate',
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
        'publicationTypes',
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
        'publicationTypes',
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