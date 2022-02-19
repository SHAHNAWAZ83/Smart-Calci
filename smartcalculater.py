from tkinter import*
from tkinter import messagebox
import math
screen=Tk()
screen.title('MY CALCULATER')
# screen.geometry("365x490")
screen.configure(bg="blue")

screen.maxsize(width=453,height=488)
# screen.minsize(width=453,height=490)
screen.minsize(width=453,height=488)

screen.iconbitmap(r"C:\Users\Shahnawaz\PycharmProjects\CALCULATOR\calu.ico.ico")

def click(number):
    global operater
    operater+=str(number)
    tex.set(operater)

def clear():
    global operater
    operater=""
    tex.set(operater)
def equal():
    global operater
    try:
        result=eval(operater)
        operater=str(result)
        tex.set(result)
    except:messagebox.showinfo('Notification','Try again something is wrong here',parent=screen)

def cmsin():
    global operater
    try:
        result=math.sin(eval(tex.get()))
        operater=str(result)
        tex.set(operater)
    except:messagebox.showinfo('Notification','Try again something is wrogn here',parent=screen )

def cmcos():
    global operater
    try:
        result=math.cos(eval(tex.get()))
        operater=str(result)
        tex.set(operater)
    except:messagebox.showinfo('Notification','Try again something is wrogn here',parent=screen )

def cmtan():
    global operater
    try:
        result=math.tan(eval(tex.get()))
        operater=str(result)
        tex.set(operater)
    except:messagebox.showinfo('Notification','Try again something is wrogn here',parent=screen )

def cmsqrt():
    global operater
    try:
        result=math.sqrt(eval(tex.get()))
        operater=str(result)
        tex.set(operater)
    except:messagebox.showinfo('Notification','Try again something is wrogn here',parent=screen )

def cmlog():
    global operater
    try:
        result=math.log(eval(tex.get()))
        operater=str(result)
        tex.set(operater)
    except:messagebox.showinfo('Notification','Try again something is wrogn here',parent=screen )

###############################binding function#####################################
def on_enter7(e):
    but7.configure(bg='red')
def on_leave7(e):
    but7.configure(bg="powder blue")

def on_enter8(e):
    but8.configure(bg='red')
def on_leave8(e):
    but8.configure(bg="powder blue")

def on_enter9(e):
    but9.configure(bg='red')
def on_leave9(e):
    but9.configure(bg="powder blue")

def on_enterADD(e):
    butADD.configure(bg='red')
def on_leaveADD(e):
    butADD.configure(bg="powder blue")

def on_enter4(e):
    but4.configure(bg='red')
def on_leave4(e):
    but4.configure(bg="powder blue")

def on_enter5(e):
    but5.configure(bg='red')
def on_leave5(e):
    but5.configure(bg="powder blue")

def on_enter6(e):
    but6.configure(bg='red')
def on_leave6(e):
    but6.configure(bg="powder blue")

def on_entersub(e):
    butsub.configure(bg='red')
def on_leavesub(e):
    butsub.configure(bg="powder blue")

def on_enter1(e):
    but1.configure(bg='red')
def on_leave1(e):
    but1.configure(bg="powder blue")

def on_enter2(e):
    but2.configure(bg='red')
def on_leave2(e):
    but2.configure(bg="powder blue")

def on_enter3(e):
    but3.configure(bg='red')
def on_leave3(e):
    but3.configure(bg="powder blue")

def on_entermul(e):
    butmul.configure(bg='red')
def on_leavemul(e):
    butmul.configure(bg="powder blue")

def on_enter0(e):
    but0.configure(bg='red')
def on_leave0(e):
    but0.configure(bg="powder blue")

def on_enterclear(e):
    butclear.configure(bg='red')
def on_leaveclear(e):
    butclear.configure(bg="powder blue")

def on_enterequal(e):
    butequal.configure(bg='red')
def on_leaveequal(e):
    butequal.configure(bg="powder blue")

def on_enterdiv(e):
    butdiv.configure(bg='red')
def on_leavediv(e):
    butdiv.configure(bg="powder blue")

def on_entersin(e):
    butsin.configure(bg='red')
