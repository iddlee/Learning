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
sql = "select stuid, stuname, sex, score from student where stuid = %d"
cursor.execute(sql % (1,))
# cursor.execute(sql % 1) 这样也可以
result = cursor.fetchone()  # 获取单条数据，返回一个元组，元组里的每个元素是该条记录的具体信息
print("查询到的结果是：", result)
print("学号：", result[0], "姓名：", result[1], "性别：", result[2], "成绩：", result[3])
cursor.close()
conn.close()
