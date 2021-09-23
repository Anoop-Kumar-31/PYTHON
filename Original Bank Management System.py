import mysql.connector

#This Function is Used to Display ENDSCREEN ----------------------------------------------------------
def endscreen():
     print("========================================================================================")
     print("------------------------------**Enter any given options**-------------------------------")
     print("-----------------------------------(A): Main Menu---------------------------------------")
     print("-------------------------------------(B): Exit------------------------------------------")
     print("========================================================================================")
     choice=input("Enter Any Of Above Option : ")
     if(choice=="A" or choice=="a"):
          menu()
     elif(choice=="B" or choice=="b"):
          print("#----------------------------------Have a Nice Day------------------------------------#")
     else:
          print("Invalid Choice Enter Again")
          endscreen()
          
#This Function is Used to Retrive Data From Table in DataBase -------------------------
def data():
     mydb=mysql.connector.connect(host='localhost'
                                  ,username='root'
                                  ,password='root'
                                  ,database='bank_sys')
     mycur=mydb.cursor()
     query="SELECT * FROM accounts"
     mycur.execute(query)
     my_data=mycur.fetchall()
     mydb.commit()
     mydb.close()
     return my_data

#This Function is Used to INSERT new Account in Table ----------------------------------------
def sqlcreate(n,i,bal):
     mydb=mysql.connector.connect(host="localhost"
                                   ,user="root"
                                   ,passwd="root"
                                   ,database="bank_sys")
     mycur=mydb.cursor()
     sql="INSERT INTO accounts (Names,Ids,Balance) VALUES (%s,%s,%s)"
     val=(n,i,bal)
     mycur.execute(sql,val)
     mydb.commit()
     mydb.close()

#This Function is Used to MODIFY Value Of balance in Table --------------------------------
def sqlmoney(n,i,bal):
     mydb=mysql.connector.connect(host="localhost"
                                   ,user="root"
                                   ,passwd="root"
                                   ,database="bank_sys")
     mycur=mydb.cursor()
     query='UPDATE accounts SET Balance=%s WHERE Ids=%s'
     val=(bal,i)
     mycur.execute(query,val)
     mydb.commit()
     mydb.close()

