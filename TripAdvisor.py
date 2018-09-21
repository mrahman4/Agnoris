# Function input paramters inside event object are :
# lat, lng, name

import boto3
import urllib.request
from db_util import make_conn, save_data

def lambda_handler(event, context):

   ## TODO: ask for api_key from https://developer-tripadvisor.com
   api_key = ""

   location_mapper_url_template = "http://api.tripadvisor.com/api/partner/2.0/location_mapper/{},{}?key={}-mapper&category=restaurants&q={}"
   url = location_mapper_url_template.format(event['lat'],event['lng'],api_key,event['name'])
   location_info = urllib.request.urlopen(url).read()


   location_rating_url_template = "http://api.tripadvisor.com/api/partner/2.0/location/{}?key={}"
   url = location_rating_url_template.format(location_info['location_id'],api_key)
   customers_feedback = urllib.request.urlopen(url).read()
   #print customers_feedback

   query_template = "INSERT INTO table (lat, lng, name, rating) VALUES ({}, {}, {}, {});"
   query = query_template.format(event['lat'],event['lng'],event['name'], customers_feedback[rating])
   conn = make_conn()
   save_data(conn, query)
   conn.close()

   return customers_feedback[rating]
