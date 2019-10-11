import common.requests_generic as rg
import re

result = ''

def sql_injection_initial(url, method, header_value, body_value, sqlmap_url, id_scan=None):
    result = sqlmap_get_status(sqlmap_url)

def sqlmap_get_status(sqlmap_url):
    try:
        sqlmap_status = rg.get(sqlmap_url)
        if 'Nothing here' in sqlmap_status.text:
            print('Sqlmap em execução')
            return True
    except:
        result = sqlmap_start_process()
        return result