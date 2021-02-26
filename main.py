from tkinter import*
import calendar

root=Tk()
root.config(background="powderblue")
root.title("Calendar")
root.geometry("750x330")
root.resizable(0,0)

def show():
    a=int(spin1.get())
    b=int(spin2.get())
    cal=calendar.month(b,a)
    txt.delete(0.0,END)
    txt.insert(INSERT,cal)

lb=Label(root,text="CALENDAR",bg="teal",fg="black",font=('arial',30,'bold')).place(x=270,y=0)

lb11=Label(root,text="Month",bg="gray",fg="black",font=('arial',12,'bold')).place(x=300,y=60)
lb12=Label(root,text="Year",bg="gray",fg="black",font=('arial',12,'bold')).place(x=400,y=60)

spin1=Spinbox(root,values=(1,2,3,4,5,6,7,8,9,20,11,12),width=4)
spin1.place(x=355,y=60)

spin2=Spinbox(root,from_=1700,to_=2100,width=4)
spin2.place(x=442,y=60)

btn=Button(root,text="Show calendar",bg="purple",fg="black",font=('arial',10,'bold'),command=show).place(x=350,y=90)
txt=Text(root,width=40,height=10)
txt.place(x=200,y=123)

btn=Button(root,text="Exit",bg="purple",fg="black",font=('arial',10,'bold'),command=exit).place(x=350,y=290)

root.iconbitmap(r'new.ico')

root.mainloop()

