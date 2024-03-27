import mysql.connector

config = {
  'user': 'root',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'learning_mysql',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cursor = cnx.cursor()
query = 'SELECT * FROM learning_mysql.new_table;'
cursor.execute(query)

for (id,title,news_text,reg_data) in cursor:
    print('Number of %s title is %s.\n%s\n%s' %(id,title,news_text,reg_data))


cnx.close()