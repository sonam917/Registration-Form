from tkinter import *
from tkinter import messagebox


top =Tk()
top.geometry("800x500")
top.title('welcome')



def insert():
    k = e1.get()
    k2 = e2.get()
    k3 = e3.get()

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Admin7351', db='ssd')
    cur = db.cursor()
    s = "insert into rmp2 values('%s','%s','%s')" % (k, k2, k3)
    result = cur.execute(s)

    if(result>0):
        messagebox.showinfo("Result", "Record insert successfully")
    else:
        messagebox.showinfo("Result", "Record not inserted")

    db.commit()



l= Label(top, text= 'Registration Form',bg='lightgrey',fg='black',font=('Arial 30'))
l.place(x=300, y=50)

l2= Label(top,text='Name',bg='lightgrey',fg='black',font=('Arial 20'))
l2.place(x=200, y=150)

e1=Entry(top,font=('Arial 20'))
e1.place(x=350, y=150)
e2=Entry(top,font=('Arial 20'))

l3=Label(top,text='Lastname',bg='lightgrey',fg='black',font=('Arial 20'))
l3.place(x=200, y=200)

e2.place(x=350, y=200)

l4=Label(top,text='Password',bg='lightgrey',fg='black',font=('Arial 20'))
l4.place(x=200,y=250)

e3=Entry(top,font=('Arial 20'),show="*")
e3.place(x=350,y=250)

b1=Button(top,text='Submit',font=('Arial 20'),command=insert)
b1.place(x=450,y=350)


top.configure(bg='lightgrey')
top.mainloop()



