from haystack.backends.elasticsearch_backend import ElasticsearchSearchBackend
from haystack.backends.elasticsearch_backend import ElasticsearchSearchEngine

class FuzzyBackend(ElasticsearchSearchBackend):
    DEFAULT_ANALYZER = "whitespace"

    def build_search_kwargs(self, query_string, **kwargs):
        if query_string == '*:*':
            kwargs = {
                'query': {
                    "match_all": {}
                },
            }
        else:
            kwargs = {
                'query': {
                    'fuzzy_like_this': {
                        'like_text': query_string,
                        'prefix_length': 1
                    },
                }
            }
        return kwargs


class ConfigurableElasticSearchEngine(ElasticsearchSearchEngine):
    backend = FuzzyBackend

# DEFAULT_SETTINGS = {
#     'settings': {
#         "analysis": {
#             "analyzer": {
#                 "ngram_analyzer": {
#                     "type": "custom",
#                     "tokenizer": "lowercase",
#                     "filter": ["haystack_ngram"]
#                 },
#                 "edgengram_analyzer": {
#                     "type": "custom",
#                     "tokenizer": "lowercase",
#                     "filter": ["haystack_edgengram"]
#                 }
#             },
#             "tokenizer": {
#                 "haystack_ngram_tokenizer": {
#                     "type": "nGram",
#                     "min_gram": 3,
#                     "max_gram": 15,
#                 },
#                 "haystack_edgengram_tokenizer": {
#                     "type": "edgeNGram",
#                     "min_gram": 2,
#                     "max_gram": 15,
#                     "side": "front"
#                 }
#             },
#             "filter": {
#                 "haystack_ngram": {
#                     "type": "nGram",
#                     "min_gram": 3,
#                     "max_gram": 15
#                 },
#                 "haystack_edgengram": {
#                     "type": "edgeNGram",
#                     "min_gram": 2,
#                     "max_gram": 15
#                 }
#             }
#         }
#     }
# }