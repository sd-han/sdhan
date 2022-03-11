from importlib import import_module
from unittest import result
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime
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

def select_user(login_id, user_name, company_name):
    cursor.execute((
        "select login_id, user_name, company_name "
        "from user_sdhan "
        "order by login_id ASC"
    ))
    result = cursor.fetchall()
    return { "result" : result }

def select_login_id(login_id):
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


@app.route('/select', methods=['GET'])
def select_user_api():
    login_id = request.args.get('login_id')
    user_name = request.args.get('user_name')
    company_name = request.args.get('company_name')
    return select_user(login_id, user_name, company_name)

@app.route('/select/login_id', methods=['GET'])
def select_login_id_api():
    login_id = request.args.get('login_id')
    return select_login_id(login_id)

@app.route('/delete', methods=['POST'])
def delete_user_api():
    login_id = request.form['login_id']
    return delete_user(login_id)

@app.route('/insert', methods=['POST'])
def insert_user_api():
    login_id = request.form['login_id']
    user_name = request.form['user_name']
    company_name = request.form['company_name']
    return insert_user(login_id, user_name, company_name)

@app.route('/update', methods=['POST'])
def update_user_api():
    login_id = request.form['login_id']
    user_name = request.form['user_name']
    company_name = request.form['company_name']
    return update_user(login_id, user_name, company_name)


@app.route('/user/list_view', methods=['GET', 'POST'])
def list_view():
    now = datetime.now()
    return render_template('list_view.html', now=now)

@app.route('/user/detail_view/<login_id>', methods=['GET', 'POST'])
def detail_view(login_id):
    now = datetime.now()
    return render_template('detail_view.html', login_id=login_id, now=now)

@app.route('/user/insert_view', methods=['GET', 'POST'])
def insert_view():
    now = datetime.now()
    return render_template('insert_view.html', now=now)        

@app.route('/user/update_view/<login_id>', methods=['GET', 'POST'])
def update_view(login_id):
    now = datetime.now()
    return render_template('update_view.html', login_id=login_id, now=now)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3001', debug=True)
