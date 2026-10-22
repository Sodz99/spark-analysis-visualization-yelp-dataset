from opensearchpy import OpenSearch, RequestsHttpConnection
import certifi

# Connect to OpenSearch
host = 'search-yelp-tutorial-hmnuzx5f2dvl2tcep2pj5q5el4.us-east-1.es.amazonaws.com'
auth = ('admin', '<***REMOVED***>')

es = OpenSearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=auth,
    use_ssl=True,
    verify_certs=True,
    ca_certs=certifi.where(),
    connection_class=RequestsHttpConnection,
    headers={"Content-Type": "application/json"}
)

# Create index with mapping for business data
business_mapping = {
    "mappings": {
        "properties": {
            "business_id": {"type": "keyword"},
            "full_address": {"type": "text"},
            "open": {"type": "boolean"},
            "categories": {"type": "text"},
            "city": {"type": "keyword"},
            "review_count": {"type": "integer"},
            "name": {"type": "text"},
            "neighborhoods": {"type": "text"},
            "location": {"type": "geo_point"},
            "state": {"type": "keyword"},
            "stars": {"type": "float"},
            "type": {"type": "keyword"}
        }
    }
}
es.indices.create(index="yelp-business", body=business_mapping, ignore=400)

# Create index with mapping for checkin data
checkin_mapping = {
    "mappings": {
        "properties": {
            "type": {"type": "keyword"},
            "business_id": {"type": "keyword"}
        }
    }
}
es.indices.create(index="yelp-checkin", body=checkin_mapping, ignore=400)

# Create index with mapping for reviews data
reviews_mapping = {
    "mappings": {
        "properties": {
            "user_id": {"type": "keyword"},
            "review_id": {"type": "keyword"},
            "stars": {"type": "float"},
            "date": {"type": "date"},
            "text": {"type": "text"},
            "type": {"type": "keyword"},
            "business_id": {"type": "keyword"},
            "votes_funny": {"type": "integer"},
            "votes_useful": {"type": "integer"},
            "votes_cool": {"type": "integer"},
        }
    }
}
es.indices.create(index="yelp-reviews", body=reviews_mapping, ignore=400)

# Create index with mapping for users data
users_mapping = {
    "mappings": {
        "properties": {
            "yelping_since": {"type": "date"},
            "review_count": {"type": "integer"},
            "name": {"type": "text"},
            "user_id": {"type": "keyword"},
            "fans": {"type": "integer"},
            "average_stars": {"type": "float"},
            "type": {"type": "keyword"},
            "elite": {"type": "text"},
            "votes_funny": {"type": "integer"},
            "votes_useful": {"type": "integer"},
            "votes_cool": {"type": "integer"},
            "compliments_profile": {"type": "float"},
            "compliments_cute": {"type": "float"},
            "compliments_funny": {"type": "float"},
            "compliments_plain": {"type": "float"},
            "compliments_writer": {"type": "float"},
            "compliments_note": {"type": "float"},
            "compliments_photos": {"type": "float"},
            "compliments_hot": {"type": "float"},
            "compliments_cool": {"type": "float"},
            "compliments_more": {"type": "float"},
            "compliments_list": {"type": "float"},
        }
    }
}
es.indices.create(index="yelp-users", body=users_mapping, ignore=400)
