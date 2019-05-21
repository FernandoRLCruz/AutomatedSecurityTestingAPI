import os
import sys
import json
import requests
import common.requests_generic as rg
import ast
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)

from hamcrest import assert_that, is_, greater_than, equal_to
from behave import then, when, given
from urllib.parse import urlparse




@given(u'I verify api "{url}" using for following methods "{method}"')
def get_url_method_data(context, url, method):
    nameTemp = urlparse(url)
    context.url = url
    context.name_domain = nameTemp.hostname
    context.method = method

@when(u'I include the "{headers}" and "{body}" to request')
def include_header_body(context, headers, body):
    try:
         if headers is None or headers == ' ':
            headers = {'Content-Type' : 'application/json'}

         if type(headers) is not dict:
            #headers = {'Content-Type' : 'application/json'}
            context.header_value = json.loads(headers)
            
            
    
         if type(body) is not dict:
            context.body_value = ast.literal_eval(body)

    except Exception as e:              
        print("Exception from include_header_body %s", e)

@when(u'I check result response')
def result_response(context):
     try:
         headers_temp = {}
         headers_origin = {}
         headers_temp.update(context.header_value)
         protocol = context.url[:context.url.find(':')]
         #get diferent origin urls
         if protocol == "http" or protocol == "https":
            domain_origin_attack = protocol + "://attackersite.com"
         post_url_attack = context.name_domain + ".attackersite.com"

         headers_origin.append(domain_origin_attack)
         headers_origin.append(post_url_attack)

         for origin_url in headers_origin:
             headers_origin = {"origin_url", origin_url}
             headers_temp.update(headers_origin)
             if context.method.upper() == 'GET' or context.method.upper() == 'POST' or context.method.upper() == 'PUT':
                context.response = rg.send_request_generic(context.url, "OPTIONS", headers_temp, context.body_value)

     except Exception as e:              
        print("Exception from result_response %s", e)
    

        
    
    
    