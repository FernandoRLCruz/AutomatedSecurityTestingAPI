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
        headers_temp["headers_origin"] = headers_origin
        if method.upper() == 'GET' or method.upper() == 'POST' or method.upper() == 'PUT':
                response = rg.send_request_generic(url, "OPTIONS", headers_temp, body_value)
                result = cors_execute(origin_url, response)
                if result:
                    print ("[+]{0} está vulneravel para cross domain attack".format(url))
                    result = {"url" : url, "impacto": result['nivel_impacto'], "headers": headers_temp, "body" : body_value, "res_headers": response, "resultado": "[+]{0} está vulneravel para cross domain attack".format(url)}

    return result

def cors_execute(origin_url, response):
    result={}
    if all (x in response for x in ("Access-Control-Allow-Origin","Access-Control-Allow-Credentials")):
        status_origin_header = response['Access-Control-Allow-Origin']
        if origin_url.lower() == status_origin_header.lower() or origin_url.lower() == status_origin_header[status_origin_header.find('://')+3:].lower():
            if response['Access-Control-Allow-Credentials'] == 'true':
                result.update({"nivel_impacto" : "Alto"})
            else:
                result.update({"nivel_impacto" : "Baixo"})
        elif status_origin_header == "*":
            result.update({"nivel_impacto" : "Baixo"})
    elif 'Access-Control-Allow-Origin' in response:
        result.update({"nivel_impacto" : "Baixo"})

    return result