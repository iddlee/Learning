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
try:
    sql1 = "update account set money = money - 200 where accid = %d"
    sql2 = "update account set money = money + 200 where accid = %d"
    cursor.execute(sql1 % 1)
    cursor.execute(sql2 % 2)
    conn.commit()  # 提交事务
    print("转账成功")
except Exception:
    conn.rollback()  # 回滚整个事务
    print("sorry，ATM发生故障，转账失败")
finally:
    cursor.close()
    conn.close()
