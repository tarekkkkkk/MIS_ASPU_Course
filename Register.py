from msilib.schema import AdminExecuteSequence
from tkinter import *
from tkinter import messagebox
from tkinter import Button
from unicodedata import name
import pyodbc
from datetime import datetime


conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-8MHDVV9\SQLEXPRESS;"
    "Database=practice test;"
    "Trusted_Connection=yes;"
)


total_fee = 10000
remaining_fee = 0
def login_main():
    def login1():
        username = entry1.get()
        password = entry2.get()
        cursor = conn.cursor()
        cursor.execute("select * from Table_5 where USERNAME = ? ",(f'{username}'))
        global admin
        admin = username
        k=0
        for k in cursor:
            print(k)
            k=1
        if k==0:
                messagebox.showinfo("","Invalid Username.")
        else:
            cursor.execute("select * from Table_5 where USERNAME = ? ",(f'{username}'))
            for row in cursor:
                print(row)
                if (username=="") and (password==""):
                    messagebox.showinfo("","Blank Not Allowed")

                elif username==row[0] and password==row[1]:
                    messagebox.showinfo("","login successful")
                    time = datetime.now()

                    file1=open("History.txt","a")
                    file1.write(f"\n{time}\t {username} has logged in {name}")

                    main3=Tk()
                    main3.title("Choose")
                    main3.geometry("400x300")

                    Button(main3,text="register", command=lambda: register(), height=3, width=13, bd=3).place(x=30,y=20)
                    Button(main3,text="show", command=lambda: show(), height=3, width=13, bd=3).place(x=30,y=70)
                    Button(main3,text="update", command=lambda: update(), height=3, width=13, bd=3).place(x=30,y=120)
                    Button(main3,text="delete", command=lambda: delete(), height=3, width=13, bd=3).place(x=30,y=170)
                    Button(main3,text="Pay fee", command=lambda: pay_fee(), height=3, width=13, bd=3).place(x=30,y=220)

                    main3.mainloop()

                else:
                    messagebox.showinfo("","incorrect username and password")
    root1=Tk()
    root1.title("Login")
    root1.geometry("300x300")

    equation = StringVar()
    global entry1
    global entry2
    Label(root1,text="username").place(x=20,y=20)
    Label(root1,text="password").place(x=20,y=70)
    entry1=Entry(root1, textvariable=equation,bd=5)
    entry1.place(x=140,y=20)
    entry1.insert(0, "username")
    
    entry2=Entry(root1,show="*",bd=5)
    entry2.place(x=140,y=70)


    Button(root1,text="Login", command=lambda: login1(), height=3, width=13, bd=3).place(x=30,y=120)
    root1.mainloop()

def register():
    main2=Tk()
    main2.title("Register")
    main2.geometry("300x550")

    def register2():
        global total_fee
        global remaining_fee
        total_fee = 10000
        remaining_fee = 0
        name = entry2.get()
        age = entry3.get()
        address = entry4.get()
        date = entry5.get()
        email = entry6.get()
        paid_fee = entry7.get()
        cursor = conn.cursor()
        cursor.execute("select * from Table_4 where [E-MAIL] = ?",(f'{email}'))
        remaining_fee = total_fee - int(paid_fee)
        k=0
        for i in cursor:
            k = 1
        if (name=="") and (age=="") and (address=="") and (date=="") and (email=="") and (paid_fee=="") :
            messagebox.showinfo("","Blank Not Allowed")
        elif k == 1:
            messagebox.showinfo("","student already exists")

        else:
            cursor = conn.cursor()
            cursor.execute(
                "insert into Table_4(NAME,AGE,ADDRESS,DATE,[E-MAIL],[PAID FEE],[REMAINING FEE],[TOTAL FEE]) values(?,?,?,?,?,?,?,?);",
                (f'{name}',f'{age}',f'{address}',f'{date}',f'{email}',f'{paid_fee}',f'{remaining_fee}',f'{total_fee}'))
            conn.commit()

            root03=Tk()
            root03.title("Registered successfully")
            root03.geometry("200x200")
            Label(root03,text="Details saved").place(x=20,y=20)

            root03.mainloop()

    global entry2
    global entry3
    global entry4
    global entry5
    global entry6
    global entry7

    Label(main2,text="name").place(x=20,y=70)
    Label(main2,text="age").place(x=20,y=120)
    Label(main2,text="address").place(x=20,y=170)
    Label(main2,text="date").place(x=20,y=220)
    Label(main2,text="email").place(x=20,y=270)
    Label(main2,text="paid_fee").place(x=20,y=320)

    entry2=Entry(main2,bd=5)
    entry2.place(x=140,y=70)
    entry3=Entry(main2,bd=5)
    entry3.place(x=140,y=120)
    entry4=Entry(main2,bd=5)
    entry4.place(x=140,y=170)
    entry5=Entry(main2,bd=5)
    entry5.place(x=140,y=220)
    entry6=Entry(main2,bd=5)
    entry6.place(x=140,y=270)
    entry7=Entry(main2,bd=5)
    entry7.place(x=140,y=320)
  
    Button(main2,text="register", command=lambda: register2(), height=3, width=13, bd=3).place(x=30,y=470)

    main2.mainloop()

