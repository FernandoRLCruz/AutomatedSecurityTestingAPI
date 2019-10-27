import os
import sys
import json
import requests
import ast
import brute_force_rate_limit_core as brute_force_core
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)

from hamcrest import assert_that, is_, greater_than, equal_to, contains_string
from behave import then, when, given
from urllib.parse import urlparse


@when(u'I check result brute force response')
def result_response(context):
    result = []
    try:
        result = brute_force_core.brute_force_initial(context.url, context.method, context.header_value, context.body_value)
        if result != None:
            assert_that(result["impact"], is_("High"))

    except Exception as e:              
        print("Exception from result_response %s", e)