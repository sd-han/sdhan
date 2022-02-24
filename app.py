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

# @app.route('/table2')
# def table_to_html2():
#     cursor.execute((
#         "SELECT user.login_id, user.user_name, company.company_name "
#         "FROM user "
#         "    INNER JOIN company ON user.company_id = company.company_id "
#         "ORDER BY login_id ASC"
#     ))
#     result = cursor.fetchall()
    
#     return { "result" : result }

@app.route('/file/<filename>')
def file(filename):
    return send_from_directory('static', filename)


@app.route('/table')
def table_to_html():
    cursor.execute((
        # "SELECT user.login_id, user.user_name, company.company_name "
        # "FROM user "
        "SELECT u.login_id, u.user_name, c.company_name "
        "FROM user AS u"
        "    INNER JOIN company AS c ON u.company_id = c.company_id "
        "ORDER BY login_id ASC"
    ))
    result = cursor.fetchall()

    data1 = (
        '<!DOCTYPE html>'
        '<html>'
        '<head>'
        '<title>Page Title</title>'
        '</head>'
        '<body>'
        '<table>'
            '<tr>'
                '<th>login_id</th>'
                '<th>user_name</th>'
                '<th>company_name</th>'
            '</tr>'
    )
    
    data2 = ('')
    
    for o in result:
        data2 += '<tr>'
        data2 += '<td>' + o[0] + '</td>'
        data2 += '<td>' + o[1] + '</td>'
        data2 += '<td>' + o[2] + '</td>'
        data2 += '</tr>'
    
    data3 = (
        '</table>'
        '</body>'
        '</html>'
    )

    return data1 + data2 + data3


def query_user(login_id, user_name, company_name):
    cursor.execute((
        "SELECT user.login_id, user.user_name, company.company_name "
        "FROM user "
        "    INNER JOIN company ON user.company_id = company.company_id "
        "WHERE login_id LIKE '%" + login_id + "%' OR user_name LIKE '%" + user_name + "%' "
        "    OR company_name LIKE '%" + company_name + "%' "
        "ORDER BY login_id ASC"
    ))

    result = cursor.fetchall()

    return { "result" : result }


@app.route("/homepage")
def text_html():
    login_id = request.args.get('login_id')
    user_name = request.args.get('user_name')
    company_name = request.args.get('company_name')
    return (
        '<!DOCTYPE html>'
        '<html>'
        '<head>'
        '<title>Page Title</title>'
        '</head>'
        '<body>'
        '<h1>This is a Heading</h1>'
        '<p>This is a paragraph.</p>'
        '<p>This is a login_id : ' + login_id + '</p>'
        '<p>This is a user_name : ' + user_name + '</p>'
        '<p>This is a company_name : ' + company_name + '</p>'
        '</body>'
        '</html>'
    )

@app.route('/api/v0/user/search', methods=['GET'])
def search_user():
    login_id = request.args.get('login_id')
    user_name = request.args.get('user_name')
    company_name = request.args.get('company_name')
    return query_user(login_id, user_name, company_name)

@app.route('/api/v0/user/search2',  methods=['POST'])
def search_user2():
    params = request.get_json()
    login_id = params['login_id']
    user_name = params['user_name']
    company_name = params['company_name']
    return query_user(login_id, user_name, company_name)

if __name__ == "__main__":
    app.run(debug=True)
