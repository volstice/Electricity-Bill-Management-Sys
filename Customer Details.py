#=======================================================Imports================================================
from tkinter import *
import tkinter as tttk
from ttkthemes import themed_tk as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import random
from fpdf import FPDF
import os
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
#==============================================================Tkinter Frames====================================================
root= tk.ThemedTk()
root.get_themes()                 
root.set_theme("radiance")
root.title("Customer Details")
root.geometry("1500x1000")
root.state("zoomed")
root.iconbitmap(r'E:\Electricity Billing System\icon.ico')


wrapper1 = ttk.Frame(root)
wrapper2 = ttk.LabelFrame (root, text="Customer Details")
wrapper3 = ttk.LabelFrame (root, text="Search Details")
inwrapper1 = ttk.Frame(wrapper3)
inwrapper2= ttk.Frame(wrapper3, relief=GROOVE, border=3)
statusbar = ttk.Label(root, text="* (Required Fields) Enter CUSTOMER ID, ACCOUNT ID, METER NUMBER and press DISPLAY DETAIL button to login ", relief=SUNKEN, anchor=W, font='Times 10 italic')
statusbar.pack(side=BOTTOM, fill=X)

wrapper1.pack(fill=BOTH,expand="yes", padx=20, pady=10)
wrapper2.pack(fill=X,expand="yes", padx=20, pady=10)
wrapper3.pack(fill=X,expand="no", padx=20, pady=10)
inwrapper1.pack(expand="no", padx=20, pady=10, side=LEFT)
inwrapper2.pack(fill="both",expand="yes", padx=20, pady=10, side=RIGHT)
lbltxt= ttk.Label (wrapper1, font= ('Century Schoolbook', 42,  'bold'), text= 'Customer Details',width=45, background= 'Ghost white',anchor=tttk.CENTER)
lbltxt.place(relx = 0.5, rely = 0.5, anchor = CENTER)


#===============================================================Customer Details====================================================================

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
t13=StringVar()
t14=StringVar()
t15=StringVar()
t16=StringVar()
t17=StringVar()
bill_no=StringVar()


#========================================================Functions===========================================================================
def credentials():
    if t1.get()=="":
        tttk.messagebox.showinfo('Fetching Error','Please enter valid Customer Id, Account Id, Meter No')
    else:
        import mysql.connector as c
        chk=0
        con=c.connect(host="localhost",user="root",passwd="sandy",database="ebms")

        d=int(t1.get())
        c=t8.get()
        e=t10.get()

        cursor=con.cursor()  
        cursor.execute( "select * from account")
        row=cursor.fetchall()
        
        for i in row:
            if i[1]==d and i[0]==c and i[3]==e:
                chk=1
                break
        if chk==1:
            ent1.configure(state=DISABLED)
            ent2.configure(state=DISABLED)
            ent3.configure(state=DISABLED)
            t12.set("LOL")
            ent1.focus()
            display()
            

        else:
            q=tttk.messagebox.showwarning('Login Error','Please check the Login details')
            ent1.focus()



