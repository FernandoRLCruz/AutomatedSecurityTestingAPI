import os
import sys
import json
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

@when(u'I include the "{header}" and "{body}" to request')
def include_header_body(context, header, body):
    if header is None or header == ' ':
        headers = {'Content-Type' : 'application/json'}

    try:
         if type(header) is not dict:
            headers = json.loads(headers)
    
         if type(body) is not dict:
            context.body = json.loads(body)

    except:              
        print("Not possible convert")

when(u'I check result response')
def include_header_body(context, header, body):
    headers_temp = []
    headers_origin = []
    headers_temp.update(header)
    protocol = context.url[:context.url.find(':')]
    if protocol == "http" or protocol == "https":
        domain_origin_attack = protocol + "://attackersite.com"
    post_url_attack = context.name_domain + ".attackersite.com"
    headers_origin.append(domain_origin_attack)
    headers_origin.append(post_url_attack)
    

        
    
    
    