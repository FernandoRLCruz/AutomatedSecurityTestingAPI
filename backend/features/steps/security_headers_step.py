import os
import sys
import json
import requests
import ast
import security_headers_core as shc
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)

from hamcrest import assert_that, is_, greater_than, equal_to, contains_string
from behave import then, when, given
from urllib.parse import urlparse




@when(u'I check result security headers response')
def result_response(context):
    result = []
    try:
        for row in context.table:
            result.append(shc.security_headers_initial(context.url, context.method, context.header_value, context.body_value, context.name_domain, row["attack_method"]))
        for item in result:
            if item != None:
                assert_that(item["alert"])                

    except Exception as e:              
        print("Exception from result_response %s", e)
    

        
    
    
    