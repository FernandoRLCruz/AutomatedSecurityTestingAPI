import common.requests_generic as rg
import re
import subprocess
import time
import json

result = ''
api_header = {'Content-Type' : 'application/json'}

def sql_injection_initial(url, method, header_value, body_value, sqlmap_url, id_scan=None):
    result = sqlmap_get_status(sqlmap_url)
    if result is True:
        taskid = get_new_task_id(sqlmap_url)
    if taskid:
        # Taskid is created.
        set_option_status = set_options_list(url,method,header_value,body_value,taskid, sqlmap_url)
        if set_option_status is True:
            # Everything is set to start the scan
            start_scan_result = start_scan(taskid)
            if start_scan_result is True:
                print("SQLi - Scan started.")
                result = scan_status(taskid)
                if result is True:
                    # API is vulnerable
                    print ("[+] is vulnerable to SQL injection")
                    attack_result = { "id" : 10, "scanid" : scanid, "url" : url, "alert": "SQL injection", "impact": "High", "req_headers": headers, "req_body":body, "res_headers": "NA" ,"res_body": "NA", "log" : scan_data}
                    dbupdate.insert_record(attack_result)

        else:
            logs.logging.info("Sqli - Failed to create a task.") 

        task_result = delete_task(taskid)
        if task_result is True:
            # Task deleted successfully
            logs.logging.info("SQLi - Task deleted: %s",taskid)


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
            out_temp = str(out)
            location_path = out_temp[out_temp.find('Location:')+10:]
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
        return      

def get_new_task_id(sqlmap_url):
    # Create a new task for scan
    new_task_url = sqlmap_url + "/task/new"
    new_task = rg.send_request_generic(new_task_url,"GET", api_header)
    if new_task.status_code == 200:
        return json.loads(new_task.text)['taskid']

def set_options_list(url, method, headers, body, task_id, sqlmap_url):
    # Setting up url,headers, body for scan
    options_set_url = sqlmap_url + "/option/" + task_id + "/set"
    data = {}
    data['url'], data['method'], data['headers'] = url, method, headers
    if method.upper() == 'POST' or method.upper() == 'PUT':
        if headers['Content-type'] == 'application/json':
            body=json.dumps(body)
        data['data'] = body
    options_list = rg.send_request_generic(options_set_url, "POST", api_header, data)
    if options_list.status_code == 200:
        return json.loads(options_list.text)['success']        