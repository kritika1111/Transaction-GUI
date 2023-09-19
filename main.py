#Imports

import os
from tkinter import *
from PIL import ImageTk, Image

#Main  Screen
master=Tk()
master.title("Banking App")
###################################################################################################################################
#Functions
#Register()
def finish_reg():
    name=temp_name.get()
    age=temp_age.get()
    gender=temp_gender.get()
    password=temp_password.get()
    # path=os.getcwd()
    all_accounts=os.listdir()
    print(all_accounts)
    if name=="" or age=="" or gender=="" or password=="":
        notif.config(fg="red",text="All fields requried *")
        return
    for name_check in all_accounts:
        if name==name_check:
            notif.config(fg="red",text="Account already exists")
            return
        else:
            new_file=open(name,"w")
            new_file.write(name+'\n')
            new_file.write(password+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write("0")
            new_file.close()
            notif.config(fg="green",text="Account has been created")
def register():
    #Var
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    temp_name=StringVar()
    temp_age=StringVar()
    temp_gender=StringVar()
    temp_password=StringVar()
    #Register Screen
    register_screen=Toplevel(master)
    register_screen.title("Register")
    #Labels
    Label(register_screen,text="Please enter your details below to register",font=('Calibari',12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Name", font=('Calibari', 12)).grid(row=1,sticky=W)
    Label(register_screen, text="Age", font=('Calibari', 12)).grid(row=2,sticky=W)
    Label(register_screen, text="Gender", font=('Calibari', 12)).grid(row=3,sticky=W)
    Label(register_screen, text="Password", font=('Calibari', 12)).grid(row=4,sticky=W)
    notif=Label(register_screen,font=('Calibari', 12))
    notif.grid(row=6,sticky=N,pady=10)

    #Enteries
    Entry(register_screen,textvariable=temp_name).grid(row=1,column=0)
    Entry(register_screen,textvariable=temp_age).grid(row=2,column=0)
    Entry(register_screen,textvariable=temp_gender).grid(row=3,column=0)
    Entry(register_screen,textvariable=temp_password,show="*").grid(row=4,column=0)
    #Button
    Button(register_screen,text="Register",command=finish_reg,font=("Calibari",12)).grid(row=5,sticky=N,pady=10)

#################################################################################################################################

def finish_log():
    global login_name
    # global personal_details
    # global depost
    # global withdraw
    all_account=os.listdir()
    login_name=temp_username.get()
    login_password=temp_password.get()
    for name in all_account:
        if name==login_name:
            file=open(name,"r")
            file_data=file.read()
            file_data=file_data.split("\n")
            password=file_data[1]
            #Account Dashboard
            if login_password==password:
                login_screen.destroy()
                account_dashboard=Toplevel(master)
                account_dashboard.title("Dashboard")
                #Dashboard Label
                Label(account_dashboard,text="Account Deshboard",font=("Calibari",12)).grid(row=0,sticky=N,pady=10)
                Label(account_dashboard,text="Welcome:"+name,font=("Calibari",12)).grid(row=1,sticky=N,padx=5)
                #dashboard Button
                Button(account_dashboard,text="Personal Details",font=("Calibari",12),width=30,command=personal_details).grid(row=2,sticky=N,padx=10)
                Button(account_dashboard,text="Deposit",font=("Calibari",12),width=30,command=deposit).grid(row=3,sticky=N,padx=10)
                Button(account_dashboard,text="Withdraw",font=("Calibari",12),width=30,command=withdraw).grid(row=4,sticky=N,padx=10)
                Label(account_dashboard).grid(row=5,sticky=N,pady=10)
                return
            else:
                login_notif.config(fg="red",text="Password incorrect!!")
                return
    login_notif.config(fg="red",text="No account found!!")

            # return

def login():
    #Var
    global temp_username
    global temp_password
    global login_notif
    global login_screen
    temp_username=StringVar()
    temp_password=StringVar()
    #Login Screen
    login_screen=Toplevel(master)
    login_screen.title("Login")
    #Labels Login
    Label(login_screen,text="Login to your account",font=("Calibari",12)).grid(row=0,sticky=N,pady=10)
    Label(login_screen,text="Username",font=("Calibari",12)).grid(row=1,sticky=W)
    Label(login_screen,text="Password",font=("Calibari",12)).grid(row=2,sticky=W)
    login_notif=Label(login_screen,font=('Calibari',12))
    login_notif.grid(row=4,sticky=N)
    #Entry Login
    Entry(login_screen,textvariable=temp_username).grid(row=1,column=1,padx=5)
    Entry(login_screen,textvariable=temp_password,show="*").grid(row=2,column=1,padx=5)
    # Button
    Button(login_screen,text="Login",command=finish_log,width=15,font=("Calibari",12)).grid(row=3,sticky=N,pady=5,padx=5)

    #############################################################################################################################################
def personal_details():
    #var
    file=open(login_name,'r')
    file_data=file.read()
    under_deatails=file_data.split('\n')
    details_name=under_deatails[0]
    details_age=under_deatails[2]
    details_gender=under_deatails[3]
    details_balance=under_deatails[4]
    #Personal Details
    personal_details_screen=Toplevel(master)
    personal_details_screen.title("Personal Details")
    #Labels
    Label(personal_details_screen,text="Personal Details",font=("Calibari",12)).grid(row=0,sticky=N,pady=10)
    Label(personal_details_screen,text="Name:"+details_name,font=("Calibari",12)).grid(row=1,sticky=W)
    Label(personal_details_screen,text="Age:"+details_age,font=("Calibari",12)).grid(row=2,sticky=W)
    Label(personal_details_screen,text="Gender:"+details_gender,font=("Calibari",12)).grid(row=3,sticky=W)
    Label(personal_details_screen,text="Balance:"+details_balance,font=("Calibari",12)).grid(row=4,sticky=W)
    notif_personal_details=Label(personal_details_screen,font=("Calibari",12))
    notif_personal_details.grid(row=5,sticky=N,pady=10)


###################################################################################################################################################

def deposit():
    #Var
    global amount
    global deposit_notif
    global current_balance_label
    amount=StringVar()
    file=open(login_name,'r')
    file_data=file.read()
    user_details=file_data.split('\n')
    details_balance=user_details[4]
    #Deposit Screen
    deposit_screen=Toplevel(master)
    deposit_screen.title("Deposit")
    #Label
    Label(deposit_screen,text="Deposit",font=("Calibari",12)).grid(row=0,sticky=N,pady=10)
    current_balance_label=Label(deposit_screen,text="Current Balance :$"+details_balance,font=("Calibari",12))
    current_balance_label.grid(row=1,sticky=W)
    Label(deposit_screen,text="Amount",font=("Calibari",12)).grid(row=2,sticky=W)
    deposit_notif=Label(deposit_screen,font=("Calibari",12))
    deposit_notif.grid(row=4,sticky=N,pady=5)
    #Entry
    Entry(deposit_screen,textvariable=amount).grid(row=2,column=1)
    #Button
    Button(deposit_screen,text="Submit",font=("Calibari",12),command=cal_deposit).grid(row=3,sticky=W,pady=5)
def cal_deposit():
    if amount.get()=="":
        deposit_notif.config(text="Amount is required!!",fg="red")
        return
    if float(amount.get())<=0:
        deposit_notif.config(text="Negative currency is not accept",fg="red")
        return
    file=open(login_name,"r+")
    file_data=file.read()
    details=file_data.split("\n")
    current_balance=details[4]
    update_balance=current_balance
    update_balance=float(update_balance)+float(amount.get())
    file_data=file_data.replace(current_balance,str(update_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    current_balance_label.config(text="Your current balance :$"+str(update_balance),fg="green")
    deposit_notif.config(text="Balance Updated",fg="green")



##############################################################################################################################################################


def withdraw():
    #var
    global withdraw_amount
    global withdraw_notif
    global  current_balance_label
    withdraw_amount=StringVar()
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]
    # withdraw Screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title("Withdaw")
    # Label
    Label(withdraw_screen, text="Deposit", font=("Calibari", 12)).grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(withdraw_screen, text="Current Balance :$" + details_balance, font=("Calibari", 12))
    current_balance_label.grid(row=1, sticky=W)
    Label(withdraw_screen, text="Amount", font=("Calibari", 12)).grid(row=2, sticky=W)
    withdraw_notif = Label(withdraw_screen, font=("Calibari", 12))
    withdraw_notif.grid(row=4, sticky=N, pady=5)
    # Entry
    Entry(withdraw_screen, textvariable=withdraw_amount).grid(row=2, column=1)
    # Button
    Button(withdraw_screen, text="Submit", font=("Calibari", 12), command=cal_withdraw).grid(row=3, sticky=W, pady=5)

def cal_withdraw():
    if withdraw_amount.get() == "":
        withdraw_notif.config(text="Amount is required!!", fg="red")
        return
    if float(withdraw_amount.get()) <= 0:
        withdraw_notif.config(text="Negative currency is not accept", fg="red")
        return
    file = open(login_name, "r+")
    file_data = file.read()
    details = file_data.split("\n")
    current_balance = details[4]
    if float(withdraw_amount.get())>float(current_balance):
        withdraw_notif.config(text="Insufficient Funds!",fg='red')
        return
    update_balance = current_balance
    update_balance = float(update_balance) - float(withdraw_amount.get())
    file_data = file_data.replace(current_balance, str(update_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    current_balance_label.config(text="Your current balance :$" + str(update_balance), fg="green")
    withdraw_notif.config(text="Balance Updated", fg="green")



    ##############################################################################################################################################################################
#Image Import
img=Image.open('img1.png')
img=img.resize((150,150))
img=ImageTk.PhotoImage(img)

#Labels
Label(master,text="Customer Banking Beta",font=('Calibari',14)).grid(row=0,sticky=N,pady=10)
Label(master,text="The most secure bank you've probably used",font=('Calibari',12)).grid(row=1,sticky=N)
Label(master,image=img).grid(row=2,sticky=N,pady=5)
#Button
Button(master,text="Register",font=('Calibari',12),width=20,command=register).grid(row=3,sticky=N)
Button(master,text="Login",font=('Calibari',12),width=20,command=login).grid(row=4,sticky=N,pady=5)
master.mainloop()