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
    print("6. search item by name")
    print("7.display count")
    print("9.exit")
    
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
        foodcode=input("enter a food code:-")
        sql="SELECT * FROM `recipe` WHERE  `foodcode`='"+foodcode+"'"
        mycursor.execute(sql)
        result=mycursor.fetchall()
        print(result) 
    elif(choice==4):
        print("UPDATE ITEM") 
        foodcode=input("enter a food code:::---")
        name=input("enter a food name to be updated:::---")
        description=input("description to be updated:::---")
        preparedby=input("prepared by to be updated:::---")
        incrediance=input("ingredients to be updated:::---")
        sql="UPDATE `recipe` SET `name`='"+name+"',`description`='"+description+"',`preparedby`='"+preparedby+"',`incrediance`='"+incrediance+"' WHERE `foodcode`="+foodcode
        mycursor.execute(sql)
        mydb.commit()
        print("Data updated successfully....")
    elif(choice==5) :
        print("DELETE ITEM")
        foodcode=input("enter a food code:::---")
        sql="DELETE FROM `recipe` WHERE `foodcode`="+foodcode
        mycursor.execute(sql)
        mydb.commit()
        print("Data deleted successfully..") 
    elif(choice==6):
        print("search a food item  by character") 
        character=input("enter a character:-")
        sql="SELECT `foodcode`, `name`, `description`, `preparedby`, `incrediance` FROM `recipe` WHERE `name` LIKE '"+character+"%'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)  
    elif(choice==7):
        print("Display count of total number of food items prepared by different cook") 
        sql="SELECT COUNT(*),preparedby FROM `recipe` GROUP BY preparedby" 
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i) 
    elif(choice==9):
        break      