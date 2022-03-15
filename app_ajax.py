from importlib import import_module
from unittest import result
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime
import pymysql

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

def select_user():
    cursor.execute((
        "select u.login_id, u.user_name, c.company_name "
        "from user_sdhan as u "
        "left join company_sdhan as c "
        "on u.company_id = c.company_id "
        "order by login_id ASC"
    ))
    result = cursor.fetchall()
    return { "result" : result }

def select_login_id(login_id):
    cursor.execute((
        "select u.login_id, u.user_name, c.company_name "
        "from user_sdhan as u "
        "left join company_sdhan as c "
        "on u.company_id = c.company_id "
        "where login_id like '" + login_id + "' "
        "limit 1;"
    ))
    result = cursor.fetchall()
    return { "result" : result }

def select_company_name():
    cursor.execute((
        "select company_id, company_name "
        "from company_sdhan "
    ))
    result = cursor.fetchall()
    return { "result" : result }

def delete_user(login_id):
    cursor.execute((
        "delete from user_sdhan "
        "where login_id like '" + login_id + "' "
        "limit 1;"
    ))
    connection.commit()
    return "0"

def insert_user(login_id, user_name, company_name):
    cursor.execute((
        "insert into user_sdhan(login_id, user_name, company_id) "
        "values ('" + login_id + "','" + user_name + "','" + company_name + "');"
    ))
    connection.commit()
    return "0"

def update_user(login_id, user_name, company_name):                                
    cursor.execute((
        "update user_sdhan "
        "set user_name='" + user_name + "', company_id='" + company_name + "' "
        "where login_id like '" + login_id + "' "
        "limit 1;"
    ))
    connection.commit()
    return "0"

@app.route('/select', methods=['GET'])
def select_user_api():
    return select_user()

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

@app.route('/insert/company_name', methods=['GET'])
def insert_company_name_api():
    return select_company_name()

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


# company_sdhan
def select_company():
    cursor.execute((
        "select company_id, company_name "
        "from company_sdhan "
        "order by company_id ASC"
    ))
    result = cursor.fetchall()
    return { "result" : result }

def select_company_id(company_id):
    cursor.execute((
        "select company_id, company_name "
        "from company_sdhan "
        "where company_id like '" + company_id + "' "
        "limit 1;"
    ))
    result = cursor.fetchall()
    return { "result" : result }

def delete_company(company_id):
    cursor.execute((
        "delete from company_sdhan "
        "where company_id like '" + company_id + "' "
        "limit 1;"
    ))
    connection.commit()
    return "0"

def insert_company(company_id, company_name):
    cursor.execute((
        "insert into company_sdhan(company_id, company_name) "
        "values ('" + company_id + "','" + company_name + "');"
    ))
    connection.commit()
    return "0"

def update_company(company_id, company_name):                                
    cursor.execute((
        "update company_sdhan "
        "set company_name='" + company_name + "' "
        "where company_id like '" + company_id + "' "
        "limit 1;"
    ))
    connection.commit()
    return "0"


@app.route('/company/select', methods=['GET'])
def select_company_api():
    return select_company()

@app.route('/company/select/company_id', methods=['GET'])
def select_company_id_api():
    company_id = request.args.get('company_id')
    return select_company_id(company_id)

@app.route('/company/delete', methods=['POST'])
def delete_company_api():
    company_id = request.form['company_id']
    return delete_company(company_id)

@app.route('/company/insert', methods=['POST'])
def insert_company_api():
    company_id = request.form['company_id']
    company_name = request.form['company_name']
    return insert_company(company_id, company_name)

@app.route('/company/update', methods=['POST'])
def update_company_api():
    company_id = request.form['company_id']
    company_name = request.form['company_name']
    return update_company(company_id, company_name)


@app.route('/company/list_view', methods=['GET', 'POST'])
def company_list_view():
    now = datetime.now()
    return render_template('company_list_view.html', now=now)

@app.route('/company/detail_view/<company_id>', methods=['GET', 'POST'])
def company_detail_view(company_id):
    now = datetime.now()
    return render_template('company_detail_view.html', company_id=company_id, now=now)

@app.route('/company/insert_view', methods=['GET', 'POST'])
def company_insert_view():
    now = datetime.now()
    return render_template('company_insert_view.html', now=now)        

@app.route('/company/update_view/<company_id>', methods=['GET', 'POST'])
def company_update_view(company_id):
    now = datetime.now()
    return render_template('company_update_view.html', company_id=company_id, now=now)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3001', debug=True)