def display():
    if t1.get()=="":
        tttk.messagebox.showinfo('Fetching Error','Please Provide Customer ID')
    else:
        def generic_data():
             
            import mysql.connector as c
            con=c.connect(host="localhost",user="root",passwd="sandy",database="ebms")
            srch2=t1.get()
            cursor=con.cursor()
            query1= "select customer.Cust_ID,customer.Customer_First_Name, customer.Customer_Last_Name, customer.Address_Line_1, customer.Address_Line_2, customer.Pincode, customer.Contact_Number, account.Account_ID, account.Account_Type, account.Meter_No, account.Cur_Meter_Reading, account.Prev_Meter_Reading from customer join account on customer.Cust_ID=account.Cust_ID WHERE customer.Cust_ID LIKE '%"+srch2+"%';"
            cursor.execute(query1)
            rows=cursor.fetchall()
            t2.set(rows[0][1])
            t3.set(rows[0][2])
            t4.set(rows[0][3])
            t5.set(rows[0][4])
            t6.set(rows[0][5])
            t7.set(rows[0][6])
            t9.set(rows[0][8])
            t11.set(rows[0][10])
            t12.set(rows[0][11])
            
        def tariff():
            import mysql.connector as c
            con=c.connect(host="localhost",user="root",passwd="sandy",database="ebms")
            srch1=t9.get()
            cursor=con.cursor()
            cursor.execute("select * from tariff where Account_Type LIKE '%"+srch1+"%';")
            row=cursor.fetchall()
            a=int(t12.get())
            b=int(t11.get())
            t13.set(row[0][1])
            t14.set(b-a)
            c=int(t14.get())* 0.13
            t15.set('$'+ str('%.2f'%c))
            t16.set('$' + str(0.03 * int(float('%.2f'%c))))
            d=int(row[0][2])
            e=float('%.2f'%c)
            f=float((0.03 * int(float('%.2f'%c))))
            g=(float(t13.get())*float('%.2f'%c))
            h=d+e+f+g
            t17.set('$'+ str('%.2f'%h))
            

            
            
            
        
        
        
            
        
    generic_data()
    tariff()
            
                
def paybill():
    a=str(t7.get())

    if a!='':       
        q=tttk.messagebox.showinfo('Pay Bill','A link to payment gateway will be sent to your registered mobile number '+a+' please refer to the text message for further instructions')
    else:
        q=tttk.messagebox.showinfo('Payment Error','Please enter required data to continue')
        
def exitb():
    p=tttk.messagebox.askokcancel('Exit','Do you want to Quit?')
    if p>0:
        root.destroy()
        return
    else:
        ent1.focus()


    
def clear():
    t1.set("")
    t2.set("")
    t3.set("")
    t4.set("")
    t5.set("")
    t6.set("")
    t7.set("")
    t8.set("")
    t9.set("")
    t10.set("")
    t11.set("")
    t12.set("")
    t13.set("")
    t14.set("")
    t15.set("")
    t16.set("")
    t17.set("")
    ent1.configure(state=NORMAL)
    ent2.configure(state=NORMAL)
    ent3.configure(state=NORMAL)
    billarea.configure(state=NORMAL)
    billarea.delete(1.0,END)
    billarea.configure(state=DISABLED)
    ent1.focus()

def requp():
    a=(t7.get())

    if a!='':       
        q=tttk.messagebox.showinfo('Request for Updation','A request token has been generated and a link to fill the data update form has been sent to your registered mobile number '+a+' please refer to the text message for further instructions')
    else:
        q=tttk.messagebox.showinfo('Update Request Error','Please enter required data to continue')
        

x=random.randint(100000,999999)
bill_no.set(str(x))

