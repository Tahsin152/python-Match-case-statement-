x=int(input("Enter a number :"))
match x :
    case 0 :
        print("X is zero")
    case 4 if x%2==0:
        print("X is four")
    case _ if x<0 :
        print(x,"is negative")
    case _ if x>4:
        print(x,"is getter than 4")
    case _ if x<4 :
        print(x,"is less than 4")
    