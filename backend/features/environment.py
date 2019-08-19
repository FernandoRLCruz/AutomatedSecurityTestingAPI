import os
import sys
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)


def before_all(context):
    context.base_url = context.config.userdata['URL']


def before_feature(context, feature):
        print("inicio")     
        #context.service_center_url = context.config.userdata['']


def before_scenario(context, scenario):
    with open("scenarios.txt", "a") as f:
        print(context.scenario.name, file=f)
