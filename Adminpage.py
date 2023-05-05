from tkinter import *
import tkinter as tttk
from ttkthemes import themed_tk as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector



def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=i)

def search():
    import mysql.connector as c
    chk=0
    con=c.connect(host="localhost",user="root",passwd="sandy",database="ebms")
    cursor=con.cursor() 
    srch2=srch.get()
    query = "select customer.Cust_ID,customer.Customer_First_Name, customer.Customer_Last_Name, customer.Address_Line_1, customer.Address_Line_2, customer.Pincode, customer.Contact_Number, account.Account_ID, account.Account_Type, account.Meter_No, account.Cur_Meter_Reading, account.Prev_Meter_Reading from customer join account on customer.Cust_ID=account.Cust_ID WHERE customer.Cust_ID LIKE '%"+srch2+"%';"
    cursor.execute(query)
    rows = cursor.fetchall()
    con.commit()
    update(rows)

def display():
    query= "select customer.Cust_ID,customer.Customer_First_Name, customer.Customer_Last_Name, customer.Address_Line_1, customer.Address_Line_2, customer.Pincode, customer.Contact_Number, account.Account_ID, account.Account_Type, account.Meter_No, account.Cur_Meter_Reading, account.Prev_Meter_Reading from customer join account on customer.Cust_ID=account.Cust_ID;"
    cursor.execute(query)
    rows=cursor.fetchall()
    update(rows)

def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
    t4.set(item['values'][3])
    t5.set(item['values'][4])
    t6.set(item['values'][5])
    t7.set(item['values'][6])
    t8.set(item['values'][7])
    t9.set(item['values'][8])
    t10.set(item['values'][9])
    t11.set(item['values'][10])
    t12.set(item['values'][11])

def update_customer():
    cusid = t1.get()
    fname = t2.get()
    lname = t3.get()
    adln1 = t4.get()
    adln2 = t5.get()
    pcode = t6.get()
    cnnum = t7.get()
    accid = t8.get()
    acctp = t9.get()
    mtrno = t10.get()
    cmtrd = t11.get()
    pmtrd = t12.get()

    if messagebox.askyesno("Confirm Updation", "Do you want to update Customer Details?"):
        query = "Update account set Account_ID = %s, Account_Type = %s, Meter_No = %s, Cur_Meter_Reading = %s, Prev_Meter_Reading = %s where Cust_ID = %s"
        query2 = "update customer set Customer_First_Name = %s, Customer_Last_Name = %s, Address_Line_1 = %s, Address_Line_2 = %s, Pincode = %s, Contact_Number = %s where Cust_ID = %s"
        cursor.execute (query, (accid, acctp, mtrno, cmtrd, pmtrd, cusid))
        cursor.execute (query2, (fname, lname, adln1, adln2, pcode, cnnum, cusid))
        mydb.commit()
        display()
    else:
        return True
        


def add_new():
    cusid = t1.get()
    fname = t2.get()
    lname = t3.get()
    adln1 = t4.get()
    adln2 = t5.get()
    pcode = t6.get()
    cnnum = t7.get()
    accid = t8.get()
    acctp = t9.get()
    mtrno = t10.get()
    cmtrd = t11.get()
    pmtrd = t12.get()

    query = "insert into customer (Cust_Id, Customer_First_Name, Customer_Last_Name, Address_Line_1, Address_Line_2, Pincode, Contact_Number) values (%s, %s, %s, %s, %s, %s, %s)"
    query2 = "insert into account (Account_ID, Cust_ID, Account_Type, Meter_No, Cur_Meter_Reading, Prev_Meter_Reading) values (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (cusid, fname, lname, adln1, adln2, pcode, cnnum))
    cursor.execute(query2, (accid, cusid, acctp, mtrno, cmtrd, pmtrd))
    mydb.commit()
    display()
    
    

def delete_customer():
    customer_id = t1.get()
    if messagebox.askyesno("Confirm Deletion?","Do you want to delete Customer Detail?"):
        query = "delete from account where Cust_ID="+customer_id
        query2= "delete from customer where Cust_ID="+customer_id
        cursor.execute(query)
        cursor.execute(query2)
        mydb.commit()
        display()
    else:
        return True

