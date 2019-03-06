
def before_feature(context, feature):
    context.service_center_url = context.config.userdata['']




def before_scenario(context, scenario):
    with open("scenarios.txt", "a") as f:
        print(context.scenario.name, file=f)
