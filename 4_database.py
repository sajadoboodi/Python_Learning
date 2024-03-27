import mysql.connector
import sys
cnx = mysql.connector.connect(user='root',password='Admin@4321',
                              database = 'learning_mysql')
#cnx.charset.encode("utf-8")
cursor = cnx.cursor()
cursor.execute("select * FROM learning_mysql.new_table;")
record = cursor.fetchall()
#print(record)
my_list = []
for row in record:
    my_list.append(row)
    print(row)
#print('#'*10)
#print(my_list[0])