def clear():
    t1.set('')
    t2.set('')
    t3.set('')
    t4.set('')
    t5.set('')
    t6.set('')
    t7.set('')
    t8.set('')
    t9.set('')
    t10.set('')
    t11.set('')
    t12.set('')
    

def exitb():
    cexit=tttk.messagebox.askyesno('Exit Admin Editor?', 'CONFIRM IF YOU WANT TO EXIT')
    if cexit>0:
        root.destroy()
        return
    else:
        srch.focus()


def clearlst():
    trv.delete(*trv.get_children())
    srch.set('')
    
    
    
    
     
    

mydb = mysql.connector.connect (host="localhost", user="root", passwd="sandy", database="ebms")
cursor = mydb.cursor()

root= tk.ThemedTk()
root.get_themes()                 
root.set_theme("radiance")
root.state("zoomed")
root.iconbitmap(r'E:\Electricity Billing System\icon.ico')
wrapper1 = ttk.LabelFrame (root, text="Customer List")
wrapper2 = ttk.LabelFrame (root, text="Search")
wrapper3 = ttk.LabelFrame (root, text="Customer Data")

#===================================================StringVars===========================================
srch=StringVar()
t1=StringVar()
t2=StringVar()
t3=StringVar()
t4=StringVar()
t5=StringVar()
t6=StringVar()
t7=StringVar()
t8=StringVar()
t9=StringVar()
t10=StringVar()
t11=StringVar()
t12=StringVar()


wrapper1.pack(fill="both",expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both",expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both",expand="yes", padx=20, pady=10)

trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7,8,9,10,11,12), show="headings", height="5")
trv.pack(side=LEFT)
trv.place(x=0, y=0)

trv.heading('#1', text="Customer ID")
trv.heading('#2', text="Cust First Name")
trv.heading('#3', text="Cust Last Name")
trv.heading('#4', text="Address Line 1")
trv.heading('#5', text="Address Line 2")
trv.heading('#6', text="Pincode")
trv.heading('#7', text="Contact Number")
trv.heading('#8', text="Account ID")
trv.heading('#9', text="Account Type")
trv.heading('#10', text="Meter No")
trv.heading('#11', text="Cur Meter Reading")
trv.heading('#12', text="Prev Meter Reading")
trv.column('#1', width=123, minwidth=150)
trv.column('#2', width=123, minwidth=150)
trv.column('#3', width=123, minwidth=150)
trv.column('#4', width=123, minwidth=150)
trv.column('#5', width=123, minwidth=150)
trv.column('#6', width=123, minwidth=150)
trv.column('#7', width=123, minwidth=150)
trv.column('#8', width=123, minwidth=150)
trv.column('#9', width=123, minwidth=150)
trv.column('#10', width=123, minwidth=150)
trv.column('#11', width=123, minwidth=150)
trv.column('#12', width=123, minwidth=150)

trv.bind('<Double 1>', getrow)

#=======================================Vertical Scrollbar=========================================
yscrollbar = ttk.Scrollbar(wrapper1, orient='vertical', command=trv.yview)
yscrollbar.pack(side=RIGHT , fill="y")



#========================================Horizontal Scrollbar======================================
xscrollbar = ttk.Scrollbar(wrapper1, orient='horizontal', command=trv.xview)
xscrollbar.pack(side=BOTTOM , fill= BOTH)

trv.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)

query= "select customer.Cust_ID,customer.Customer_First_Name, customer.Customer_Last_Name, customer.Address_Line_1, customer.Address_Line_2, customer.Pincode, customer.Contact_Number, account.Account_ID, account.Account_Type, account.Meter_No, account.Cur_Meter_Reading, account.Prev_Meter_Reading from customer join account on customer.Cust_ID=account.Cust_ID;"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)



#==========================================Search Section============================================

lbl = ttk.Label(wrapper2, text ="Search Using Customer ID:")
lbl.pack(side=tttk.LEFT, padx=10)
ent = ttk.Entry(wrapper2, textvariable = srch)
ent.pack(side=tttk.LEFT, padx=6)
btn = ttk.Button(wrapper2, text="Search", command = search)
btn.pack(side=tttk.LEFT, padx=6)
dbtn = ttk.Button(wrapper2, text="Display All", command = display)
dbtn.pack(side=tttk.LEFT, padx=6)
ccbtn= ttk.Button(wrapper2, text="Clear List", command = clearlst)
ccbtn.pack(side=tttk.LEFT, padx=6)


