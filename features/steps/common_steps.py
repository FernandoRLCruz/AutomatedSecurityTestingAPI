import os
import sys
import json
import requests
import ast
import cors_core as cors
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)

from hamcrest import assert_that, is_, greater_than, equal_to, contains_string
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
            context.header_value = json.loads(headers)         
            
    
         if type(body) is not dict:
            context.body_value = ast.literal_eval(body)

    except Exception as e:              
        print("Exception from include_header_body %s", e)