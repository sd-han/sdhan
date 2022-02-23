from flask import Flask, request, jsonify
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
 
def query_user(login_id, user_name):
    cursor.execute("SELECT login_id FROM user WHERE login_id LIKE '%" + login_id + "%' OR user_name LIKE '%" + user_name + "%'")
    result = cursor.fetchall()

    return { "result" : result }


@app.route('/api/v0/user/search',  methods=['GET'])
def search_user():
    login_id = request.args.get('login_id')
    user_name = request.args.get('user_name')
    
    return query_user(login_id, user_name)


@app.route('/api/v0/user/search2',  methods=['POST'])
def user_juso2():
    
    params = request.get_json()
    temp1 = params['login_id']
    temp2 = params['user_name']

    return query_user(temp1, temp2)

# temp1 = request.args.get('name', "user01")
# temp2 = request.args.get('juso', "평택시")
# print(sql)
# /api/v0/user/search?login_id=xxx&user_name=yyy
# cursor.execute(sql)
# result = cursor.fetchall()
# return result
# return temp1 + "-" + temp2

# @app.route('/test')
# def get_user_list():
#     cursor = mysql.get_db().cursor()

#     # User Info : followers, followings, last updated time
#     cursor.execute("SELECT * FROM user_list")
#     data = json.dumps(cursor.fetchall())
    
#     return data

# sql = "SELECT * FROM user \n WHERE login_id LIKE %<xxx>% AND WHERE user_name LIKE %<yyy>% "

if __name__ == "__main__":
    app.run(debug=True)



# @app.route('/api/v0/user/search?login_id=<login_id>&user_name=<user_name>')
# def search():
#     login_id = request.args.get('login_id')
#     print(login_id)
#     user_name= request.args.get('user_name')
#     print(user_name)
#     return ({"result": "ok"})

# @app.route('/api/v0/user/search2', methods=['GET', 'POST'])
# def search():
#     login_id = request.args.get('login_id')
#     print(login_id)
#     user_name= request.args.get('user_name')
#     print(user_name)



# cursor = connection.cursor()

# @app.route('/api/v0/user/search?login_id=xxx&user_name=yyy')
# def string_return(xxx, yyy):

#     sql = "SELECT * FROM user \n WHERE login_id LIKE <xxx> AND WHERE user_name LIKE <yyy> "
#     cur.execute(sql)
#     a_var = sql
#     print(a_var)
#     return '%s' %a_var

# @app.route('/s/<string_value>')
# def string_return(string_value):
#     a_var = string_value
#     print(a_var)
#     return '%s' %string_value

# @app.route('/api/v0/user/search?login_id=<xxx>&user_name=<yyy>') #test api
# def hello_world():
#     return jsonify({"result": "hsd"})

# sql = "SELECT * FROM user \n WHERE login_id LIKE '%<xxx>%' OR user_name LIKE 'saa%' "

# with connection:
#     with connection.cursor() as cur:
#         cur.execute(sql)
#         result = cur.fetchall()
#         for data in result:
#             print(data)
           
# try:
#     with connection.cursor() as cursor:  
#         sql = "SELECT * FROM user WHERE login_id = 'a%' LIKE 's%' "
#         cursor.execute(sql)
#         result = cursor.fetchall()
        
#         for i in result:
#             print(i)
# finally:
#     connection.close()

# @app.route('/') #test api
# def hello_world():
#     return ({"result": "ok"})
#     # return 'Hello, World!'


# @app.route('/city')
# def population():
#     pop_info = {'Seoul' : 1, 
#             'Busan' : 2,
#             'Gyeonggi' : 3,
#             }
#     return jsonify(pop_info)

# @app.route('/echo_call', methods=['POST']) #post echo api
# def post_echo_call():
#     param = request.get_json()
#     return jsonify(param)


    
