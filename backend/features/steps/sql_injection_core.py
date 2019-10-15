import common.requests_generic as rg
import re
import subprocess
import time

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

def sqlmap_start_process():
    try:
        p = subprocess.Popen(["pip", "show", "sqlmap"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            location_path = out[out.find('Location:')+10:]
            sqlmap_path = location_path[:location_path.fin('\n')] + '/sqlmap/sqlmapapi.py'
            if sqlmap_path:
                start_sqlmap_status = subprocess.Popen(['python', sqlmap_path, '-s'],stdout=subprocess.PIPE)
                time.sleep(5)
                while True:
                    line = start_sqlmap_status.stdout.readline()
                    if "Admin" in line:
                        print("sqlmap is started")
                        return True
    except:
        print('Failed to start sqlmap')
        pass      