#This Function is Used to Display The MAIN Screen ----------------------------------------------------
def menu():
     print("===========================================================================================")
     print("--------------------------**WELCOME TO BANK'S MANAGEMENT SYSTEM**--------------------------")
     print("-------------------------Avaliable option to check/create accounts-------------------------")
     print("---------------------------------(A): Create an Account------------------------------------")
     print("----------------------------(B): Deposit Money in your Account-----------------------------")
     print("---------------------------(C): Withdraw Money from your Account---------------------------")
     print("-----------------------(D): See Details and Balance of your Account------------------------")
     print("---------------------------------------(E): Exit-------------------------------------------")
     print("===========================================================================================")
     userchoice=input("Enter Your Choice From Above Options : ")

     if(userchoice=="A" or userchoice=="a"):
          create()
          endscreen()
     elif(userchoice=="B" or userchoice=="b"):
          deposit()
          endscreen()
     elif(userchoice=="C" or userchoice=="c"):
          withdraw()
          endscreen()
     elif(userchoice=="D" or userchoice=="d"):
          display()
          endscreen()
     elif(userchoice=="E" or userchoice=="e"):
          print("#-----------------------------------Have a Nice Day---------------------------------------#")
     else:
          print("~~~~~~~~~~~~~~~~~~~~~~~~ERROR : Make Choice From Given Options~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
          menu()
     

#This Function is Used to Create Account --------------------------------------------------------------------
def create():
     names,ids,balances=zip(*data())
     names,ids,balances=list(names),list(ids),list(balances)
     user_name=str(input("Enter Your Name : "))
     if(len(ids)==0):
          user_id=1
     else:
          user_id=ids[-1]+1
     balance=0
     names.append(user_name)
     ids.append(user_id)
     balances.append(balance)
     sqlcreate(user_name,user_id,balance)
     print("==============================================================")
     print("****************Your Account has Been Created*****************")
     print("~~~~~~~~~~~~~~~~~~Your ID is : ",ids[-1],"~~~~~~~~~~~~~~~~~~~~")
     print("==============================================================")

#This Function is Used to Deposit Money in Account ------------------------------------------------
def deposit():
     names,ids,balances=zip(*data())
     names,ids,balances=list(names),list(ids),list(balances)
     user_name=str(input("Enter Your Name : "))
     user_id=int(input("Enter Your ID : "))
     invalid=0
     for i in range(0,len(names)):
          if(user_name==names[i]):
               invalid+=1
               e=i
               if(user_id==ids[i]):
                    amount=float(input("Enter Amount To Deposit : "))
                    if(balances[i]==0):
                         sqlmoney(user_name,user_id,amount)
                    else:
                         balances[i]+=amount
                         sqlmoney(user_name,user_id,balances[i])
                    print("Your Account has Been Credited by amount : ", amount)
                    print("Your Total Balance is : ", balances[i])
                    break
               else:
                    #In Case Of More Than 1 People Of Same Name But Diff.. ID
                    duplicate=0
                    for j in range(0,len(names)):
                         if(user_name==names[j]):
                              duplicate+=1
                    if(duplicate==1):
                         print("*****************Invalid ID*******************")
                         print("************Enter Details Again***************")
                         deposit()
                    else:
                         continue
          else:
               continue
     if(invalid==0):
          print("Your Name is Not Found , Please Enter Your Name Again")
          deposit()

#This Function is Used to Withdraw Money From Account --------------------------------------
def withdraw():
     names,ids,balances=zip(*data())
     names,ids,balances=list(names),list(ids),list(balances)
     user_name=str(input("Enter Your Name : "))
     user_id=int(input("Enter Your ID : "))
     invalid=0
     for i in range(0,len(names)):
          if(user_name==names[i]):
               invalid+=1
               e=i
               if(user_id==ids[i]):
                    amount=float(input("Enter Amount To Withdraw : "))
                    if(balances[i]-amount<=-1):
                         print("#-----*Insuficient Balance,Enter Acceptable Amount*-----#")
                         withdraw()
                    else:
                         balances[i]-=amount
                         sqlmoney(user_name,user_id,balances[i])
                         print("Your Account has Been Debited by amount : ", amount)
                         print("Your Total Balance is : ", balances[i])
                         break
               else:
                    #In Case Of More Than 1 People Of Same Name But Diff.. ID
                    duplicate=0
                    for j in range(0,len(names)):
                         if(user_name==names[j]):
                              duplicate+=1
                    if(duplicate==1):
                         print("*****************Invalid ID*******************")
                         print("************Enter Details Again***************")
                         withdraw()
                    else:
                         continue
          else:
               continue
          
     if(invalid==0):
          print("Your Name is Not Found , Please Enter Your Name Again")
          withdraw()
          
#This Function is Used to Display Account's Details --------------------------------------------------
def display():
     names,ids,balances=zip(*data())
     names,ids,balances=list(names),list(ids),list(balances)
     user_name=str(input("Enter Your Name : "))
     user_id=int(input("Enter Your ID : "))
     invalid=0
     for i in range(0,len(names)):
          if(user_name==names[i]):
               invalid+=1
               if(user_id==ids[i]):
                    print("--------------------Details-------------------")
                    print("Your Name : ",names[i])
                    print("Your ID : ",ids[i])
                    print("Your Balance : ",balances[i])
                    print("==============================================")
               else:
                    #In Case Of More Than 1 People Of Same Name ~~~~~
                    duplicate=0
                    for j in range(0,len(names)):
                         if(user_name==names[j]):
                              duplicate+=1
                    if(duplicate==1):
                         print("*****************Invalid ID*******************")
                         print("*************Enter Details Again**************")
                         display()
                    else:
                         continue
          else:
               continue
     if(invalid==0):
          print("Your Name is Not Found , Please Enter Your Name Again")
          display()

#Here We Are Calling The Main Funtion To Start The Program ---------------------------------- 
menu()
