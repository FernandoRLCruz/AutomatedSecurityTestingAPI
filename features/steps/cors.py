import os
import sys
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)

from hamcrest import assert_that, is_, greater_than, equal_to
from behave import then, when, given
from urllib.parse import urlparse



@given(u'I verify api "{url}" using for following methods "{method}"')
def get_url_method_data(context, url, method):
    nameTemp = urlparse(url)
    context.name = nameTemp.hostname
    print(context.name)
    context.method = method

@when(u'I include the "{header}" and "{body}" to request')
def include_header_body(context, header, body):
    if header is None or header == ' ':
        headers = {'Content-Type' : 'application/json'}
    else:
        context.header = header
    context.body = body

when(u'I check result response')
def include_header_body(context, header, body):
    print("TODO")
    #cors_main()