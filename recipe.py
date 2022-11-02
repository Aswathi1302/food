import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='foodrecipe')
mycursor=mydb.cursor()
from secrets import choice


while True:
    print("select an option from the menu")
    print("1. add item")
    print("2.view item")
    print("3.search item")
    print("4.upadte item")
    print("5. delete item")
    print("6.exit")
    
    choice=int(input("enter your choice:-"))
    if(choice==1):
        print("ADD ITEM")
        foodcode=input("enter a food code:::---")
        name=input("enter a food name:::---")
        description=input("description:::---")
        preparedby=input("prepared by:::---")
        incrediance=input("ingredients:::---")
        sql="INSERT INTO `recipe`(`foodcode`, `name`, `description`, `preparedby`, `incrediance`) VALUES (%s,%s,%s,%s,%s)"
        data=(foodcode,name, description,preparedby,incrediance)
        mycursor.execute(sql,data)
        mydb.commit()
        print("values entared successfully.......!")
    elif(choice==2):
        print("VIEW ITEM")  
        sql="SELECT * FROM `recipe`  "
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i) 
    elif(choice==3):
        print("SEARCH ITEM")
    elif(choice==4):
        print("UPDATE ITEM") 
    elif(choice==5) :
        print("DELETE ITEM")
    elif(choice==6):
        break      