#================================================User Data==================================================
lbl1 =ttk.Label(wrapper3, text="Customer ID")
lbl1.grid(row=0, column=1, padx=5, pady=3)
ent1 = ttk.Entry(wrapper3, textvariable= t1)
ent1.grid(row=0, column=2, padx=5, pady=3)

lbl2 =ttk.Label(wrapper3, text="Customer First Name")
lbl2.grid(row=1, column=1, padx=5, pady=3)
ent2 = ttk.Entry(wrapper3, textvariable= t2)
ent2.grid(row=1, column=2, padx=5, pady=3)

lbl3 =ttk.Label(wrapper3, text="Customer Last Name")
lbl3.grid(row=2, column=1, padx=5, pady=3)
ent3 = ttk.Entry(wrapper3, textvariable= t3)
ent3.grid(row=2, column=2, padx=5, pady=3)

lbl4 =ttk.Label(wrapper3, text="Address Line 1")
lbl4.grid(row=3, column=1, padx=5, pady=3)
ent4 = ttk.Entry(wrapper3, textvariable= t4)
ent4.grid(row=3, column=2, padx=5, pady=3)

lbl5 =ttk.Label(wrapper3, text="Address Line 2")
lbl5.grid(row=4, column=1, padx=5, pady=3)
ent5 = ttk.Entry(wrapper3, textvariable= t5)
ent5.grid(row=4, column=2, padx=5, pady=3)

lbl6 =ttk.Label(wrapper3, text="Pincode")
lbl6.grid(row=5, column=1, padx=5, pady=3)
ent6 = ttk.Entry(wrapper3, textvariable= t6)
ent6.grid(row=5, column=2, padx=5, pady=3)

lbl7 =ttk.Label(wrapper3, text="Contact Number")
lbl7.grid(row=6, column=1, padx=5, pady=3)
ent7 = ttk.Entry(wrapper3, textvariable= t7)
ent7.grid(row=6, column=2, padx=5, pady=3)

lbl8 =ttk.Label(wrapper3, text="Account ID")
lbl8.grid(row=7, column=1, padx=5, pady=3)
ent8 = ttk.Entry(wrapper3, textvariable= t8)
ent8.grid(row=7, column=2, padx=5, pady=3)

lbl9 =ttk.Label(wrapper3, text="Account Type")
lbl9.grid(row=8, column=1, padx=5, pady=3)
ent9 = ttk.Entry(wrapper3, textvariable= t9)
ent9.grid(row=8, column=2, padx=5, pady=3)

lbl10 =ttk.Label(wrapper3, text="Meter Number")
lbl10.grid(row=9, column=1, padx=5, pady=3)
ent10 = ttk.Entry(wrapper3, textvariable= t10)
ent10.grid(row=9, column=2, padx=5, pady=3)

lbl11 =ttk.Label(wrapper3, text="Current Meter Reading")
lbl11.grid(row=10, column=1, padx=5, pady=3)
ent11 = ttk.Entry(wrapper3, textvariable= t11)
ent11.grid(row=10, column=2, padx=5, pady=3)

lbl12 =ttk.Label(wrapper3, text="Previous Meter Reading")
lbl12.grid(row=11, column=1, padx=5, pady=3)
ent12 = ttk.Entry(wrapper3, textvariable= t12)
ent12.grid(row=11, column=2, padx=5, pady=3)

up_btn = ttk.Button(wrapper3, text="Update", command = update_customer)
add_btn = ttk.Button(wrapper3, text="Add New", command= add_new)
del_btn = ttk.Button(wrapper3, text="Delete", command= delete_customer)
cbtn = ttk.Button(wrapper3, text="Clear", command = clear)
exbtn = ttk.Button(wrapper3, text ="Exit", command = exitb)

add_btn.grid(row=13, column=0, padx=5, pady=3)
up_btn.grid(row=13, column=1, padx=5, pady=3)
del_btn.grid(row=13, column=2, padx=5, pady=3)
cbtn.grid(row=13, column=3, padx=5, pady=3)
exbtn.grid(row=13, column=4, padx=5, pady=3)



root.title("Admin Page")
root.geometry("1500x1000")
root.mainloop()
 
