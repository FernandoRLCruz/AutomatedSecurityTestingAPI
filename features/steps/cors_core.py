import common.requests_generic as rg


def cors_initial(url, method, header_value, body_value, name_domain):
    headers_temp = {}
    headers_origin = {}
    result = {}
    headers_temp.update(header_value)
    protocol = url[:url.find(':')]
    #get diferent origin urls
    if protocol == "http" or protocol == "https":
       domain_origin_attack = protocol + "://attackersite.com"
       post_url_attack = name_domain + ".attackersite.com"

    headers_origin["domain_origin_attack"] = domain_origin_attack
    headers_origin["post_url_attack"] = post_url_attack

    for origin_url in headers_origin:
        headers_origin = {"origin_url", origin_url}
        headers_temp.update(headers_origin)
        if method.upper() == 'GET' or method.upper() == 'POST' or method.upper() == 'PUT':
                context.response = rg.send_request_generic(url, "OPTIONS", headers_temp, body_value)

    return result            