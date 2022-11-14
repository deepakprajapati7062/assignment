import pandas as pd

df = pd.read_csv('user.csv',index_col=False)

val = input("1: UserId \n2: Firstname \n\n Please select : ")

if(val == '1'):
    U_id = input("Enter UserId value: ")
    record = df.loc[df['U_id'] == int(U_id)]
    print(record.to_string(index= False))

elif(val == '2'):
    Firstname = input("Enter Firstname value: ")
    record = df.loc[df['Firstname'] == Firstname]
    print(record.to_string(index= False))
else:
    print("Please select valid number")
    exit
