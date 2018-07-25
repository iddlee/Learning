import pymysql
conn = pymysql.Connect(
    host='10.35.165.217',  # MySQL所在的主机地址
    port=3306,  # MySQL的默认端口
    user='root',  # 连接MySQL的用户名
    passwd='123456',  # 连接MySQL的密码
    db='mydb',  # 要进入的数据库
    charset='utf8',  # 连接的编码
)

cursor = conn.cursor()  # 获取游标对象
sql = "select stuid, stuname, sex, score from student where score >= %d"
cursor.execute(sql % 60)
# cursor.execute(sql % 1) 这样也可以
results = cursor.fetchall()  # 获取多条数据，返回的是一个大元组，大元组里的每个元素是一个小元组，每个小元组代表一条记录
print("学号   姓名   性别   成绩")
for result in results:
    print(result[0], "  ", result[1], "  ", result[2], "  ", result[3])
cursor.close()
conn.close()
