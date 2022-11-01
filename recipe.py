from secrets import choice


while True:
    print("select an option from the menu")
    print("1. add item")
    print("2.view item")
    print("3.search item")
    print("4.upadte item")
    print("5. delete item")
    print("6.exit")
    
    choice=int(input("enter your choice"))
    if(choice==1):
        print("ADD ITEM")
    elif(choice==2):
        print("VIEW ITEM")    
    elif(choice==3):
        print("SEARCH ITEM")
    elif(choice==4):
        print("UPDATE ITEM") 
    elif(choice==5) :
        print("DELETE ITEM")
    elif(choice==6):
        break      