import unittest 

import semanticSearch as Search 

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


class AuthorSearchTests(unittest.TestCase()): 

    def test_input_basic(self): 
        tmp = Search.author_search('Adam Smith',limit=1)
        keys = sorted(list(tmp[0].keys()))
        self.assertEqual(keys,sorted(list(AUTHOR_FIELDS_BASIC)))
    
