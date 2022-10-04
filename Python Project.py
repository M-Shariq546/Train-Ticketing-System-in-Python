#Main Menu
print("-:Select Your Choice:-")
print("1- New Entry")
print("2- View Entry")
print("3- Delete Entry")
print("4- Exit")
#Class of train
class train():
    def __init__(self , name , age , gender , tname , tnum , price , total):
        self.name = name 
        self.age = age
        self.gender = gender
        self.tname = tname
        self.tnum = tnum
        self.price = price
        self.total = total
        #Data Storing line in file
        with open("E:\AIC course\AIC course\Train data.txt", "a") as f:
            f.write("<======================================================>"+ "\n")
            f.write("Name : " + self.name + "\n")
            f.write("Age : "  +self.age+ "\n")
            f.write("Gender : " +self.gender+ "\n")
            f.write("Train Name : " +self.tname+ "\n")
            f.write("No Of Seats : " +self.tnum+ "\n")
            f.write("Per Seat Price : " +self.price+ "\n")
            f.write("Total Price : " +self.total+ "\n")
            f.write("<======================================================>"+ "\n")
    def readData():    
        with open("E:\AIC course\AIC course\Train data.txt" , "r") as f:
            data = f.read()
            print(data)
            



#Main Function

ch = int(input("Enter your Choice From above Menu: "))
if(ch == 1):
    n = str(input("Enter the passenger's Name : "))
    a = str(input("Enter the Passenger's age : "))
    g = str(input("Enter the gender : "))
    tn = str(input("Enter the train name : "))
    tnu = str(input("Enter the number of seats : "))
    p = str(input("Enter the price of 1 seat : "))
    t = str(int(tnu) * int(p))
    print("Total Payable Price : " , t)
    t1 = train(n , a , g , tn , tnu , p , t)
    if(ch== 2):
        t1.readData()
else:
    exit()