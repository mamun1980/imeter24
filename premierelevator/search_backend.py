from haystack.backends.elasticsearch_backend import ElasticsearchSearchBackend
from haystack.backends.elasticsearch_backend import ElasticsearchSearchEngine

class FuzzyBackend(ElasticsearchSearchBackend):
    def build_search_kwargs(self, query_string, **kwargs):
        kwargs = {
            'query': {
                'fuzzy_like_this': {
                    'like_text': query_string,
                    'prefix_length': 0
                },
            },

        }
        return kwargs


class ConfigurableElasticSearchEngine(ElasticsearchSearchEngine):
    backend = FuzzyBackend