def on_leavesin(e):
    butsin.configure(bg="powder blue")

def on_entercos(e):
    butcos.configure(bg='red')
def on_leavecos(e):
    butcos.configure(bg="powder blue")

def on_entertan(e):
    buttan.configure(bg='red')
def on_leavetan(e):
    buttan.configure(bg="powder blue")

def on_entersqrt(e):
    butsqrt.configure(bg='red')
def on_leavesqrt(e):
    butsqrt.configure(bg="powder blue")

def on_enterlog(e):
    butlog.configure(bg='red')
def on_leavelog(e):
    butlog.configure(bg="powder blue")




def on_entryenter(e):
    entry1.config(bg="red",fg='white')
def on_entryleave(e):
    entry1.configure(bg="orange",fg='black')
tex=StringVar()
operater=""
entry1=Entry(screen,bg='orange',font=('arial',20,'italic bold'),bd='30',justify='right',textvariable=tex)
entry1.grid(row=0,columnspan=4)

but7=Button(screen,text='7',font=('arial',20,'italic bold',),bd='8',padx=16,pady=16,command=lambda:click(7),activebackground='green',activeforeground='white',bg='powder blue')
but7.grid(row=1,column=0)

but8=Button(screen,text='8',font=('arial',20,'italic bold',),bd='8',padx=16,pady=16,command=lambda:click(8),activebackground='green',activeforeground='white',bg='powder blue')
but8.grid(row=1,column=1)

but9=Button(screen,text='9',font=('arial',20,'italic bold',),bd='8',padx=16,pady=16,command=lambda:click(9),activebackground='green',activeforeground='white',bg='powder blue')
but9.grid(row=1,column=2)

butADD=Button(screen,text='+',font=('arial',20,'italic bold',),bd='8',padx=16,pady=16,command=lambda:click('+'),activebackground='green',activeforeground='white',bg='powder blue')
butADD.grid(row=1,column=3)

but4=Button(screen,text='4',font=('arial',20,'italic bold',),bd='8',padx=16,pady=16,command=lambda:click(4),activebackground='green',activeforeground='white',bg='powder blue')
but4.grid(row=2,column=0)

but5=Button(screen,text='5',font=('arial',20,'italic bold',),bd='8',padx=16,pady=16,command=lambda:click(5),activebackground='green',activeforeground='white',bg='powder blue')
but5.grid(row=2,column=1)

but6=Button(screen,text='6',font=('arial',20,'italic bold',),bd='8',padx=16,pady=16,command=lambda:click(6),activebackground='green',activeforeground='white',bg='powder blue')
but6.grid(row=2,column=2)

butsub=Button(screen,text='-',font=('arial',20,'italic bold',),bd='8',padx=16,pady=16,command=lambda:click('-'),activebackground='green',activeforeground='white',bg='powder blue')
butsub.grid(row=2,column=3)

but1=Button(screen,text='1',font=('arial',20,'italic bold',),bd='8',padx=16,pady=16,command=lambda:click(1),activebackground='green',activeforeground='white',bg='powder blue')
but1.grid(row=3,column=0)

but2=Button(screen,text='2',font=('arial',20,'italic bold',),bd='8',padx=16,pady=16,command=lambda:click(2),activebackground='green',activeforeground='white',bg='powder blue')
but2.grid(row=3,column=1)

but3=Button(screen,text='3',font=('arial',20,'italic bold',),bd='8',padx=16,pady=16,command=lambda:click(3),activebackground='green',activeforeground='white',bg='powder blue')
but3.grid(row=3,column=2)

butmul=Button(screen,text='*',font=('arial',20,'italic bold',),bd='8',padx=16,pady=16,command=lambda:click("*"),activebackground='green',activeforeground='white',bg='powder blue')
butmul.grid(row=3,column=3)

but0=Button(screen,text='0',font=('arial',20,'italic bold',),bd='8',padx=16,pady=16,command=lambda:click(0),activebackground='green',activeforeground='white',bg='powder blue')
but0.grid(row=4,column=0)

