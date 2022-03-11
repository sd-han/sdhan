from importlib import import_module
from unittest import result
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import pymysql
import json
import urllib.request

app = Flask(__name__)
CORS(app)

connection = pymysql.connect(
    user='YT', 
    passwd='~!blue0427()', 
    host='dev1.whyit.co.kr', 
    port=48092,
    db='porta_siem', 
    charset='utf8'
)

cursor = connection.cursor()

def query_user(login_id, user_name, company_name):
    cursor.execute((
        "select login_id, user_name, company_name "
        "from user_sdhan "
        # "where login_id like '%" + login_id + "%' or user_name like '%" + user_name + "%' "
        # "    or company_name like '%" + company_name + "%' "
        "order by login_id ASC"
    ))
    result = cursor.fetchall()
    return { "result" : result }

def query_login_id(login_id):
    cursor.execute((
        "select login_id, user_name, company_name "
        "from user_sdhan "
        "where login_id like '" + login_id + "'"
        "limit 1;"
    ))
    result = cursor.fetchall()
    return { "result" : result }

def delete_user(login_id):
    cursor.execute((
        "delete from user_sdhan "
        "where login_id like '" + login_id + "'"
        "limit 1;"
    ))
    connection.commit()
    return "0"

def insert_user(login_id, user_name, company_name):
    cursor.execute((
        "insert into user_sdhan(login_id, user_name, company_name) "
        "values ('" + login_id + "','" + user_name + "','" + company_name + "');"
    ))
    connection.commit()
    return "0"

def update_user(login_id, user_name, company_name):                                
    cursor.execute((
        "update user_sdhan "
        "set user_name='" + user_name + "', company_name='" + company_name + "' "
        " where login_id like '" + login_id + "'"
        "limit 1;"
    ))
    connection.commit()
    return "0"

@app.route('/read', methods=['GET'])
def sql_search_user():
    login_id = request.args.get('login_id')
    user_name = request.args.get('user_name')
    company_name = request.args.get('company_name')
    return query_user(login_id, user_name, company_name)

@app.route('/read/login_id', methods=['GET'])
def sql_search_login_id():
    login_id = request.args.get('login_id')
    return query_login_id(login_id)

@app.route('/delete', methods=['GET'])
def sql_delete_user():
    login_id = request.args.get('login_id')
    return delete_user(login_id)

@app.route('/insert', methods=['GET'])
def sql_insert_user():
    login_id = request.args.get('login_id')
    user_name = request.args.get('user_name')
    company_name = request.args.get('company_name')
    return insert_user(login_id, user_name, company_name)

@app.route('/update', methods=['GET'])
def sql_update_user():
    login_id = request.args.get('login_id')
    user_name = request.args.get('user_name')
    company_name = request.args.get('company_name')
    return update_user(login_id, user_name, company_name)

@app.route('/api', methods=['GET'])
def test_api():
    cursor.execute((
        "SELECT login_id, user_name, company_name "
        "from user_sdhan "
        "ORDER BY login_id ASC"
    ))
    result = cursor.fetchall()
    
    return { "result" : result }

@app.route('/ajax2/<variable>')
def test_jinja(variable):
    value_list = ['list1', 'list2', 'list3']
    
    return render_template('jinja.html', name1=variable, values=value_list)

@app.route('/user/list_view', methods=['GET', 'POST'])
def list_view():
    url = 'http://www.daum.net'
    date = urllib.request.urlopen(url).headers['Date']
    month = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', \
    'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
    d, m , y, hour, min, sec = date[5:7], month[date[8:11]], date[12:16], date[17:19], date[20:22], date[23:25]
    hour_int = int(hour)
    hour_result = hour_int + 9
    result_Time = [d, m, y, hour_result, min, sec]
    return render_template('list_view.html', d=d, m=m, y=y, hour=hour, min=min, sec=sec, hour_result=hour_result)

@app.route('/user/detail_view/<login_id>', methods=['GET', 'POST'])
def detail_view(login_id):
    url = 'http://www.daum.net'
    date = urllib.request.urlopen(url).headers['Date']
    month = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', \
    'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
    d, m , y, hour, min, sec = date[5:7], month[date[8:11]], date[12:16], date[17:19], date[20:22], date[23:25]
    hour_int = int(hour)
    hour_result = hour_int + 9
    return render_template('detail_view.html', login_id = login_id, d=d, m=m, y=y, hour=hour, min=min, sec=sec, hour_result=hour_result)

@app.route('/user/insert_view', methods=['GET', 'POST'])
def insert_view():
    url = 'http://www.daum.net'
    date = urllib.request.urlopen(url).headers['Date']
    month = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', \
    'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
    d, m , y, hour, min, sec = date[5:7], month[date[8:11]], date[12:16], date[17:19], date[20:22], date[23:25]
    hour_int = int(hour)
    hour_result = hour_int + 9
    return render_template('insert_view.html', d=d, m=m, y=y, hour=hour, min=min, sec=sec, hour_result=hour_result)        

@app.route('/user/update_view/<login_id>', methods=['GET', 'POST'])
def update_view(login_id):
    url = 'http://www.daum.net'
    date = urllib.request.urlopen(url).headers['Date']
    month = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', \
    'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
    d, m , y, hour, min, sec = date[5:7], month[date[8:11]], date[12:16], date[17:19], date[20:22], date[23:25]
    hour_int = int(hour)
    hour_result = hour_int + 9
    return render_template('update_view.html', login_id = login_id, d=d, m=m, y=y, hour=hour, min=min, sec=sec, hour_result=hour_result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3001', debug=True)
