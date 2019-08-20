import common.requests_generic as rg

def security_headers_initial(url, method, header_value, body_value, name_domain):
    response = rg.send_request_generic(url, method, header_value, body_value)
    response_headers_temp = response.headers
	response_body_temp = response.text
	response_cookies_temp =  response.cookies   
	csp_check(url, method, headers, body, scan_id, res_headers, res_body)
	xss_protection_check(url, method, headers, body, scan_id, res_headers, res_body)
	x_frame_options_check(url, method, headers, body, scan_id, res_headers, res_body)
	x_content_type_options_check(url, method, headers, body, scan_id, res_headers, res_body)
	hsts_check(url, method, headers, body, scan_id, res_headers, res_body)
	cookies_check(cookies, url, method, headers, body, scan_id, res_headers, res_body)
	check_version_disclosure(url, method, headers, body, scan_id, res_headers, res_body)