from tkinter import *

u1 = [None, None, None]
v1 = [None, None, None]
u2 = [None, None, None]
v2 = [None, None, None]

root = Tk()
root.geometry("490x310")
root.resizable(False, False)
root.title("Lines.py")
bg = PhotoImage(file = 'bg.png')

def printValue():
    u1[0] = int(u1tf1.get())
    u1[1] = int(u1tf2.get())
    u1[2] = int(u1tf3.get())

    v1[0] = int(v1tf1.get())
    v1[1] = int(v1tf2.get())
    v1[2] = int(v1tf3.get())

    u2[0] = int(u2tf1.get())
    u2[1] = int(u2tf2.get())
    u2[2] = int(u2tf3.get())

    v2[0] = int(v2tf1.get())
    v2[1] = int(v2tf2.get())
    v2[2] = int(v2tf3.get())
    print(u1,u2,v1,v2)

    if 0 in v2:
        x1 = [i / j for i, j in zip(v2, v1)]
    else:
        x1 = [i / j for i, j in zip(v1, v2)]

    if (x1[0] == x1[1] == x1[2]):
        Label(root, text ="The directional vectors are related",bg='white').place(x=35,y=155)
        x2 = [i - j for i, j in zip(u2, u1)]
        x3 = [i / j for i, j in zip(x2, v1)]
        if(x3[0] == x3[1] == x3[2]):
            Label(root, text ="The Lines are identical",bg='white').place(x=35,y=170)
            return
        else:
            Label(root, text ="The lines are parallel",bg='white').place(x=35,y=170)
    else:
        Label(root, text ="The directional vectors have no relation",bg='white').place(x=35,y=155)
        x4 = [(u2[0] - u1[0]) / v1[0], v2[0] / v1[0]]
        x5 = u1[1] * x4
        if not x5:
            Label(root, text ="The lines are distorted",bg='white').place(x=35,y=170)
        else:
            x6 = v2[1] - x5[1]
            x7 = u2[1] - u1[1]
            x8 = x7 / x6
            Label(root, text =("x1 = "+str(x8)),bg='white').place(x=35,y=185)
            x9 = x4[0] + x4[1] * x8
            Label(root, text =(("x2 = "+str(x9))),bg='white').place(x=35,y=200)
            x10 = u1[2] + v1[2] * x9
            x11 = u2[2] + v2[2] * x8
            if(x10 == x11):
                Label(root, text ="The lines intersect",bg='white').place(x=35,y=170)
                x12 = x9 * v1 + u1
                Label(root, text =("Intersection = "+str(x12)),bg='white').place(x=35,y=215)
            else:
                Label(root, text ="The lines are distorted",bg='white').place(x=35,y=170)
                x13 = [x10, x11]
            Label(root, text =("LGS: "+str(x13[0])+" = "+str(x13[1])),bg='white').place(x=35,y=215)

labelbg = Label(root, image = bg)
labelbg.place(x = 0, y = 0)

u1tf1 = Entry(root,width=3,bg='#f0f0f0')
u1tf1.place(x=105,y=70)
u1tf2 = Entry(root,width=3,bg='#f0f0f0')
u1tf2.place(x=105,y=90)
u1tf3 = Entry(root,width=3,bg='#f0f0f0')
u1tf3.place(x=105,y=110)

v1tf1 = Entry(root,width=3,bg='#f0f0f0')
v1tf1.place(x=194,y=70)
v1tf2 = Entry(root,width=3,bg='#f0f0f0')
v1tf2.place(x=194,y=90)
v1tf3 = Entry(root,width=3,bg='#f0f0f0')
v1tf3.place(x=194,y=110)

u2tf1 = Entry(root,width=3,bg='#f0f0f0')
u2tf1.place(x=338,y=70)
u2tf2 = Entry(root,width=3,bg='#f0f0f0')
u2tf2.place(x=338,y=90)
u2tf3 = Entry(root,width=3,bg='#f0f0f0')
u2tf3.place(x=338,y=110)

v2tf1 = Entry(root,width=3,bg='#f0f0f0')
v2tf1.place(x=427,y=70)
v2tf2 = Entry(root,width=3,bg='#f0f0f0')
v2tf2.place(x=427,y=90)
v2tf3 = Entry(root,width=3,bg='#f0f0f0')
v2tf3.place(x=427,y=110)

def close():
    root.quit()

button1 = Button(root, text="Quit",font=("Calibri",10), command=close,height=1,width=5,).place(x=439,y=278)
button2 = Button(root, text="Calculate",font=("Calibri",10), command=printValue,height=1,width=7,).place(x=5,y=278)

frame1 = Frame(root)
frame1.pack(pady = 20 )

root.mainloop()
