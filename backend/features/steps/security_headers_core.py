import common.requests_generic as rg

result = []

def security_headers_initial(url, method, header_value, body_value, name_domain, attack_method):
		response = rg.send_request_generic(url, method, header_value, body_value)
		response_headers_temp = response.headers
		response_body_temp = response.text
		response_cookies_temp =  response.cookies
		if attack_method == "csp_check":
    			result.append(csp_check(url, method, headers, body, scan_id, res_headers, res_body))
		elif attack_method == "xss_protection_check":
    			result.append(xss_protection_check(url, method, headers, body, scan_id, res_headers, res_body))
		elif attack_method == "x_frame_options_check":
    			result.append(x_frame_options_check(url, method, headers, body, scan_id, res_headers, res_body))
		elif attack_method == "x_content_type_options_check":
    			result.append(x_content_type_options_check(url, method, headers, body, scan_id, res_headers, res_body))
		elif attack_method == "hsts_check":
    			result.append(hsts_check(url, method, headers, body, scan_id, res_headers, res_body))
		elif attack_method == "cookies_check":
				result.append(cookies_check(cookies, url, method, headers, body, scan_id, res_headers, res_body))
		elif attack_method == "check_version_disclosure":
    			result.append(check_version_disclosure(url, method, headers, body, scan_id, res_headers, res_body))
		return result



def csp_check(url, method, headers, body, scan_id, res_headers, res_body):
    	# checks if csp header is implemented
		if 'Content-Security-Policy' not in res_headers:
		attack_result = { "id" : 15, "scanid" : scan_id, "url" : url, "alert": "CSP Header Missing", "impact": "Low", "req_headers": req_headers, "req_body": req_body, "res_headers": res_headers ,"res_body": res_body}