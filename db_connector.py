"""
connector for the DB connection
"""
import pymysql

db_user = 'LXf29u1CXu'
my_db = pymysql.connect(host='remotemysql.com', port=3306, user=db_user, passwd='0BRRO69NXP', db='LXf29u1CXu', autocommit=True)
my_db_cursor = my_db.cursor()

def execute(sql):
    my_db_cursor.execute(sql)
    return my_db_cursor

def select(fields, table, where):
    return(execute(f"select {fields} from {db_user}.{table} where {where} ;"))

def insert(table, fields, values ):
    return(execute(f"insert into {db_user}.{table}({fields}) values ({values})  ;"))

def update(table, set , where ):
    return(execute(f"update  {db_user}.{table} set {set} where {where};"))

def delete(table, where ):
    return(execute(f"delete from {db_user}.{table} where {where};"))

if __name__ == '__main__':
    mycon = select("'Y'","users", "user_id = 2")
    print(mycon.rowcount)
