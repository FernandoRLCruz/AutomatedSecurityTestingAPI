import common.requests_generic as rg
import re

result = ''

def security_headers_initial(url, method, header_value, body_value, name_domain, attack_method):
		response = rg.send_request_generic(url, method, header_value, body_value)
		response_headers_temp = response.headers
		response_body_temp = response.text
		response_cookies_temp =  response.cookies
		if attack_method == "csp_check":
    			result = csp_check(url, method, response_headers_temp, response_body_temp)
		elif attack_method == "xss_protection_check":
    			result = xss_protection_check(url, method, response_headers_temp, response_body_temp)
		elif attack_method == "x_frame_options_check":
    			result = x_frame_options_check(url, method, response_headers_temp, response_body_temp)
		elif attack_method == "x_content_type_options_check":
    			result = x_content_type_options_check(url, method, response_headers_temp, response_body_temp)
		elif attack_method == "hsts_check":
    			result = hsts_check(url, method, response_headers_temp, response_body_temp)
		elif attack_method == "cookies_check":
				result = cookies_check(response_cookies_temp, url, method, response_headers_temp, response_body_temp)
		elif attack_method == "check_version_disclosure":
    			result = check_version_disclosure(url, method, response_headers_temp, response_body_temp)
		return result




def csp_check(url, method, header, body):
    	# checks if csp header is implemented
		if 'Content-Security-Policy' not in header:
			attack_result = { "id" : 1, "url" : url, "alert": "CSP Header Missing", "impact": "Low", "res_headers": header ,"res_body": body}
			return attack_result

		
def xss_protection_check(url, method, header, body):
    	# checks if xss-protection is enabled and configured correctly
	if 'X-XSS-Protection' not in header:
		attack_result = { "id" : 2, "url" : url, "alert": "X-XSS-Protection Header Missing", "impact": "Low", "res_headers": header ,"res_body": body}
	else:
		xss_protection = header['X-XSS-Protection']
		xss_protection = str(xss_protection.replace(" ", "")) # remove space
		if xss_protection == "0":
			attack_result = { "id" : 2.1, "url" : url, "alert": "X-XSS-Protection Header Disabled", "impact": "Low", "res_headers": header ,"res_body": body}			
		elif xss_protection != "1;mode=block": 
			attack_result = { "id" : 2.2, "url" : url, "alert": "X-XSS-Protection Header not securly implemented", "impact": "Low", "res_headers": header ,"res_body": body}
	return attack_result


def x_frame_options_check(url, method, header, body):
    	# check if X-Frame-Options header is present
	if 'X-Frame-Options' not in header:
		attack_result = { "id" : 3, "url" : url, "alert": "X-Frame-Options Header Missing", "impact": "Low", "res_headers": header ,"res_body": body}
		return attack_result


def x_content_type_options_check(url, method, header, body):
    	# check if Content-Type-Options header is present
	if 'X-Content-Type-Options' not in header:
		attack_result = { "id" : 4,  "url" : url, "alert": "X-Content-Type-Options Header Missing", "impact": "Low", "res_headers": header ,"res_body": body}
		return attack_result


def hsts_check(url, method, header, body):
    	# check if Strict-Transport-Security header is present
	if 'Strict-Transport-Security' not in header:
		attack_result = { "id" : 5, "url" : url, "alert": "Strict-Transport-Security Header Missing", "impact": "Low", "res_headers": header ,"res_body": body}
		return attack_result


def cookies_check(cookies, url, method, header, body):
    	# check if cookies are marked secure and httponly
	for cookie in cookies:
		if not cookie.secure or not cookie.has_nonstandard_attr('HttpOnly'):
			attack_result = { "id" : 6, "url" : url, "alert": "Cookie not marked secure or httponly", "impact": "Low", "res_headers": header ,"res_body": body}
			return attack_result
			


def check_version_disclosure(url, method, header, body):
    	# check if any of the headers in the list discloses version information
	version_headers = ["Server", "X-Powered-By", "X-AspNet-Version"]
	for each_version_header in version_headers:
		if each_version_header in header:
			header_value = header[each_version_header]
			if bool(re.search('\d', header_value)):    #checks if the header has any digit.  
				attack_result = { "id" : 7, "url" : url, "alert": "Server Version Disclosure", "impact": "Low", "res_headers": header ,"res_body": body}
				return attack_result
				