butclear=Button(screen,text='C',font=('arial',20,'italic bold',),bd='8',padx=16,pady=16,command=clear,activebackground='green',activeforeground='white',bg='powder blue')
butclear.grid(row=4,column=1)

butequal=Button(screen,text='=',font=('arial',20,'italic bold',),bd='8',padx=16,pady=16,command=equal,activebackground='green',activeforeground='white',bg='powder blue')
butequal.grid(row=4,column=2)

butdiv=Button(screen,text='/',font=('arial',20,'italic bold',),bd='8',padx=16,pady=16,command=lambda:click('/'),activebackground='green',activeforeground='white',bg='powder blue')
butdiv.grid(row=4,column=3)

butsin=Button(screen,text='sin',font=('arial',15,'italic bold',),bd='8',padx=18,pady=20,command=cmsin,activebackground='green',activeforeground='white',bg='powder blue')
butsin.grid(row=0,column=4)

butcos=Button(screen,text='cos',font=('arial',15,'italic bold',),bd='8',padx=18,pady=20,command=cmcos,activebackground='green',activeforeground='white',bg='powder blue')
butcos.grid(row=1,column=4)

buttan=Button(screen,text='tan',font=('arial',15,'italic bold',),bd='8',padx=18,pady=20,command=cmtan,activebackground='green',activeforeground='white',bg='powder blue')
buttan.grid(row=2,column=4)

butsqrt=Button(screen,text='sqrt',font=('arial',15,'italic bold',),bd='8',padx=18,pady=20,command=cmsqrt,activebackground='green',activeforeground='white',bg='powder blue')
butsqrt.grid(row=3,column=4)

butlog=Button(screen,text='log',font=('arial',15,'italic bold',),bd='8',padx=18,pady=20,command=cmlog,activebackground='green',activeforeground='white',bg='powder blue')
butlog.grid(row=4,column=4)
###############################binding####################################################
entry1.bind('<Enter>',on_entryenter)
entry1.bind('<Leave>',on_entryleave)

butsin.bind('<Enter>',on_entersin)
butsin.bind('<Leave>',on_leavesin)

butcos.bind('<Enter>',on_entercos)
butcos.bind('<Leave>',on_leavecos)

buttan.bind('<Enter>',on_entertan)
buttan.bind('<Leave>',on_leavetan)

butsqrt.bind('<Enter>',on_entersqrt)
butsqrt.bind('<Leave>',on_leavesqrt)

butlog.bind('<Enter>',on_enterlog)
butlog.bind('<Leave>',on_leavelog)

but7.bind('<Enter>',on_enter7)
but7.bind('<Leave>',on_leave7)

but8.bind('<Enter>',on_enter8)
but8.bind('<Leave>',on_leave8)

but9.bind('<Enter>',on_enter9)
but9.bind('<Leave>',on_leave9)

butADD.bind('<Enter>',on_enterADD)
butADD.bind('<Leave>',on_leaveADD)

but4.bind('<Enter>',on_enter4)
but4.bind('<Leave>',on_leave4)

but5.bind('<Enter>',on_enter5)
but5.bind('<Leave>',on_leave5)

but6.bind('<Enter>',on_enter6)
but6.bind('<Leave>',on_leave6)

butsub.bind('<Enter>',on_entersub)
butsub.bind('<Leave>',on_leavesub)

but1.bind('<Enter>',on_enter1)
but1.bind('<Leave>',on_leave1)

but2.bind('<Enter>',on_enter2)
but2.bind('<Leave>',on_leave2)

but3.bind('<Enter>',on_enter3)
but3.bind('<Leave>',on_leave3)

butmul.bind('<Enter>',on_entermul)
butmul.bind('<Leave>',on_leavemul)

but0.bind('<Enter>',on_enter0)
but0.bind('<Leave>',on_leave0)

butclear.bind('<Enter>',on_enterclear)
butclear.bind('<Leave>',on_leaveclear)

butequal.bind('<Enter>',on_enterequal)
butequal.bind('<Leave>',on_leaveequal)

butdiv.bind('<Enter>',on_enterdiv)
butdiv.bind('<Leave>',on_leavediv)

screen.mainloop()
