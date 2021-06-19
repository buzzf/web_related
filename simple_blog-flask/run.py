#!/usr/bin/env python
# coding:utf8
import time
from flask import *
import warnings
warnings.filterwarnings("ignore")
import pymysql
from config import *



app = Flask(__name__)
app.config.from_object(__name__)

# 连接数据库
def connectdb():
	db = pymysql.connect(host=HOST, user=USER, passwd=PASSWORD, db=DATABASE, port=PORT, charset=CHARSET, cursorclass = pymysql.cursors.DictCursor)
	db.autocommit(True)
	cursor = db.cursor()
	return (db,cursor)

# 关闭数据库
def closedb(db,cursor):
	db.close()
	cursor.close()

# 首页
@app.route('/')
def index():
	return render_template('index.html')


# 文章列表
@app.route('/list')
def list():
	(db, cursor) = connectdb()
	cursor.execute("select * from post")
	posts = cursor.fetchall()
	for x in range(0, len(posts)):
		posts[x]['timestamp'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(posts[x]['timestamp'])))
	closedb(db, cursor)
	return render_template('list.html', posts=posts)


# 处理文章提交
@app.route('/handle', methods=['POST'])
def handle():
	if request.method == 'POST':
		title = request.form.get('title', None)
		content = request.form.get('content', None)
		print(title, content)
		(db, cursor) = connectdb()
		cursor.execute("insert into post(title, content, timestamp) VALUES(%s, %s, %s)", [title, content, int(time.time())])
		closedb(db, cursor)
	return redirect(url_for('list'))


# 文章内容
@app.route('/article/<article_id>')
def article(article_id):
	(db, cursor) = connectdb()
	cursor.execute("select * from post where id=%s",[article_id])
	article = cursor.fetchone()
	article['timestamp'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(article['timestamp'])))
	closedb(db, cursor)
	return render_template('article.html', article=article)

if __name__ == '__main__':
	app.run(debug=True)