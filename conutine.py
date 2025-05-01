print("==============================WELCOME TO MY WORLD====================================")
print("--------------------------------------------------------------------------------------")
print("SELECT YOUR OPTION:")
print("1.Creat a List")
print("2.Add Element in list")
print("3.Remove element in list")
print("4.Update Element of list")
print("5.Display Element")
print("6.Exit")
choice=int(input("Enter Your Choice:"))
l1=[]
while(choice!=6):
    if(choice==1):
        len=int(input("Enter Length of List:"))
        for i in range(1,len+1):
            ele=int(input("Enter Element:"))
            l1.append(ele)
    elif(choice==2):
        print("===================Inserting Element======================")
        print("----------------------------------------------------------")
        print("1. At specfic Location:")
        print("2. At the End of List")
        c1=int(input("Enter Your Choice:"))
        if(c1==1):
            location=int(input("Enter Location:"))
            ele=int(input("Enter Element:"))
            l1.insert(location,ele)
        else:
            ele=int(input("Enter Number:"))
            l1.append(ele)
    elif(choice==3):
        print("1.Want to Remove Particular Element:")
        print("2.Delete last Element")
        c1=int(input("Enter Your Choice:"))
        if(c1==1):
            ele=int(input("Enter Element you want to remove:"))
            l1.remove(ele)
        else:
            ele=l1.pop()
            print("Deleted Element:",ele)
            print("Deleted ")
    elif(choice==4):
        location=int(input("Enter Index to change to element:"))
        ele=int(input("Enter Element:"))
        l1.insert(location,ele)
    elif(choice==5):
        print("List:",l1)
        print("List:,")
    else:
        print("Thanks for your support")
        break
    print("SELECT YOUR OPTION:")
    print("1.Creat a List")
    print("2.Add Element in list")
    print("3.Remove element in list")
    print("4.Update Element of list")
    print("5.Display Element")
    print("6.Exit")
    choice=int(input("Enter Your Choice:"))

print("Thanks for your respone")






