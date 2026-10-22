from opensearchpy import OpenSearch, RequestsHttpConnection, helpers
import certifi
import json
import os
import math

host = 'search-yelp-tutorial-hmnuzx5f2dvl2tcep2pj5q5el4.us-east-1.es.amazonaws.com'
auth = ('admin', "***REMOVED***")

# Connect to OpenSearch
es = OpenSearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=auth,
    use_ssl=True,
    verify_certs=True,
    ca_certs=certifi.where(),
    connection_class=RequestsHttpConnection,
    headers={"Content-Type": "application/json"}
)

def transform_data(doc):
    # Transform location field
    if 'location' in doc:
        if 'latitude' in doc['location'] and 'longitude' in doc['location']:
            doc['location'] = {
                "lat": doc['location'].get('latitude'),
                "lon": doc['location'].get('longitude')
            }
    
    # Replace 'nan' with None
    for key, value in doc.items():
        if isinstance(value, str) and value == 'nan':
            doc[key] = None
        elif isinstance(value, dict):
            doc[key] = transform_data(value)
    
    return doc

def load_json(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename)) as f:
                for line in f:
                    doc = json.loads(line)
                    yield transform_data(doc)

# Index Business Data
helpers.bulk(es, load_json("/home/hadoop/yelp/json/business"), index='yelp-business')

# Index Checkin Data
helpers.bulk(es, load_json("/home/hadoop/yelp/json/checkin"), index='yelp-checkin')

# Index Reviews Data
helpers.bulk(es, load_json("/home/hadoop/yelp/json/reviews_sample"), index='yelp-reviews')

# Index Users Data
helpers.bulk(es, load_json("/home/hadoop/yelp/json/users"), index='yelp-users')
