from tkinter import *
from math import *
#---------show GUI---------
root=Tk()
root.title('Plot Curve Function of x         written by QiZH on 2014/7/19')

#-------define input area-------
frame4input=LabelFrame(root,text="Input Area",labelanchor='n')
frame4input.grid(column=0,row=0)
Label(frame4input).grid()
titles=("F(x)=","Step-factor(pixel) of x:","Min of x:","Max of x:","Min of F(x):","Max of F(x):","Color:")
d=1
parameters=list()
for c in titles:
    l1=Label(frame4input,borderwidth=3,text=c)
    l1.grid(stick="E",column=0,row=d)
    E1=Entry(frame4input)
    E1.grid(stick=W,column=1,row=d)
    parameters.append(E1)
    d+=1
#---------initialize the data-----    
parameters[0].insert(0,"cos(x)")
parameters[1].insert(0,"3")
parameters[2].insert(0,"-2*pi")
parameters[3].insert(0,"2*pi")
parameters[4].insert(0,"-1.2")
parameters[5].insert(0,"1.2")
parameters[6].insert(0,"red")

#-----define plot area--------
canvas=Canvas(root,width=400,height=400,bg="white")
canvas.grid(column=1,row=0)
print(canvas["width"])
#------conversion to coordinate of screen----
    
def conversion2s(x,y):  #conversion the position to screen coordinate
    w=float(canvas["width"])
    h=float(canvas["height"])
    a1=eval(parameters[2].get())
    a2=eval(parameters[3].get())
    b1=eval(parameters[4].get())
    b2=eval(parameters[5].get())
    x1=w*(x-a1)/(a2-a1)
    y1=h*(y-b2)/(b1-b2)
    return (int(x1),int(y1))  #it must be integer

#------conversion to coordinate of screen----
    
def conversion2t(x,y):    #conversion the position to theory coordinate
    w=float(canvas["width"])
    h=float(canvas["height"])
    a1=eval(parameters[2].get())
    a2=eval(parameters[3].get())
    b1=eval(parameters[4].get())
    b2=eval(parameters[5].get())
    x1=(a2-a1)*x/w+a1
    y1=(b1-b2)*y/h+b2
    print(x1,y1)
    return (x1,y1)  # it must be float

#--------------------
def plot():
    print("i am in plot")
    #canvas.master
    calme=parameters[0].get()
    #-----calculate the step according s-factor--
    sfactor=eval(parameters[1].get())
    p1=conversion2t(sfactor,0)
    p2=conversion2t(0,0)
    step=p1[0]-p2[0]
    print(step)
    
    a1=eval(parameters[2].get())
    a2=eval(parameters[3].get())
    b1=eval(parameters[4].get())
    b2=eval(parameters[5].get())
    mycolor=parameters[6].get()
    print(mycolor)
    #----draw x and y axis
    p1=conversion2s(a1,0)
    p2=conversion2s(a2,0)
    p3=conversion2s(0,b1)
    p4=conversion2s(0,b2)
    canvas.create_line(p1,p2)
    canvas.create_line(p3,p4)
    #----draw-----
    x=a1
    pLast=""
    p=(0,0)
    while x<a2:
        try:
            y=eval(calme)
            p=conversion2s(x,y)
        except:
            pLast=(x,0)
        if pLast=="": # the first Last point
            pLast=p
        canvas.create_line(pLast,p,fill=mycolor)
        pLast=p
        x=x+step

#------run plot drawing-------    
Button1=Button(frame4input,text="Plot!",command=plot)
Button1.grid()
Button2=Button(frame4input,text="Clear!",command=plot)
Button2.grid()

#--------mainloop-------------
root.mainloop()
