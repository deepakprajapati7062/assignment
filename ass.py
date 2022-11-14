import csv

def write():
    ch='Y'
    f=open("User.csv","w",newline='')
    wo=csv.writer(f)
    wo.writerow(["id","Firstname","Lastname","Username","E-mail","Avatar","Gender","DOB","Address"])
    while True:
        U_id=input("Enter thne id-:")
        Firstname=input("Enter your firstname-:")
        Lastname=input("Enter your lastname-:")
        Username=input("Enter your username-:")
        E_mail=input("Enter your E-mail-:")
        Avatar=input("Enter your Avatar-:")
        Gender=input("Enter your Gender-:")
        DOB=input("Enter your DOB-:")
        Address=input("Enter your Address-:")
        data=[U_id,Firstname,Lastname,Username,E_mail,Avatar,Gender,DOB,Address]
        wo.writerow(data)
        ch=input("Do you want to enter more records (y/N)-:")
        if ch in 'Nn':
            break;
    f.close()

def read():
    f=open("User.csv","r")
    ro=csv.reader(f)
    for i in ro:
        print(i)



    
write()
read()
