#Q3:
'''
def if_it_is_palindrome(word1):
    if word1 == word1[::-1]:
        return True
    else:
        return False

x1 = input("Please input your word:")

if if_it_is_palindrome(x1) == True:
    print("Yes, it is a Palindrome.")
else:
    print("No, it is not a Palindrome")
'''

#Q4:
'''
class TestPalindromeFunction(TestCase):
    def It_is_right(self):
        expected = True
        result = if_it_is_palindrome(word1='madam')
        self.assertEqual(expected, result)

    def It_is_wrong(self):
        expected = False
        result = if_it_is_palindrome(word1='sir')
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()

My explanation:
Because for my function, there are only two situations (yes or no), so I just need a case of yes(true) and another case of no(false), and those could include all the possible situations.
'''

#Q7
'''
We need a python file called config.py to storage the HOST, USER and PASSWORD of our MySql.
And we should create another python file and using these codes:
import mysql.connector
from config import USER, PASSWORD, HOST

def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx

def get_all_records():
    try:
        db_name = 'tests' 
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: {}".format(db_name))

        query = """SELECT * FROM abcdefgh"""
        cur.execute(query)
        results = cur.fetchall()

        for i in results:
            print(i)

        cur.close()

    except Exception:
        raise DbConnectionError('Failed to read data')

    finally:
        if cur:
            cur.close()

        if db_connection:
            db_connection.close()
            print("DB connection closed")
def main():
    pass
    get_all_records()

if __name__ == '__main__':
    main()
Before we run the program in Python, we need to run that DB in MySQL first, and then run these Python codes.

Fetch / Insert data into DB tables from a python program is similar: (I will take an saling DB as an example):
import pandas as pd
import pymysql

filepath = 'C:\ProgramData.xls'
data = pd.read_excel(filepath)
db = pymysql.connect('localhost','root','1234','python_analysis')
cursor = db.cursor()
try:
    cursor.execute('create table ProgramData(num int primary key,date datetime, sale float )')
except:
    print('The DB has been created')

query = """insert into catering_sale (num, date, sale) values (%s,%s,%s)"""

for r in range(0, len(data)):
    num = data.ix[r,0]
    date = data.ix[r,1]
    sale = data.ix[r,2]
    values = (int(num), str(date), float(sale))
    cursor.execute(query, values)

cursor.close()
db.commit()
db.close()

db = pymysql.connect('localhost','root','1234','python_anylysis')
cursor = db.cursor()
cursor.execute('''select * from PythonData'''')
results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
db.commit()
db.close()

'''
