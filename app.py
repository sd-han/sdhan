from importlib import import_module
from unittest import result
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import pymysql
import json

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

def delete_user(login_id, user_name, company_name):
    cursor.execute((
        "insert into user_sdhan (login_id, user_name, company_name) "
        "valuse '" + login_id + "','" + user_name + "','" + company_name + "')"
    ))
    return

def insert_user(login_id, user_name, company_name):
    cursor.execute((
        "insert into user_sdhan (login_id, user_name, company_name) "
        "valuse '" + login_id + "','" + user_name + "','" + company_name + "')"
    ))
    return

def update_user(login_id, user_name, company_name):
    cursor.execute((
        "insert into user_sdhan (login_id, user_name, company_name) "
        "valuse '" + login_id + "','" + user_name + "','" + company_name + "')"
    ))
    return

@app.route('/api/v0/user/search', methods=['GET'])
def search_user():
    login_id = request.args.get('login_id')
    user_name = request.args.get('user_name')
    company_name = request.args.get('company_name')
    return query_user(login_id, user_name, company_name)

@app.route('/api', methods=['GET'])
def test_api():
    cursor.execute((
        "SELECT login_id, user_name, company_name "
        "from user_sdhan "
        "ORDER BY login_id ASC"
    ))
    result = cursor.fetchall()
    
    return { "result" : result }

@app.route('/file/<filename>')
def file(filename):

    return send_from_directory('static', filename)


@app.route('/ajax/<filename>')
def send_ajax(filename):
    
    return send_from_directory('static', filename)

@app.route('/ajax2/<variable>')
def test_jinja(variable):
    value_list = ['list1', 'list2', 'list3']
    
    return render_template('jinja.html', name1=variable, values=value_list)

@app.route('/user/list_view', methods=['GET', 'POST'])
def list_view():
    cursor.execute((
        "SELECT login_id, user_name, company_name "
        "from user_sdhan "
        "ORDER BY login_id ASC"
    ))
    result = cursor.fetchall()

    return render_template('list_view.html')

@app.route('/user/detail_view', methods=['GET', 'POST'])
def detail_view():
    return render_template('detail_view.html')

@app.route('/user/insert_view', methods=['GET', 'POST'])
def insert_view():
    return render_template('insert_view.html')        

@app.route('/user/update_view', methods=['GET', 'POST'])
def update_view():
    return render_template('update_view.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3001', debug=True)
