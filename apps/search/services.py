from config.elasticsearch import es

def search_products(query, category=None, min_rating=None):
    body = {
        "query": {
            "bool": {
                "must": [{"match": {"name": query}}],
                "filter": []
            }
        }
    }
    if category:
        body["query"]["bool"]["filter"].append({"term": {"main_category": category}})
    if min_rating:
        body["query"]["bool"]["filter"].append({"range": {"ratings": {"gte": min_rating}}})
    
    return es.search(index="products", body=body)