def reciept():
    billarea.configure(state=NORMAL)
    billarea.delete(1.0,END)
    billarea.insert(END, "\t\t\t\t Electricity Monthly Bill")
    billarea.insert(END, "\n=======================================================================")
    billarea.insert(END, f'\n\t\t\tBill Number: \t\t\t{bill_no.get()}')
    billarea.insert(END, f'\n\t\t\tCustomer ID: \t\t\t{t1.get()}')
    billarea.insert(END, f'\n\t\t\tAccount ID: \t\t\t{t8.get()}')
    billarea.insert(END, f'\n\t\t\tMeter No: \t\t\t{t10.get()}')
    billarea.insert(END, f'\n\t\t\tCustomer First Name: \t\t\t{t2.get()}')
    billarea.insert(END, f'\n\t\t\tCustomer Last Name: \t\t\t{t3.get()}')
    billarea.insert(END, f'\n\t\t\tAddress Line 1: \t\t\t{t4.get()}')
    billarea.insert(END, f'\n\t\t\tAddress Line 2: \t\t\t{t5.get()}')
    billarea.insert(END, f'\n\t\t\tPin Code: \t\t\t{t6.get()}')
    billarea.insert(END, f'\n\t\t\tContact Number: \t\t\t{t7.get()}')
    billarea.insert(END, f'\n\t\t\tAccount Type: \t\t\t{t9.get()}')
    billarea.insert(END, f'\n\t\t\tPrevious Meter Reading: \t\t\t{t11.get()}')
    billarea.insert(END, f'\n\t\t\tCurrent Meter Reading: \t\t\t{t12.get()}')
    billarea.insert(END, f'\n\t\t\tTariff Implied: \t\t\t{t13.get()}')
    billarea.insert(END, f'\n\t\t\tUnits Used: \t\t\t{t14.get()}')
    billarea.insert(END, f'\n\t\t\tNet Bill: \t\t\t{t15.get()}')
    billarea.insert(END, f'\n\t\t\tTax: \t\t\t{t16.get()}')
    billarea.insert(END, "\n=======================================================================")
    billarea.insert(END, f'\n\t\t\tTotal Payable Amount: \t\t\t{t17.get()}')
    billarea.insert(END, "\n=======================================================================")
    billarea.insert(END, "\n\n\t\t\t*This receipt is system generated and no signature required")
    billarea.configure(font='roboto 11')
    billarea.configure(state=DISABLED)
    

#-----------------------------------------Print(pre defined path)----------------------------------------
def printf():
    q=tttk.messagebox.askokcancel('Confirm Print','Do you want to print the bill?')
    if  q>0:
        fpdf= FPDF()
        fpdf.add_page()
        fpdf.set_font("Arial", size=15)
        a=billarea.get('1.0',END)
        fpdf.multi_cell(0,5,a)
        fpdf.ln()
        m=bill_no.get()
        fpdf.output(opensave(filename))
        tttk.messagebox.showinfo('File Downloading...','Your bill has been downloaded as "Bill Number: '+str(m)+'.pdf"')
    else:
        ent1.focus()
#---------------------------------------------Print(user defined path)---------------------------------------    
def opensave():
    
    q=tttk.messagebox.askokcancel('Confirm Print','Do you want to print the bill?')
    if  q>0:
        try:
            fpdf= FPDF()
            fpdf.add_page()
            fpdf.set_font("Arial", size=15)
            a=str(billarea.get('1.0',END))
            fpdf.multi_cell(0,5,a)
            fpdf.ln()
            m=bill_no.get()
            #filname = os.path.basename(filename)
            files = [('All Files', '.*'), 
                     ('Python Files', '.py'),
                     ('Text Document', '.txt'),
                     ('PDF Document', '.pdf')]
            n=(tttk.filedialog.asksaveasfilename(filetypes = files, defaultextension = '.pdf'))
            fob=open(fpdf.output(n), 'w')
            fob.write(a)
            fob.close()
        except Exception:
            pass
        
        #tttk.messagebox.showinfo('File Downloading...','Your bill has been downloaded as "Bill Number: '+str(m)+'.pdf"')
    else:
        ent1.focus()
    
    
#========================================================Wrapper 2 Labels and Entry Boxes===================================

lbl1 =ttk.Label(wrapper2, text="Customer ID*:", width=20, justify= RIGHT)
lbl1.grid(row=0, column=1, padx=40, pady=15)
ent1 = ttk.Entry(wrapper2, textvariable= t1, width=30, font = ('roboto', 10, 'bold'))
ent1.grid(row=0, column=2, padx=10, pady=8)

lbl2 =ttk.Label(wrapper2, text="Account ID*:", width=20, justify= RIGHT)
lbl2.grid(row=0, column=3, padx=40, pady=15)
ent2 = ttk.Entry(wrapper2, textvariable= t8, width=30, font = ('roboto', 10, 'bold'))
ent2.grid(row=0, column=4, padx=10, pady=8)

