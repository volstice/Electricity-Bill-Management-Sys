#==============================================================Imports======================================================
from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import tkinter as tttk
from ttkthemes import themed_tk as tk
from subprocess import call
import mysql.connector

#=============================================================Tkinter Frames========================================================
b= tk.ThemedTk()
b.get_themes()                 
b.set_theme("radiance")
b.title('Electricity Bill Management System')
b.geometry('1350x750+0+0')
b.config(bg='#F5F5F5')
b.state("zoomed")
b.iconbitmap(r'E:\Electricity Billing System\icon.ico')


uname = StringVar()
paswd = StringVar()

#=============================================================================Main Frame (Login)=============================================================================

mainframe=  Frame(b, bg = '#F5F5F5')
mainframe.grid()

b.txtno=ttk.Label(mainframe,text= '###:', font= ('Calibri', 32,  'bold'),  background= '#F5F5F5', foreground='#F5F5F5')
b.txtno.grid(row=0, column=0)

b.txtno5=ttk.Label(mainframe,text= '###:', font= ('Calibri', 30,  'bold'),  background= '#F5F5F5', foreground='#F5F5F5')
b.txtno5.grid(row=7, column=0)

b.txtno3=ttk.Label(mainframe,text= '###:', font= ('Calibri', 30,  'bold'),  background='#F5F5F5', foreground='#F5F5F5')
b.txtno3.grid(row=11, column=0)

titframe = Frame(mainframe, bd= 2, padx=120, pady= 8, bg= 'Ghost White', relief= RIDGE)
titframe.grid(row=1,column=0)
b.txtno=Label(mainframe,text= 'Username:', font= ('Calibri', 30,  'bold'),  background= '#F5F5F5', foreground='#F5F5F5')
b.txtno.grid(row=4, column=0)

b.lbltit= ttk.Label (titframe, font= ('Century Schoolbook', 47,  'bold'), text= '  Electricity Bill Management System',width=40, background= 'Ghost white')
b.lbltit.grid(row=0, column=0)

dataframe = Frame(mainframe, bd= 1, width= 1300, height= 200, padx= 455,pady= 20, bg= 'ghost white', relief= RIDGE)
dataframe.grid(row=6, column=0)

staffframe = Frame(mainframe, bd= 1, width= 1300, height= 200, padx= 455,pady= 20, bg= 'ghost white', relief= RIDGE)
staffframe.grid(row=10, column=0)

exframe=Frame(mainframe, bd= 1, width= 1300, height= 200, padx= 718,pady= 20, bg= 'ghost white', relief= RIDGE)
exframe.grid(row=12, column=0)

     

def credentials():
    import mysql.connector as c
    chk=0
    con=c.connect(host="localhost",user="root",passwd="sandy",database="ebms")

    d=uname.get()
    c=paswd.get()

    cursor=con.cursor()  
    cursor.execute( "select * from admin")
    row=cursor.fetchall()
    for i in row:
        if i[0]==d and i[4]==c:
            chk=1
            break
    if chk==1:
        uname.set('')
        paswd.set('')
        b.txtuname.focus()
        call(["python","Adminpage.py"])
        con.commit()
        

    else:
        q=tkinter.messagebox.askyesno('Login Error','Please check the Login details')
        uname.set('')
        paswd.set('')
           
        if  q>0:
            b.txtuname.focus()
        else:
            p=tkinter.messagebox.askyesno('Exit','Do you want to Quit?')
            if p>0:
                b.destroy()
                return
            else:
                b.txtuname.focus()
    con.commit()



def window():
    call(["python","Customer Details.py"])


def qexit():
        qexit=tkinter.messagebox.askyesno('Exit Restaurant System', 'Confirm to exit')
        if qexit>0:
            b.destroy()
            return
s = ttk.Style()
s.configure('my.TButton', font=('Century Schoolbook', 14))
b.exbtn = ttk.Button (exframe, text= 'Exit',width= 20, command= qexit, style='my.TButton')
b.exbtn.grid(row=4, column=1)



b.lbltit= ttk.Label (dataframe, font= ('Century Schoolbook', 25,  'bold'), text= 'Admin Login:', background= 'Ghost white')
b.lbltit.grid(row=0, column= 0, sticky=W)

b.lbluname= ttk.Label (dataframe, font= ('Century Schoolbook', 20,  'bold'), text= '    Admin_ID:', background= 'Ghost white')
b.lbluname.grid(row=2, column= 0, sticky=W)
b.txtuname= ttk.Entry (dataframe, font= ('Calibri', 20,  'bold'), textvariable= uname,width= 20)
b.txtuname.grid(row=2, column= 2)

b.lblpaswd= ttk.Label (dataframe, font= ('Century Schoolbook', 20,  'bold'), text= '    Password:',  background= 'Ghost white')
b.lblpaswd.grid(row=3, column= 0, sticky=W)
b.txtpaswd= ttk.Entry (dataframe, font= ('Calibri', 20,  'bold'), textvariable= paswd,width= 20, show='*')
b.txtpaswd.grid(row=3, column= 2)

b.btnlogin = ttk.Button (dataframe, text= 'Login', width= 20, command=credentials,  style='my.TButton' )
b.btnlogin.grid(row=4, column=1)

b.lbltit= ttk.Label (staffframe, font= ('Century Schoolbook', 25,  'bold'), text= 'Customer Login:', width= 41,  background= 'Ghost white')
b.lbltit.grid(row=1, column= 1, sticky=W)

b.btnlogin = ttk.Button (staffframe, text= 'Proceed',  width= 20,  style='my.TButton', command=window)
b.btnlogin.grid(row=3, column=1)


b.txtuname.focus()


b.mainloop()
