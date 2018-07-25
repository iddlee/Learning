import pymysql
# 获取连接对象

conn = pymysql.Connect(
    host='10.35.165.217',  # MySQL所在的主机地址
    port=3306,  # MySQL的默认端口
    user='root',  # 连接MySQL的用户名
    passwd='123456',  # 连接MySQL的密码
    db='mydb',  # 要进入的数据库
    charset='utf8',  # 连接的编码
)
cursor = conn.cursor()  # 通过连接对象获取游标对象（用来操作数据库）
sql = "insert into student(stuname, sex, score, class_id)values('%s', '%s', %.1f, %d)"
data = ("欧阳锋", "男", 98, 1)
cursor.execute(sql % data)  # 将SQL发送给MySQL服务器，执行SQL语句
conn.commit()  # 提交事务
print("执行成功！")
cursor.close()  # 关闭游标对象
conn.close()  # 关闭连接对象