lbl3 =ttk.Label(wrapper2, text="Meter Number*:", width=20, justify= RIGHT)
lbl3.grid(row=0, column=5, padx=40, pady=15)
ent3 = ttk.Entry(wrapper2, textvariable= t10, width=30, font = ('roboto', 10, 'bold'))
ent3.grid(row=0, column=6, padx=10, pady=8)

lbl4 =ttk.Label(wrapper2, text="Customer First Name:", width=20, justify= RIGHT)
lbl4.grid(row=1, column=1, padx=40, pady=15)
ent4 = ttk.Entry(wrapper2, textvariable= t2, width=30, font = ('roboto', 10, 'bold'), state =DISABLED)
ent4.grid(row=1, column=2, padx=10, pady=8)

lbl5 =ttk.Label(wrapper2, text="Customer Last Name:", width=20, justify= RIGHT)
lbl5.grid(row=1, column=3, padx=40, pady=15)
ent5 = ttk.Entry(wrapper2, textvariable= t3, width=30, font = ('roboto', 10, 'bold'), state =DISABLED)
ent5.grid(row=1, column=4, padx=10, pady=8)

lbl6 =ttk.Label(wrapper2, text="Address Line 1:", width=20, justify= RIGHT)
lbl6.grid(row=1, column=5, padx=40, pady=15)
ent6 = ttk.Entry(wrapper2, textvariable= t4, width=30, font = ('roboto', 10, 'bold'), state =DISABLED)
ent6.grid(row=1, column=6, padx=10, pady=8)

lbl7 =ttk.Label(wrapper2, text="Address Line 2:", width=20, justify= RIGHT)
lbl7.grid(row=2, column=1, padx=40, pady=15)
ent7 = ttk.Entry(wrapper2, textvariable= t5, width=30, font = ('roboto', 10, 'bold'), state =DISABLED)
ent7.grid(row=2, column=2, padx=10, pady=8)

lbl8 =ttk.Label(wrapper2, text="Pincode:", width=20, justify= RIGHT)
lbl8.grid(row=2, column=3, padx=40, pady=15)
ent8 = ttk.Entry(wrapper2, textvariable= t6, width=30, font = ('roboto', 10, 'bold'), state =DISABLED)
ent8.grid(row=2, column=4, padx=10, pady=8)

lbl9 =ttk.Label(wrapper2, text="Contact Number:", width=20, justify= RIGHT)
lbl9.grid(row=2, column=5, padx=40, pady=15)
ent9 = ttk.Entry(wrapper2, textvariable= t7, width=30, font = ('roboto', 10, 'bold'), state =DISABLED)
ent9.grid(row=2, column=6, padx=10, pady=8)


lbl10 =ttk.Label(wrapper2, text="Account Type:", width=20, justify= RIGHT)
lbl10.grid(row=3, column=1, padx=40, pady=15)
ent10 = ttk.Entry(wrapper2, textvariable= t9, width=30, font = ('roboto', 10, 'bold'), state =DISABLED)
ent10.grid(row=3, column=2, padx=10, pady=8)

lbl11 =ttk.Label(wrapper2, text="Previous Meter Reading:", width=20, justify= RIGHT)
lbl11.grid(row=3, column=3, padx=40, pady=15)
ent11 = ttk.Entry(wrapper2, textvariable= t11, width=30, font = ('roboto', 10, 'bold'), state =DISABLED)
ent11.grid(row=3, column=4, padx=10, pady=8)

lbl12 =ttk.Label(wrapper2, text="Current Meter Reading:", width=20, justify= RIGHT)
lbl12.grid(row=3, column=5, padx=40, pady=15)
ent12 = ttk.Entry(wrapper2, textvariable= t12, width=30, font = ('roboto', 10, 'bold'), state =DISABLED)
ent12.grid(row=3, column=6, padx=10, pady=8)

