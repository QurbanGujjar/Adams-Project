# import pandas as pd
# xl = pd.ExcelFile('feb.xlsx')
# xl.sheet_names

# [u'1', u'2', u'3']

# df = xl.parse("1")
# # df=xl
# pd.DataFrame(df.iloc[2:19,0:3])
# # print(df,columns=['A','B','C','D','E','F','G','H'])



import sqlite3, csv
def insertBooker():    
    connection =sqlite3.connect('market/MumtazBrothers.db')
    cursor=connection.cursor()
    with open("booker.csv","r") as File:
        records =0
        for row in File:
            cursor.execute("insert into booker values(?,?,?)",row.split(","))
            connection.commit()
            records +=1 
    connection.close()
    print(f"{records} records Transferned")
    
def insertItem():    
    connection =sqlite3.connect('market/MumtazBrothers.db')
    cursor=connection.cursor()
    with open("item.csv","r") as File:
        records =0
        for row in File:
            cursor.execute("insert into item values(?,?,?,?,?)",row.split(","))
            connection.commit()
            records +=1 
    connection.close()
    print(f"{records} records Transferned")    
    
insertItem()
insertBooker()    