def show():
    main2=Tk()
    main2.title("Show")
    main2.geometry("1000x300")
    cursor = conn.cursor()
    cursor.execute("select * from Table_4 ")
    Label(main2,text="ID \t NAME \t\t\t AGE \t ADDRESS \t DATE \t\t E-MAIL \t\t\t\t PAID FEE \t REMAINING \t TOTAL").place(x=20,y=20)
    Yaxis=20
    print(f"{admin} seen the detail of students.")
    time = datetime.now()

    file1=open("History.txt","a")
    file1.write(f"\n{time}\t {admin} has seen details")
    for row in cursor:
        Yaxis+=30
        Label(main2,text=f"\n{row[0]} \t {row[1].capitalize()} \t\t {row[2]} \t {row[3]} \t\t {row[4]} \t {row[5]} \t\t {row[6]} \t\t {row[7]} \t\t {row[8]}").place(x=20,y=Yaxis)
    main2.mainloop()



    main2.mainloop()

def update():
    main2=Tk()
    main2.title("Update")
    main2.geometry("270x300")
    def proceed():
        id = entry1.get()
        cursor = conn.cursor()
        if (id=="") :
            messagebox.showinfo("","Blank Not Allowed")
        else:
            cursor.execute("select * from Table_4 where ID = ?",(f'{id}'))
            for row in cursor:
                root03=Tk()
                root03.title("Update")
                root03.geometry("600x400")
                def update2():
                    name = entry2.get()
                    age = entry3.get()
                    address = entry4.get()
                    date = entry5.get()
                    email = entry6.get()
                    if (name=="") or (age=="") or (address=="") or (date=="") or (email=="") :
                        messagebox.showinfo("","Blank Not Allowed")
                    else:
                        cursor = conn.cursor()
                        cursor.execute("update TABLE_4 set NAME = ?, AGE = ?, ADDRESS = ?, DATE = ?, [E-MAIL] = ?  where ID = ?;",(f'{name}',age,f'{address}',f'{date}', f'{email}', id))
                        conn.commit()

                        root04=Tk()
                        root04.title("Update successfully")
                        root04.geometry("200x200")
                        Label(root04,text=f"Updated data of {name}").place(x=20,y=20)

                        root04.mainloop()

                equation1 = StringVar()
                equation2 = StringVar()
                equation3 = StringVar()
                equation4 = StringVar()
                equation5 = StringVar()
                global entry2
                global entry3
                global entry4
                global entry5
                global entry6

                Label(root03,text="name").place(x=20,y=70)
                Label(root03,text="age").place(x=20,y=120)
                Label(root03,text="address").place(x=20,y=170)
                Label(root03,text="date").place(x=20,y=220)
                Label(root03,text="email").place(x=20,y=270)

                entry2=Entry(root03, textvariable=equation1,bd=5)
                entry2.place(x=140,y=70)
                entry2.insert(0, f"{row[1]}")
                entry3=Entry(root03, textvariable=equation2,bd=5)
                entry3.place(x=140,y=120)
                entry3.insert(0, f"{row[2]}")
                entry4=Entry(root03, textvariable=equation3,bd=5)
                entry4.place(x=140,y=170)
                entry4.insert(0, f"{row[3]}")
                entry5=Entry(root03, textvariable=equation4,bd=5)
                entry5.place(x=140,y=220)
                entry5.insert(0, f"{row[4]}")
                entry6=Entry(root03, textvariable=equation5,bd=5)
                entry6.place(x=140,y=270)
                entry6.insert(0, f"{row[5]}")

            
                Button(root03,text="Update", command=lambda: update2(), height=3, width=13, bd=3).place(x=30,y=320)

                root03.mainloop()

    global entry1

    Label(main2,text="ID").place(x=20,y=20)
    
    entry1=Entry(main2,bd=5)
    entry1.place(x=140,y=20)



    Button(main2,text="Proceed", command=lambda: proceed(), height=3, width=13, bd=3).place(x=30,y=70)

    main2.mainloop()

