import common.requests_generic as rg
import re
import random
import string

result = ''


def brute_force_initial(url, method, header_value, body_value):
    try:
        if method == "POST" or method == "PUT":
            if body_value:
                # Before we brute force, we need to find suspicious param to attack.
                param_names = ['pin', 'password', 'cvv', 'pass', 'otp']
                attack_params = []
                for name in param_names:
                    for key, value in body_value.items():
                        if name.lower() == key.lower():
                            attack_params.append(name.lower())

                    if attack_params:
                        attack_result = brute_force(url, method, header_value, body_value, attack_params)
                        print(attack_result)
                        return attack_result
                            
    except:
        print("Falha no teste de brute force")


def generate_brute_list(length, type):
    # Generate different possible param value for brute force
    brute_force_list = []
    if type == 'int':
        length = '%0'+str(length)+'d'
        brute_force_list = [length % x for x in range(50)]
    elif type == 'str':
        for a in range(1, 50):
            brute_force_list += [''.join(random.choice(string.ascii_letters)
                                         for i in range(length))]
    return brute_force_list


def brute_force(url, method, header_value, body_value, attack_params):
    attack_result = {}
    failed_set = ['exceed', 'captcha',
                  'too many', 'rate limit', 'Maximum login']
    if len(attack_params) == 1:
        # attack_params[0] is a first value from list Ex Pin, password
        # param_value is a value of param. Example: 1234
        param_value = body_value[attack_params[0]]
        if type(param_value) == int:
            length = len(str(param_value))
            brute_list = generate_brute_list(length, 'int')

        elif type(param_value) == str or type(param_value) == string.unicode:
            length = len(param_value)
            brute_list = generate_brute_list(length, 'str')

        # Starting brute force attack.
        count = 0
        if brute_list is not None:
            for value in brute_list:
                    # Mdofiying a json data and update the dictionary.
                    # Example:{"Username":"test",password:"abc"}
                    #		  {"Username":"test",password:"def"}
                brute_force_request = rg.send_request_generic(
                    url, method, header_value, body_value)
                if brute_force_request is not None:
                    if count == 0:
                        http_len = len(brute_force_request.text)
                        count += count

            if len(brute_force_request.text) == http_len:
                if str(brute_force_request.status_code)[0] == '2' or str(brute_force_request.status_code)[0] == '4':
                    for failed_name in failed_set:
                        if failed_name in brute_force_request.text:
                            # Brute force protection detected :-(
                            result = False
                            break
                        else:
                            result = True

            if result is True:
                attack_result = {
                    "id": 7,
                    "url": url,
                    "alert": "Missing Rate limit",
                    "impact": "High",
                    "req_headers": header_value,
                    "req_body": body_value,
                    "res_headers": brute_force_request.headers,
                    "res_body": brute_force_request.text

                }

            return attack_result
