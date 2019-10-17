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
        # return result

def sqlmap_start_process():
    try:
        p = subprocess.Popen(["pip", "show", "sqlmap"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            out_temp = str(out)
            location_path = out_temp[out_temp.find('Location:')+10:]
            # location_path = str(location_path)
            location_path_temp = location_path.split('\\n')
            sqlmap_path = location_path_temp[0] + '/sqlmap/sqlmapapi.py'
            if sqlmap_path:
                start_sqlmap_status = subprocess.Popen(['python', sqlmap_path, '-s'],stdout=subprocess.PIPE)
                time.sleep(5)
                while True:
                    line = start_sqlmap_status.stdout.readline()
                    line_temp = str(line)
                    if "Admin" in line_temp:
                        print("sqlmap is started")
                        return True
    except:
        print('Failed to start sqlmap')
        pass      