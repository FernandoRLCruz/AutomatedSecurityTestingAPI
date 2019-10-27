import os
import sys
import json
import requests
import ast
import sql_injection_core as sic
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)

from hamcrest import assert_that, is_, greater_than, equal_to, contains_string
from behave import then, when, given
from urllib.parse import urlparse




@when(u'I check result sqli response')
def result_response(context):
    result = []
    try:
        result.append(sic.sql_injection_initial(context.url, context.method, context.header_value, context.body_value, context.config.userdata['URL_SQLMAP']))
        for item in result:
            if item != None:
                assert_that(item["impact"], is_("Low"))

    except Exception as e:              
        print("Exception from result_response %s", e)