def delete():
    main2=Tk()
    main2.title("Delete")
    main2.geometry("270x300")
    def delete1():
        id = entry1.get()
        cursor = conn.cursor()
        cursor.execute("select * from Table_4 where ID = ?",(f'{id}'))
        if (id=="") :
            messagebox.showinfo("","Blank Not Allowed")
        else:
            cursor = conn.cursor()
            cursor.execute(
            "delete from TABLE_4 where ID=?",(f'{id}')
            )
            conn.commit()

            main04=Tk()
            main04.title("Deleted successfully")
            main04.geometry("200x200")
            Label(main04,text="Deleted").place(x=20,y=20)

            main04.mainloop()

    global entry1

    Label(main2,text="ID").place(x=20,y=20)
    

    entry1=Entry(main2,bd=5)
    entry1.place(x=140,y=20)
  

    Button(main2,text="delete", command=lambda: delete1(), height=3, width=13, bd=3).place(x=30,y=70)

    main2.mainloop()


def pay_fee():
    main2=Tk()
    main2.title("payment gateway")
    main2.geometry("270x300")
    def proceed1():
        id = entry1.get()
        cursor = conn.cursor()
        if (id=="") :
            messagebox.showinfo("","Blank Not Allowed")
        else:
            cursor.execute("select * from Table_4 where ID = ?",(f'{id}'))
            for row in cursor:
                root03=Tk()
                root03.title("Fee payment")
                root03.geometry("600x400")
                def pay_fee1():
                    total_fee = 10000
                    remaining_fee = int(row[7])
                    paid_fee = int(row[6])
                    new_payment= fee_entry.get()
                    cursor = conn.cursor()
                    cursor.execute("select * from Table_4 where ID = ?",(f'{id}'))
                    if (new_payment=="") :
                        messagebox.showinfo("","Blank Not Allowed")
                    elif int(new_payment)> remaining_fee :
                        messagebox.showinfo("","You have entered the extra amount.")
                    else:
                        paid_fee= int(row[6]) + int(new_payment)
                        remaining_fee= total_fee - paid_fee
                        cursor = conn.cursor()
                        cursor.execute("update TABLE_4 set [PAID FEE] = ?, [REMAINING FEE] = ? where ID = ?;",(paid_fee, remaining_fee, id))
                        conn.commit()

                        root04=Tk()
                        root04.title("Update successfully")
                        root04.geometry("200x200")
                        Label(root04,text=f"Payment details updated").place(x=20,y=20)

                        root04.mainloop()

                global fee_entry

                Label(root03,text="Pay fee").place(x=20,y=20)

                fee_entry=Entry(root03,bd=5)
                fee_entry.place(x=140,y=20)     

                Button(root03,text="Pay fee", command=lambda: pay_fee1(), height=3, width=13, bd=3).place(x=30,y=70)
                
                root03.mainloop()


                    

    global entry1

    Label(main2,text="ID").place(x=20,y=20)
    
    entry1=Entry(main2,bd=5)
    entry1.place(x=140,y=20)



    Button(main2,text="Proceed", command=lambda: proceed1(), height=3, width=13, bd=3).place(x=30,y=70)

    main2.mainloop()

main=Tk()
main.title("Login")
main.geometry("300x300")

Button(main,text="Login", command=lambda: login_main(), height=3, width=13, bd=3).place(x=30,y=20)
main.mainloop()