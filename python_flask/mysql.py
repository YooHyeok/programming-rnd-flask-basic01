from flask import Flask, jsonify
import pymysql # 모듈 import

db = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='board', charset='utf8') # MySQL 데이터베이스 연결 설정

app = Flask(__name__)

@app.route('/articles')
def all_articles():
    cursor = db.cursor() # 데이터 접근
    sql = "SELECT * FROM article ORDER BY id DESC LIMIT 10"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    return jsonify(result)

if __name__ == '__main__':
    app.run()