lbl13 =ttk.Label(wrapper2, text="Tarrif Implied:", width=20, justify= RIGHT)
lbl13.grid(row=4, column=1, padx=40, pady=15)
ent13 = ttk.Entry(wrapper2, textvariable= t13, width=30, font = ('roboto', 10, 'bold'), state =DISABLED)
ent13.grid(row=4, column=2, padx=10, pady=8)

lbl14 =ttk.Label(wrapper2, text="Units Used:", width=20, justify= RIGHT)
lbl14.grid(row=4, column=3, padx=40, pady=15)
ent14 = ttk.Entry(wrapper2, textvariable= t14, width=30, font = ('roboto', 10, 'bold'), state =DISABLED)
ent14.grid(row=4, column=4, padx=10, pady=8)

lbl15 =ttk.Label(wrapper2, text="Net Bill:", width=20, justify= RIGHT)
lbl15.grid(row=4, column=5, padx=40, pady=15)
ent15 = ttk.Entry(wrapper2, textvariable= t15, width=30, font = ('roboto', 10, 'bold'), state =DISABLED)
ent15.grid(row=4, column=6, padx=10, pady=8)

lbl16 =ttk.Label(wrapper2, text="Tax:", width=20, justify= RIGHT)
lbl16.grid(row=5, column=1, padx=40, pady=15)
ent16 = ttk.Entry(wrapper2, textvariable= t16, width=30, font = ('roboto', 10, 'bold'), state =DISABLED)
ent16.grid(row=5, column=2, padx=10, pady=8)

lbl17 =ttk.Label(wrapper2, text="Total Payable Amount:", width=20, justify= RIGHT)
lbl17.grid(row=5, column=5, padx=40, pady=15)
ent17 = ttk.Entry(wrapper2, textvariable= t17, width=30, font = ('roboto', 10, 'bold'), state =DISABLED)
ent17.grid(row=5, column=6, padx=10, pady=8)

#===============================================================Wrapper 3 Buttons and Bill=================================================
#================================================================InWrapper1================================================================
btn1=  ttk.Button(inwrapper1, text="Display Details", command = credentials, width=20)
btn1.grid(row=0, column=0, padx=10, pady=8)

btn2=  ttk.Button(inwrapper1, text="Clear", command = clear, width=20)
btn2.grid(row=0, column=1, padx=10, pady=8)

btn3=  ttk.Button(inwrapper1, text="Generate Bill", command = reciept, width=20)
btn3.grid(row=0, column=2, padx=10, pady=8)

btn4=  ttk.Button(inwrapper1, text="Pay Bill", command = paybill, width=20)
btn4.grid(row=1, column=0, padx=10, pady=8)

btn5=  ttk.Button(inwrapper1, text="Print Invoice", command = opensave, width=20)
btn5.grid(row=1, column=1, padx=10, pady=8)

btn6=  ttk.Button(inwrapper1, text="Exit", command = exitb, width=20)
btn6.grid(row=1, column=2, padx=10, pady=8)

btn7=  ttk.Button(inwrapper1, text="Request for Update", command = requp, width=20)
btn7.grid(row=2, column=1, padx=10, pady=8)
#====================================================================InWrapper2============================================================
s = ttk.Style()
s.configure('my.TLabel', font=('Century Schoolbook', 14, 'bold'))
bill_title= ttk.Label(inwrapper2, text= "Electricity Bill Window", relief= GROOVE, border=2, anchor =tttk.CENTER, style= 'my.TLabel')
bill_title.pack(fill=X)

scroll_bill=ttk.Scrollbar(inwrapper2, orient=VERTICAL)
billarea=Text(inwrapper2,width=80, height=12, yscrollcommand=scroll_bill)
scroll_bill.pack(side=RIGHT, fill=Y)
scroll_bill.config(command=billarea.yview)
billarea.pack()

 

root.mainloop()
